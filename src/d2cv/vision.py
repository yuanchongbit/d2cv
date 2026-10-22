"""Vision helpers for boxes, masks, and coordinates."""

from __future__ import annotations

import numpy as np
from PIL import Image, ImageDraw

ArrayLike = np.ndarray | list | tuple


def _to_numpy(x: ArrayLike | object) -> np.ndarray:
    if hasattr(x, "detach"):
        x = x.detach().cpu().numpy()
    return np.asarray(x)


def box_xyxy_to_cxcywh(boxes: ArrayLike | object) -> np.ndarray:
    boxes = _to_numpy(boxes).astype(np.float64).reshape(-1, 4)
    x1, y1, x2, y2 = boxes.T
    return np.stack([(x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1], axis=1)


def box_cxcywh_to_xyxy(boxes: ArrayLike | object) -> np.ndarray:
    boxes = _to_numpy(boxes).astype(np.float64).reshape(-1, 4)
    cx, cy, w, h = boxes.T
    return np.stack([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], axis=1)


def draw_boxes(
    image: Image.Image | np.ndarray,
    boxes: ArrayLike | object,
    labels: ArrayLike | None = None,
    scores: ArrayLike | None = None,
    color: tuple[int, int, int] = (255, 64, 64),
    width: int = 2,
) -> Image.Image:
    """Draw xyxy boxes on a copy of the image."""
    img = image.copy() if isinstance(image, Image.Image) else Image.fromarray(np.asarray(image))
    draw = ImageDraw.Draw(img)
    boxes = _to_numpy(boxes).astype(np.float64).reshape(-1, 4)

    for i, (x1, y1, x2, y2) in enumerate(boxes):
        draw.rectangle([float(x1), float(y1), float(x2), float(y2)], outline=color, width=width)
        if labels is not None:
            text = str(labels[i])
            if scores is not None:
                text += f" {float(scores[i]):.2f}"
            draw.text((float(x1) + 3, float(y1) + 3), text, fill=color)
    return img


def draw_masks(
    image: Image.Image | np.ndarray,
    masks: ArrayLike | object,
    colors: ArrayLike | None = None,
    alpha: float = 0.4,
) -> Image.Image:
    """Blend binary masks over a copy of the image."""
    array = np.asarray(image.convert("RGB") if isinstance(image, Image.Image) else image)
    base = array.astype(np.float32)
    masks = _to_numpy(masks)
    if masks.ndim == 2:
        masks = masks[None]

    if colors is None:
        colors = np.array(
            [
                [255, 64, 64],
                [64, 200, 64],
                [64, 96, 255],
                [255, 200, 64],
                [220, 64, 220],
                [64, 220, 220],
            ],
            dtype=np.float32,
        )
    colors = np.asarray(colors, dtype=np.float32).reshape(-1, 3)

    overlay = base.copy()
    for i, mask in enumerate(masks):
        overlay[mask.astype(bool)] = colors[i % len(colors)]

    blended = (1 - alpha) * base + alpha * overlay
    return Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8))
