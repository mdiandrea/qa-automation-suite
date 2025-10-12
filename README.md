# 🧪 Selenium Test Suite – Functional, API, and SQL Automation

Welcome to my end-to-end QA automation suite! This project demonstrates robust testing across web UI, REST APIs, and SQL queries using Python’s `unittest` framework and Selenium WebDriver.

---

## 📌 Features

- ✅ Functional UI Testing with Selenium (ChromeDriver)
- ✅ API Testing using `requests`
- ✅ SQL Query Validation with SQLite
- ✅ Modular Test Runner for multi-folder discovery
- ✅ Cross-domain coverage: login flows, search functionality, API status, and DB logic
- ✅ Screenshot capture on failure
- ✅ Clear console logging for test progress and debugging

---

🗂️ **Project Structure**

C:\Users\skiny\Documents\selenium
```
├── run_tests.py                     # Unified test runner
```
 ```
├── selenium_tests\
 │   └── test_login.py # Valid login test using Selenium
```
 ```
├── api_tests\
 │   └── test_example_api.py         # Sample API status check
```
 ```
├── sql_tests\
 │   └── test_sql_sample.py           # Dummy SQL query test
```
 ```
├── python_org_tests\
 │   └── test_python_search.py       # UI tests for python.org
```
```
├── screenshots\                    # Captured on test failure
```




## 🚀 Getting Started

 1. Clone the Repo

git clone https://github.com/your-username/selenium-test-suite.git
cd selenium-test-suite

2. Install Dependencies
pip install -r requirements.txt

3. Run All Tests
python run_tests.py

4. Run a Specific Test
python selenium_tests/test_login.py


## 🧪 **Sample Output**
```
test_login_with_valid_credentials (test_login.TestLogin) ...
Waiting for username field...
Sending credentials...
Waiting for success message...
✅ Login test passed.
ok

----------------------------------------------------------------------
Ran 5 tests in 8.965s

OK
```


📸 Screenshots
Screenshots are automatically saved to the screenshots/ folder on test failure for easy debugging.



🧠 **Tech Stack**

Python 3.10+

Selenium WebDriver

unittest

requests

SQL

💡 Future Enhancements
[ ] Add negative login test cases

[ ] Integrate with GitHub Actions for CI

[ ] Generate HTML reports with pytest-html

[ ] Add test data parameterization
