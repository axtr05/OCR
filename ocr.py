import cv2
import pytesseract
import numpy as np
import os
from pdf2image import convert_from_path

# 🔴 SET PATHS CORRECTLY
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-25.12.0\Library\bin"   # ✅ FIXED


def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh


def extract_text_with_layout(image):
    processed = process_image(image)

    return pytesseract.image_to_string(
        processed,
        config="--oem 3 --psm 4 preserve_interword_spaces=1"
    )


def handle_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    # 🟢 IMAGE FILES
    if ext in [".png", ".jpg", ".jpeg", ".bmp"]:
        image = cv2.imread(file_path)
        if image is None:
            return "Error: Image not loaded"

        return extract_text_with_layout(image)

    # 🔵 PDF FILES
    elif ext == ".pdf":
        try:
            pages = convert_from_path(
                file_path,
                poppler_path=POPPLER_PATH
            )
        except Exception as e:
            return f"PDF Error: {str(e)}"

        all_text = ""
        for page in pages:
            img = np.array(page)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            all_text += extract_text_with_layout(img) + "\n"

        return all_text.strip()

    else:
        return f"Unsupported file type: {ext}"


# ✅ CLI MODE
if __name__ == "__main__":
    file_path = input("Enter file path: ")
    text = handle_file(file_path)

    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("----- Extracted Text -----")
    print(text)