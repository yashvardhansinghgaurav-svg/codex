# AI Image Detector Platform

A simple AI platform that detects what an uploaded image represents using a pretrained ResNet-50 classifier from `torchvision`.

## Features

- Web UI for image upload.
- Top-5 class predictions with confidence percentages.
- FastAPI backend and Jinja template frontend.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000` and upload an image.

## Test

```bash
pytest
```

## Notes

- The first classification request may take longer while model weights are loaded/downloaded.
