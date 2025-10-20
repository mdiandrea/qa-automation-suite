from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_flow():
    # Selenium Manager automatically manages the ChromeDriver
    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")

    # Wait until username input is present and input credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Scroll into view and click login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    try:
        login_button.click()
    except:
        driver.execute_script("arguments[0].click();", login_button)

    # Wait to verify page contains 'Secure Area'
    time.sleep(3)
    assert "Secure Area" in driver.page_source

    driver.quit()
