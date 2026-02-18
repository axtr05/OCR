import cv2
import pytesseract
import numpy as np

# Path to tesseract executable (change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read input image
image = cv2.imread("sample.jpg")

# Check if image loaded
if image is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Remove noise using Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding
_, thresh = cv2.threshold(
    blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Extract text using OCR
text = pytesseract.image_to_string(thresh, lang="eng")

# Post-processing
clean_text = text.replace("\n", " ").strip()

# Save output to file
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)

# Display results
print("----- Extracted Text -----")
print(clean_text)

# Show images (optional for demo)
cv2.imshow("Original Image", image)
cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
x