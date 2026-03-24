# OCR

### Install Tesseract OCR Engine

Download Windows installer:
https://github.com/UB-Mannheim/tesseract/wiki

After installation, note the path (usually):
C:\Program Files\Tesseract-OCR

---

### Verify Tesseract Installation

tesseract --version

If the command fails:
- Verify installation folder: C:\Program Files\Tesseract-OCR
- Add this path to Environment Variables → Path

---

### Install Poppler (Required for PDF Support)

Download Poppler for Windows:
https://github.com/oschwartz10612/poppler-windows/releases

Steps:
1. Download latest Release zip
2. Extract to:
   C:\poppler
3. Locate folder:
   C:\poppler\poppler-xx\Library\bin
4. Copy this path and update in ocr.py:

   POPPLER_PATH = r"C:\poppler\poppler-xx\Library\bin"

(Optional)
You can also add this path to Environment Variables → Path

---

### Verify Python Installation

python --version

---

### Install Python Libraries

pip install pytesseract opencv-python pillow numpy pdf2image

---

### Project Folder Structure

OCR_Project
├── ocr.py          (OCR processing logic)
├── app.py          (GUI application)
├── sample.jpg
├── sample.pdf      (optional)
└── extracted_text.txt

---

### Add Sample File

Add a sample image or PDF inside the project folder.

---

### Run CLI Version (Basic)

python ocr.py

- Enter file path when prompted
- Output will be printed in terminal
- extracted_text.txt will be created

---

### Run GUI Version (Recommended)

python app.py

Features:
- Upload image or PDF file
- Click "Process"
- View extracted text in UI
- Save output to file

---

### Supported File Types

- Images: .png, .jpg, .jpeg, .bmp
- PDFs: .pdf (requires Poppler)

---

### Notes

- For best OCR accuracy, use clear, high-resolution images
- PDFs are converted to images before OCR
- Layout may not be perfectly preserved for complex documents

---

### Troubleshooting

1. Tesseract not found:
   - Check installation path
   - Update pytesseract path in ocr.py

2. PDF not working:
   - Ensure Poppler is installed
   - Verify POPPLER_PATH is correct

3. GUI not opening:
   - Ensure Tkinter is installed
   - Run: python -m tkinter

---

### Output

- Text is displayed in terminal or GUI
