from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # Disable Chrome password manager and leak detection
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Path to your ChromeDriver
    service = Service("C:/Users/mdian/qa-automation-suite/drivers/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://practice.expandtesting.com/login")
        print("Navigated to login page")

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        print("Username field found")

        driver.find_element(By.ID, "username").send_keys("practice")
        print("Entered username")

        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        print("Entered password")

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", login_button)
        print("Login button clicked")

        WebDriverWait(driver, 30).until(
            lambda d: "You logged into a secure area!" in d.page_source
        )
        print("Login successful")

    except Exception as e:
        print(f"Test failed with error: {e}")
        raise

    finally:
        print("Closing browser...")
        driver.quit()
