import torch

from src.packages.training.model_utils import Transformer


def _load_model(checkpoint_path, device, precision, use_tp):
    with torch.device('meta'):
        model = Transformer.from_json(str(checkpoint_path / "config.json"))

    checkpoint = torch.load(str(checkpoint_path / "pytorch_model.bin"), mmap=True, weights_only=True)
    model.load_state_dict(checkpoint, strict=False, assign=True)
    for name, module in model.named_modules():
        if hasattr(module, "weight_type"):
            module.weight_type_int = int(module.weight_type)

    if use_tp:
        from tp import apply_tp
        apply_tp(model)

    model = model.to(device=device, dtype=precision)
    return model.eval()
