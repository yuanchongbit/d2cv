"""Dataset download, extraction, and split helpers."""

from __future__ import annotations

import hashlib
import tarfile
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
import torch


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download_file(url: str, dest: str | Path, sha256: str | None = None) -> Path:
    """Download a file unless it already exists with the expected checksum."""
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        if sha256 is None or _sha256(dest) == sha256:
            return dest

    tmp = dest.with_suffix(dest.suffix + ".part")
    urllib.request.urlretrieve(url, tmp)
    if sha256 is not None and _sha256(tmp) != sha256:
        tmp.unlink(missing_ok=True)
        raise ValueError(f"Checksum mismatch for {url}")
    tmp.replace(dest)
    return dest


def extract_archive(path: str | Path, dest: str | Path) -> Path:
    """Extract a .zip, .tar, .tar.gz, or .tgz archive."""
    path = Path(path)
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)

    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            zf.extractall(dest)
    elif tarfile.is_tarfile(path):
        with tarfile.open(path) as tf:
            tf.extractall(dest, filter="data")
    else:
        raise ValueError(f"Unsupported archive: {path}")
    return dest


def split_indices(n: int, val_ratio: float = 0.2, seed: int = 42) -> tuple[list[int], list[int]]:
    """Split range(n) into disjoint train/val index lists."""
    if not 0 < val_ratio < 1:
        raise ValueError("val_ratio must be in (0, 1)")
    indices = np.random.default_rng(seed).permutation(n)
    n_val = int(round(n * val_ratio))
    return indices[n_val:].tolist(), indices[:n_val].tolist()


def denormalize(
    tensor: torch.Tensor,
    mean: tuple[float, ...] = (0.485, 0.456, 0.406),
    std: tuple[float, ...] = (0.229, 0.224, 0.225),
) -> np.ndarray:
    """Convert a normalized CHW tensor to an HWC uint8 array."""
    t = tensor.detach().cpu().float()
    mean_t = torch.as_tensor(mean, dtype=t.dtype).view(-1, 1, 1)
    std_t = torch.as_tensor(std, dtype=t.dtype).view(-1, 1, 1)
    t = (t * std_t + mean_t).clamp(0, 1)
    return (t.permute(1, 2, 0).numpy() * 255).round().astype(np.uint8)
