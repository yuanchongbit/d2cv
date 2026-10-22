"""Shared utilities for the D2CV book."""

from .data import denormalize, download_file, extract_archive, split_indices
from .metrics import AverageMeter, accuracy, box_iou, nms, segmentation_iou
from .plot import plot_history, set_chinese_font, show_images
from .torch import (
    Timer,
    count_parameters,
    evaluate_accuracy,
    get_device,
    set_seed,
    train_one_epoch,
)
from .vision import box_cxcywh_to_xyxy, box_xyxy_to_cxcywh, draw_boxes, draw_masks

__version__ = "0.1.0"

__all__ = [
    "AverageMeter",
    "Timer",
    "accuracy",
    "box_cxcywh_to_xyxy",
    "box_iou",
    "box_xyxy_to_cxcywh",
    "count_parameters",
    "denormalize",
    "download_file",
    "draw_boxes",
    "draw_masks",
    "evaluate_accuracy",
    "extract_archive",
    "get_device",
    "nms",
    "plot_history",
    "segmentation_iou",
    "set_chinese_font",
    "set_seed",
    "show_images",
    "split_indices",
    "train_one_epoch",
]
