"""Print the local environment used by the book."""

from __future__ import annotations

import platform
import sys

import torch
import torchvision

import d2cv


def main() -> None:
    print(f"python      : {sys.version.split()[0]}")
    print(f"platform    : {platform.platform()}")
    print(f"machine     : {platform.machine()}")
    print(f"torch       : {torch.__version__}")
    print(f"torchvision : {torchvision.__version__}")
    print(f"d2cv        : {d2cv.__version__}")
    print(f"cuda        : {torch.cuda.is_available()}")
    print(f"mps         : {torch.backends.mps.is_available()}")
    print(f"device      : {d2cv.get_device()}")


if __name__ == "__main__":
    main()
