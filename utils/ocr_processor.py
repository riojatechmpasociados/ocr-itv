import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    extracted_text = []

    for page_num in range(len(doc)):
        pix = doc[page_num].get_pixmap(dpi=300)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        text = pytesseract.image_to_string(image, lang='spa')
        extracted_text.append({
            "page": page_num + 1,
            "text": text
        })

    return extracted_text