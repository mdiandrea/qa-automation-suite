import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Make sure chromedriver is in PATH or specify full path

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.quit()  # Close the browser

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_in_python_org():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys("pycon")
    elem.submit()
    assert "No results found." not in driver.page_source
    driver.quit()

def test_downloads_link_exists():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
    assert downloads_link is not None
    driver.quit()
