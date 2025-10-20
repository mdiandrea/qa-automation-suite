from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_flow():
    # Initialize ChromeDriver with WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://practice.expandtesting.com/login")

    # Wait for username field to be present and enter username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Scroll and wait for login button to be clickable, then click it
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    try:
        login_button.click()
    except:
        # Fallback click via JavaScript if intercepted
        driver.execute_script("arguments[0].click();", login_button)

    # Optional: wait and validate login success
    time.sleep(3)
    assert "Secure Area" in driver.page_source

    driver.quit()
