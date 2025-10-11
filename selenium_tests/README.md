🧪 Selenium Login Test: test_login_flow.py
This test automates a login flow using Selenium WebDriver against the ExpandTesting demo site, designed for safe public automation. It verifies successful login using dummy credentials and checks for expected post-login behavior.

🔍 What It Does
Navigates to the login page

Inputs demo-safe username and password

Submits the form

Verifies login success by checking for a dashboard element or confirmation message

🛡️ Safety Notes
Uses dummy credentials and a public demo site

No real accounts, sensitive data, or production systems involved

Ideal for portfolio and interview demonstrations

🚀 How to Run
Make sure you have the required dependencies installed:

bash
pip install selenium
Then run the test:

bash
python selenium_tests/test_login_flow.py
⚙️ Requirements
Python 3.x

Chrome browser

ChromeDriver installed and added to PATH

📁 File Location
Code
qa-automation-suite/
├── selenium_tests/
│   └── test_login_flow.py
