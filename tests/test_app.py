from fastapi.testclient import TestClient

import app
from classifier import Prediction


class StubClassifier:
    def predict(self, image_bytes: bytes, top_k: int = 5):
        return [Prediction(label="tabby cat", confidence=0.91)]


def test_home_page_loads():
    client = TestClient(app.app)
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Image Detector" in response.text


def test_classify_rejects_non_image():
    client = TestClient(app.app)
    response = client.post(
        "/classify",
        files={"image": ("notes.txt", b"hello", "text/plain")},
    )
    assert response.status_code == 400
    assert "Please upload a valid image file." in response.text


def test_classify_displays_predictions(monkeypatch):
    app.get_classifier.cache_clear()
    monkeypatch.setattr(app, "get_classifier", lambda: StubClassifier())

    client = TestClient(app.app)
    response = client.post(
        "/classify",
        files={"image": ("photo.jpg", b"fakeimagedata", "image/jpeg")},
    )
    assert response.status_code == 200
    assert "tabby cat" in response.text
