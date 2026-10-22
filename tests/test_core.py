import numpy as np
import torch
from torch import nn

from d2cv.data import denormalize, split_indices
from d2cv.torch import count_parameters, get_device, set_seed


def test_set_seed_reproducible():
    set_seed(123)
    a = torch.randn(4)
    set_seed(123)
    b = torch.randn(4)
    assert torch.equal(a, b)


def test_count_parameters():
    model = nn.Linear(4, 2)
    assert count_parameters(model) == 10


def test_get_device_returns_device():
    assert isinstance(get_device(), torch.device)


def test_split_indices_disjoint():
    train, val = split_indices(100, val_ratio=0.2, seed=7)
    assert len(train) == 80
    assert len(val) == 20
    assert set(train).isdisjoint(val)


def test_denormalize_shape_and_range():
    tensor = torch.zeros(3, 8, 8)
    array = denormalize(tensor)
    assert array.shape == (8, 8, 3)
    assert array.min() >= 0
    assert array.max() <= 255
    assert np.isfinite(array).all()
