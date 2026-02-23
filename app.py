from __future__ import annotations

from functools import lru_cache

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from classifier import ImageClassifier

app = FastAPI(title="Image Understanding Platform")
templates = Jinja2Templates(directory="templates")


@lru_cache(maxsize=1)
def get_classifier() -> ImageClassifier:
    return ImageClassifier()


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "predictions": None, "filename": None, "error": None},
    )


@app.post("/classify", response_class=HTMLResponse)
async def classify(request: Request, image: UploadFile = File(...)) -> HTMLResponse:
    if not image.content_type or not image.content_type.startswith("image/"):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "predictions": None,
                "filename": None,
                "error": "Please upload a valid image file.",
            },
            status_code=400,
        )

    image_bytes = await image.read()
    predictions = get_classifier().predict(image_bytes=image_bytes, top_k=5)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "predictions": predictions,
            "filename": image.filename,
            "error": None,
        },
    )
