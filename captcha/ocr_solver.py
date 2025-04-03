import pytesseract
import cv2
import numpy as np

# Update with your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the CAPTCHA image
image = cv2.imread("captcha.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Increase contrast
gray = cv2.equalizeHist(gray)

# Apply Gaussian blur to reduce noise
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# Adaptive thresholding to binarize the image
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 2
)

# Dilation to separate characters
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
binary = cv2.dilate(binary, kernel, iterations=1)

# Save the processed image for debugging
cv2.imwrite("processed_captcha.png", binary)

# Extract text using Tesseract
custom_config = r"--psm 7 --oem 3 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
captcha_text = pytesseract.image_to_string(binary, config=custom_config)

# Clean the extracted text
captcha_text = captcha_text.strip()

# Debugging output
print("🔍 Extracted CAPTCHA:", repr(captcha_text))
