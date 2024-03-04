import time
from pathlib import Path

import torch

from src.packages.training.load_utils import _load_model


def load_from_bin(
    checkpoint_path: Path = Path("."),
    device='mps',
) -> torch.nn:
    """Generates text samples based on a pre-trained Transformer model and tokenizer.
    """

    tokenizer_path = checkpoint_path / "tokenizer.model"
    assert tokenizer_path.is_file(), tokenizer_path
    print(f"Using device={device}")

    precision = torch.float16

    print("Loading model ...")
    t0 = time.time()
    model = _load_model(checkpoint_path, device, precision, use_tp=False)

    print(f"Time to load model: {time.time() - t0:.02f} seconds")

    return model