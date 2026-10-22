import numpy as np
import torch

from d2cv.metrics import AverageMeter, accuracy, box_iou, nms, segmentation_iou


def test_accuracy_top1():
    logits = torch.tensor([[0.1, 0.9], [0.8, 0.2]])
    target = torch.tensor([1, 0])
    assert accuracy(logits, target) == [100.0]


def test_accuracy_top2():
    logits = torch.tensor([[0.1, 0.9, 0.0], [0.8, 0.2, 0.1]])
    target = torch.tensor([0, 1])
    assert accuracy(logits, target, topk=(1, 2)) == [0.0, 100.0]


def test_box_iou():
    boxes1 = np.array([[0, 0, 10, 10], [10, 10, 20, 20]], dtype=float)
    boxes2 = np.array([[0, 0, 5, 10]], dtype=float)
    ious = box_iou(boxes1, boxes2)
    assert ious.shape == (2, 1)
    assert np.isclose(ious[0, 0], 0.5)
    assert np.isclose(ious[1, 0], 0.0)


def test_nms():
    boxes = np.array([[0, 0, 10, 10], [1, 1, 11, 11], [20, 20, 30, 30]], dtype=float)
    scores = np.array([0.9, 0.8, 0.7])
    assert nms(boxes, scores, iou_threshold=0.5).tolist() == [0, 2]


def test_segmentation_iou_perfect():
    target = np.array([[0, 1], [1, 1]])
    pred = target.copy()
    per_class, miou = segmentation_iou(pred, target, num_classes=2)
    assert per_class.tolist() == [1.0, 1.0]
    assert miou == 1.0


def test_average_meter():
    meter = AverageMeter()
    meter.update(2.0)
    meter.update(4.0, n=3)
    assert np.isclose(meter.avg, 3.5)
