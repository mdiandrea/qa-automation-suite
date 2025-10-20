from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_login_flow():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # ✅ Explicit path to chromedriver.exe
    service = Service("C:/Users/mdian/qa-automation-suite/drivers/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://jobright.ai/?login=true")

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login")

    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    login_button.click()

    assert "Dashboard" in driver.title or "Welcome" in driver.page_source
    driver.quit()
