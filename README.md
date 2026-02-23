# AI Image Detector Platform

A beginner-friendly AI web app that lets you upload an image and get the model's best guess for what it represents.

## What this project does

- Upload an image from your computer.
- Runs a pretrained ResNet-50 image model.
- Shows the top predictions with confidence percentages.

---

## 1) Put this project on GitHub (if you cannot see it there yet)

If this folder is only local on your machine/container, you must push it to a GitHub repository.

### A. Create an empty repo on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name suggestion: `ai-image-detector`
3. Keep it **Public** or **Private** (your choice)
4. Click **Create repository**

### B. Connect local code to that repo and push

Run these commands from this project folder:

```bash
git init
git add .
git commit -m "Initial commit: AI image detector"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
git push -u origin main
```

Replace:
- `<YOUR_USERNAME>` with your GitHub username
- `<YOUR_REPO>` with your repo name

After this, refresh the repo page on GitHub and you will see your code.

> If `git remote add origin ...` says remote already exists, use:
>
> ```bash
> git remote set-url origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
> git push -u origin main
> ```

---

## 2) Run locally

### Requirements

- Python 3.10+
- `pip`

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Start the app

```bash
python -m uvicorn app:app --reload
```

Open your browser at:

- http://127.0.0.1:8000

Then upload an image and click **Analyze Image**.

---

## 3) Run tests

```bash
pytest
```

---

## 4) Common beginner issues

- **`uvicorn: command not found`**
  - Activate virtualenv first: `source .venv/bin/activate`
  - Or run with Python module style: `python -m uvicorn app:app --reload`

- **`No module named fastapi`**
  - You did not install dependencies yet:
    `pip install -r requirements.txt`

- **GitHub asks for password/token on push**
  - Use a Personal Access Token (PAT) instead of password.
  - Or use GitHub CLI: `gh auth login`

---

## Notes

- The first classification request may be slower because model weights may need to download.
- Large ML dependencies (`torch`, `torchvision`) can take a while to install.
