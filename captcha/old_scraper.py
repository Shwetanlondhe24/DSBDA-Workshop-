from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open website
url = "https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
driver.get(url)

# Wait for CAPTCHA to load (adjust time if needed)
try:
    captcha_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "form_rcdl:j_idt33:j_idt40"))
    )
    captcha_element.screenshot("captcha.png")
    print("✅ CAPTCHA screenshot saved as 'captcha.png'")

except Exception as e:
    print("❌ CAPTCHA not found:", e)

# Close browser
driver.quit()

# form_rcdl:j_idt33:j_idt38 - old id
#id="form_rcdl:j_idt33:j_idt40"