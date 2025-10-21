import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginFlowTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-features=PasswordCheck")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        # Optional: use a fresh profile to avoid reused credentials
        # options.add_argument("--user-data-dir=C:\\Temp\\ChromeProfile")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://practice.expandtesting.com/login")

    def test_login_flow(self):
        driver = self.driver

        # Wait for username field and enter credentials
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("practice")

        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Scroll to login button and click via JavaScript to bypass overlays
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
        driver.execute_script("arguments[0].click();", login_button)

        # Wait for redirect and success message
        WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
        flash = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )

        self.assertIn("You logged into a secure area!", flash.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
