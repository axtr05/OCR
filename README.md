# OCR

### Install Tesseract OCR Engine

Download Windows installer:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, note the path (usually):


### Verify installation:

```bash
tesseract --version
```

If the command fails:

Verify installation folder: C:\Program Files\Tesseract-OCR

Add this path to Environment Variables → Path

### Verify Python Installation

```bash
python --version
```

### Install Python Libraries

```bash
pip install pytesseract opencv-python pillow numpy
```

### Project Folder Structure
<<<<<<< HEAD
=======
```
>>>>>>> b7e9c9faeaae399165f40876c3f8631e08ac1af0
OCR_Project
├── ocr.py
├── sample.jpg
└── extracted_text.txt
```


Add a sample.jpg image inside the project folder.

### Run the Project


```bash
python ocr.py
```

<<<<<<< HEAD
you will see your output text in your terminal and a file extracted_text.txt will be created displaying the same text in your project directory
=======
you will see your output text in your terminal and a file extracted_text.txt will be created displaying the same text in your project directory
>>>>>>> b7e9c9faeaae399165f40876c3f8631e08ac1af0
