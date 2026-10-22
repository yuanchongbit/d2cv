"""Plotting helpers with a consistent style."""

from __future__ import annotations

from math import ceil

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


def set_chinese_font() -> str | None:
    """Pick an available CJK font for matplotlib and return its name."""
    candidates = [
        "PingFang SC",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "Arial Unicode MS",
    ]
    available = {font.name for font in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in available:
            plt.rcParams["font.sans-serif"] = [name]
            plt.rcParams["axes.unicode_minus"] = False
            return name
    plt.rcParams["axes.unicode_minus"] = False
    return None


def _to_display(image: object) -> np.ndarray:
    if hasattr(image, "detach"):
        image = image.detach().cpu().numpy()
    array = np.asarray(image)
    if array.ndim == 3 and array.shape[0] in (1, 3):
        array = np.transpose(array, (1, 2, 0))
    if array.ndim == 3 and array.shape[0] == 1:
        array = array[0]
    return array


def show_images(
    images: list | tuple,
    titles: list[str] | None = None,
    ncols: int = 4,
    figsize=None,
):
    """Show a batch of images in a grid."""
    images = list(images)
    if not images:
        raise ValueError("images must not be empty")

    ncols = max(1, min(ncols, len(images)))
    nrows = ceil(len(images) / ncols)
    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=figsize or (3 * ncols, 3 * nrows),
        squeeze=False,
    )

    for i, ax in enumerate(axes.flat):
        ax.axis("off")
        if i >= len(images):
            continue
        array = _to_display(images[i])
        ax.imshow(array, cmap="gray" if array.ndim == 2 else None)
        if titles is not None:
            ax.set_title(titles[i])
    return fig


def plot_history(history: dict[str, list[float]], keys: list[str] | None = None):
    """Plot one or more metric curves from a training history."""
    keys = keys or list(history)
    fig, axes = plt.subplots(1, len(keys), figsize=(4 * len(keys), 3), squeeze=False)
    for ax, key in zip(axes.flat, keys, strict=False):
        ax.plot(history[key])
        ax.set_title(key)
        ax.set_xlabel("epoch")
    return fig
