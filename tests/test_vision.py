import numpy as np
from PIL import Image

from d2cv.vision import box_cxcywh_to_xyxy, box_xyxy_to_cxcywh, draw_boxes, draw_masks


def test_box_conversion_roundtrip():
    boxes = np.array([[10, 20, 50, 80], [0, 0, 10, 10]], dtype=float)
    converted = box_cxcywh_to_xyxy(box_xyxy_to_cxcywh(boxes))
    assert np.allclose(converted, boxes)


def test_draw_boxes_preserves_size():
    image = Image.new("RGB", (100, 80), "white")
    result = draw_boxes(image, [[10, 10, 50, 60]], labels=["cat"], scores=[0.9])
    assert result.size == image.size
    assert result is not image


def test_draw_masks_preserves_size():
    image = np.full((32, 48, 3), 255, dtype=np.uint8)
    masks = np.zeros((2, 32, 48), dtype=bool)
    masks[0, :16] = True
    masks[1, 16:] = True
    result = draw_masks(image, masks)
    assert result.size == (48, 32)
