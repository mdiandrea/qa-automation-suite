from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust if needed

service = Service(executable_path="C:\\WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
