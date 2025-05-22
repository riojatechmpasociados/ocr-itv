from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.ocr_processor import extract_text_from_pdf

app = FastAPI()

# Permitir CORS (opcional para frontend web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr")
async def ocr_pdf(file: UploadFile = File(...)):
    content = await file.read()
    extracted = extract_text_from_pdf(content)
    return {"result": extracted}