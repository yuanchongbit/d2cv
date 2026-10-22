"""Evaluation utilities used across chapters."""

from __future__ import annotations

import numpy as np

ArrayLike = np.ndarray | list | tuple


def _to_numpy(x: ArrayLike | object) -> np.ndarray:
    if hasattr(x, "detach"):
        x = x.detach().cpu().numpy()
    return np.asarray(x)


class AverageMeter:
    """Track a running average of a scalar."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.val = 0.0
        self.sum = 0.0
        self.count = 0

    def update(self, val: float, n: int = 1) -> None:
        self.val = float(val)
        self.sum += float(val) * n
        self.count += n

    @property
    def avg(self) -> float:
        return self.sum / self.count if self.count else 0.0


def accuracy(
    output: ArrayLike | object,
    target: ArrayLike | object,
    topk: tuple[int, ...] = (1,),
) -> list[float]:
    """Return top-k accuracy in percent."""
    logits = _to_numpy(output)
    labels = _to_numpy(target).reshape(-1)
    max_k = min(max(topk), logits.shape[1])
    topk = tuple(min(k, max_k) for k in topk)
    pred = np.argsort(-logits, axis=1)[:, :max_k]
    correct = pred == labels[:, None]
    return [float(correct[:, :k].any(axis=1).mean() * 100) for k in topk]


def box_iou(boxes1: ArrayLike | object, boxes2: ArrayLike | object) -> np.ndarray:
    """Compute pairwise IoU for boxes in xyxy format."""
    b1 = _to_numpy(boxes1).astype(np.float64).reshape(-1, 4)
    b2 = _to_numpy(boxes2).astype(np.float64).reshape(-1, 4)
    if len(b1) == 0 or len(b2) == 0:
        return np.zeros((len(b1), len(b2)), dtype=np.float64)

    lt = np.maximum(b1[:, None, :2], b2[None, :, :2])
    rb = np.minimum(b1[:, None, 2:], b2[None, :, 2:])
    wh = np.clip(rb - lt, 0.0, None)
    inter = wh[..., 0] * wh[..., 1]

    area1 = np.clip(b1[:, 2] - b1[:, 0], 0.0, None) * np.clip(b1[:, 3] - b1[:, 1], 0.0, None)
    area2 = np.clip(b2[:, 2] - b2[:, 0], 0.0, None) * np.clip(b2[:, 3] - b2[:, 1], 0.0, None)
    union = area1[:, None] + area2[None, :] - inter
    return np.divide(inter, union, out=np.zeros_like(inter), where=union > 0)


def nms(
    boxes: ArrayLike | object,
    scores: ArrayLike | object,
    iou_threshold: float = 0.5,
) -> np.ndarray:
    """Greedy non-maximum suppression; returns kept indices."""
    boxes = _to_numpy(boxes).astype(np.float64).reshape(-1, 4)
    scores = _to_numpy(scores).astype(np.float64).reshape(-1)
    if len(boxes) == 0:
        return np.empty((0,), dtype=np.int64)

    order = np.argsort(-scores)
    keep: list[int] = []
    while order.size > 0:
        i = int(order[0])
        keep.append(i)
        if order.size == 1:
            break
        ious = box_iou(boxes[i : i + 1], boxes[order[1:]])[0]
        order = order[1:][ious <= iou_threshold]
    return np.asarray(keep, dtype=np.int64)


def segmentation_iou(
    pred: ArrayLike | object,
    target: ArrayLike | object,
    num_classes: int,
    ignore_index: int | None = None,
) -> tuple[np.ndarray, float]:
    """Return per-class IoU and mIoU; classes without union are ignored in mIoU."""
    pred = _to_numpy(pred).reshape(-1)
    target = _to_numpy(target).reshape(-1)
    valid = np.ones_like(target, dtype=bool) if ignore_index is None else target != ignore_index
    pred = pred[valid]
    target = target[valid]

    ious = []
    for cls in range(num_classes):
        if ignore_index is not None and cls == ignore_index:
            continue
        p = pred == cls
        t = target == cls
        union = np.logical_or(p, t).sum()
        inter = np.logical_and(p, t).sum()
        ious.append(float(inter / union) if union else float("nan"))

    ious_arr = np.asarray(ious, dtype=np.float64)
    miou = float(np.nanmean(ious_arr)) if np.any(~np.isnan(ious_arr)) else 0.0
    return ious_arr, miou
