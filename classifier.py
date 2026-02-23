from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from typing import List


@dataclass
class Prediction:
    label: str
    confidence: float


class ImageClassifier:
    def __init__(self) -> None:
        import torch
        from torchvision.models import ResNet50_Weights, resnet50

        self.torch = torch
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval()
        self.preprocess = self.weights.transforms()
        self.labels = self.weights.meta["categories"]

    def predict(self, image_bytes: bytes, top_k: int = 5) -> List[Prediction]:
        from PIL import Image

        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        tensor = self.preprocess(image).unsqueeze(0)

        with self.torch.inference_mode():
            outputs = self.model(tensor)
            probabilities = self.torch.nn.functional.softmax(outputs[0], dim=0)
            scores, indices = self.torch.topk(probabilities, k=top_k)

        return [
            Prediction(label=self.labels[idx], confidence=float(score))
            for score, idx in zip(scores, indices)
        ]
