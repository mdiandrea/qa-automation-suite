import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_flow():
    # Explicitly set paths to avoid Selenium Manager issues
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    driver_path = "C:\\WebDrivers\\chromedriver.exe"

    options = Options()
    options.binary_location = chrome_path

    service = Service("C:/Users/skiny/Documents/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://practice.expandtesting.com/login")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys("practice")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        try:
            login_button.click()
        except:
            driver.execute_script("arguments[0].click();", login_button)

        time.sleep(3)
        assert "Secure Area" in driver.page_source

    finally:
        driver.quit()
