from fastapi import FastAPI, UploadFile
from typing import Optional
from PIL import Image
import pytesseract

ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = FastAPI()

@app.get("/")
def read_root():
    return {"Proyecto": "ImagenesToText"}

@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    try:
        img = Image.open(file.file)
        text = pytesseract.image_to_string(img, "spa")
    except Exception as e:
        return {"text": "NO_VALID_IMAGE"}

    return {"text": text}
