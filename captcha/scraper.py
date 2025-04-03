from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def find_captcha_element(driver):
    """Find CAPTCHA element using multiple strategies"""
    locators = [
        (By.ID, "form_rcdl:j_idt33:j_idt40"),  # Current ID
        (By.ID, "form_rcdl:j_idt33:j_idt38"),  # Old ID
        (By.XPATH, "//img[contains(@id, 'captcha') or contains(@id, 'idt')]"),  # Partial match
        (By.CSS_SELECTOR, "img[src*='captcha']"),  # Image with "captcha" in src
        (By.XPATH, "//div[contains(@class, 'captcha')]/img"),  # Image in captcha div
        (By.XPATH, "//form[@id='form_rcdl']//img[not(@class)]")  # Any image without class in form
    ]
    
    for by, value in locators:
        try:
            return WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((by, value))
            )
        except:
            continue
    
    raise Exception("CAPTCHA element not found with any locator strategy")

# Set up WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open website
url = "https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
driver.get(url)

# Wait for page to load
time.sleep(3)

# Find CAPTCHA using robust strategy
try:
    captcha_element = find_captcha_element(driver)
    captcha_element.screenshot("captcha.png")
    print("✅ CAPTCHA screenshot saved as 'captcha.png'")

except Exception as e:
    print(f"❌ CAPTCHA not found: {e}")

# Close browser
driver.quit()