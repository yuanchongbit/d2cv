"""PyTorch training utilities."""

from __future__ import annotations

import random
import time
from collections.abc import Iterable

import numpy as np
import torch
from torch import nn


def set_seed(seed: int, deterministic: bool = False) -> None:
    """Seed Python, NumPy, and PyTorch."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def count_parameters(model: nn.Module, trainable_only: bool = True) -> int:
    params = model.parameters()
    return sum(p.numel() for p in params if p.requires_grad or not trainable_only)


class Timer:
    """Wall-clock timer with CUDA synchronization."""

    def __init__(self, device: torch.device | str | None = None) -> None:
        self.device = device
        self.elapsed = 0.0
        self._start = 0.0

    def _synchronize(self) -> None:
        if self.device is None:
            return
        device = torch.device(self.device)
        if device.type == "cuda" and torch.cuda.is_available():
            torch.cuda.synchronize(device)

    def __enter__(self) -> Timer:
        self._synchronize()
        self._start = time.perf_counter()
        return self

    def __exit__(self, *exc: object) -> None:
        self._synchronize()
        self.elapsed = time.perf_counter() - self._start


def train_one_epoch(
    model: nn.Module,
    loader: Iterable,
    optimizer: torch.optim.Optimizer,
    criterion: nn.Module,
    device: torch.device,
    scheduler: object | None = None,
    scaler: torch.amp.GradScaler | None = None,
    max_batches: int | None = None,
) -> float:
    """Train for one epoch and return the sample-weighted mean loss."""
    model.train()
    total_loss = 0.0
    total_samples = 0

    for step, (images, targets) in enumerate(loader):
        if max_batches is not None and step >= max_batches:
            break
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)
        optimizer.zero_grad(set_to_none=True)

        if scaler is not None:
            with torch.autocast(device_type=device.type):
                loss = criterion(model(images), targets)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            loss = criterion(model(images), targets)
            loss.backward()
            optimizer.step()

        if scheduler is not None:
            scheduler.step()

        batch_size = images.size(0)
        total_loss += float(loss.detach()) * batch_size
        total_samples += batch_size

    return total_loss / max(total_samples, 1)


@torch.inference_mode()
def evaluate_accuracy(
    model: nn.Module,
    loader: Iterable,
    device: torch.device,
    max_batches: int | None = None,
) -> float:
    """Return top-1 accuracy in percent."""
    model.eval()
    correct = 0
    total = 0
    for step, (images, targets) in enumerate(loader):
        if max_batches is not None and step >= max_batches:
            break
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)
        preds = model(images).argmax(dim=1)
        correct += int((preds == targets).sum())
        total += targets.numel()
    return 100.0 * correct / max(total, 1)
