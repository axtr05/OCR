# OCR Document System

### Install Tesseract OCR Engine

Download Windows installer:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, note the path (usually):


Verify installation:

```bash
tesseract --version

If the command fails:

Verify installation folder:

C:\Program Files\Tesseract-OCR

Add this path to Environment Variables → Path

Verify Python Installation

```bash
python --version

Install Python Libraries

```bash
pip install pytesseract opencv-python pillow numpy

Project Folder Structure
OCR_Project
│
├── ocr.py
├── sample.jpg
└── extracted_text.txt

### Run the Project

Add a sample.jpg image inside the project folder.

```bash
python ocr.py

you will see your output text in your terminal and a file extracted_text.txt will be created displaying the same text