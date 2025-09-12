import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize Chrome driver; ensure chromedriver is in PATH
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_search_in_python_org(self):
        """
        Test the search functionality on python.org by searching for 'pycon'
        and verify results are returned.
        """
        driver = self.driver
        wait = self.wait
        driver.get("https://www.python.org")

        # Wait for the title to contain "Python"
        wait.until(EC.title_contains("Python"))
        self.assertIn("Python", driver.title)

        # Wait for the search box and enter query
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys("pycon")
        search_box.send_keys(Keys.RETURN)

        # Wait for results page to load and verify no "No results found."
        wait.until(EC.presence_of_element_located((By.ID, "content")))
        self.assertNotIn("No results found.", driver.page_source)

    def test_downloads_link_exists(self):
        """Verify that the 'Downloads' link is present on the python.org homepage"""
        driver = self.driver
        wait = self.wait
        driver.get("https://www.python.org")

        downloads_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Downloads")))
        self.assertIsNotNone(downloads_link)

    @classmethod
    def tearDownClass(cls):
        # Close the browser once all tests complete
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

