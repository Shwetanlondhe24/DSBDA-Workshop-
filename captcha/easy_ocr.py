import easyocr

# Load the EasyOCR reader without progress bar
reader = easyocr.Reader(["en"], verbose=False)

# Run OCR
result = reader.readtext("captcha.png", detail=0)
captcha_text = "".join(result)

print("🔍 EasyOCR Extracted CAPTCHA:", captcha_text)
