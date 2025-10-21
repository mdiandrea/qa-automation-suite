# 🧪 QA Automation Suite – Selenium, Cypress, API, and SQL Testing

Welcome to my end-to-end QA automation suite! This project demonstrates robust testing across web UI, REST APIs, and SQL queries using both Python and JavaScript frameworks. It’s designed for scalability, clarity, and cross-domain coverage—from browser automation to backend validation.

---

## 📌 Features

✅ Functional UI Testing with Selenium (Python)  
✅ UI and API Testing with Cypress (JavaScript)  
✅ REST API Validation using `requests`  
✅ SQL Query Testing with SQLite  
✅ Modular Test Runner for Python tests  
✅ Screenshot capture on failure (Python + Cypress)  
✅ Clear console logging for debugging  
✅ Cross-domain coverage: login flows, search functionality, API status, and DB logic

---

## 🗂️ Project Structure

```
qa-automation-suite/
├── run_tests.py                 # Unified Python test runner
├── selenium_tests/             # Selenium UI tests
│   └── test_login.py           # Valid login flow
├── python_org_tests/           # UI tests for python.org
│   └── test_python_search.py   # Search functionality test
├── api_tests/                  # Python API tests
│   └── test_example_api.py     # Sample API status check
├── sql_tests/                  # SQL query tests
│   └── test_sql_sample.py      # Dummy SQLite query test
├── cypress/
│   ├── e2e/
│   │   ├── sample-ui.cy.js     # Cypress UI test for docs.cypress.io
│   │   └── sample-api.cy.js    # Cypress API test for randomuser.me
│   ├── screenshots/            # Cypress screenshots on failure
│   └── cypress.config.js       # Cypress configuration
├── screenshots/                # Python screenshots on failure
├── assets/, drivers/, reports/ # Supporting files
```

---

## 🚀 Getting Started

### 🔧 Python Setup
```bash
pip install -r requirements.txt
python run_tests.py
```

Run a specific test:
```bash
python selenium_tests/test_login.py
```

### 🔧 Cypress Setup
```bash
npm install
npx cypress run         # Headless mode
npx cypress open        # GUI mode
```

---

## 🧪 Test Breakdown

### ✅ Selenium UI Tests
- `test_login.py`: Validates login flow using Selenium WebDriver and ChromeDriver  
- `test_python_search.py`: Automates a search on python.org and verifies results

### ✅ Python API Test
- `test_example_api.py`: Sends GET request to a sample REST endpoint and asserts status code and response structure

### ✅ SQL Test
- `test_sql_sample.py`: Executes a dummy SQL query using SQLite and validates result structure

### ✅ Cypress Tests
- `sample-ui.cy.js`: Loads docs.cypress.io and verifies presence of `nav`, `main`, and `footer` elements  
- `sample-api.cy.js`: Sends GET request to randomuser.me and asserts that the response contains a `results` array with one user

---

## 📸 Screenshots

- Python failures: saved to `screenshots/`  
- Cypress failures: saved to `cypress/screenshots/`

---

## 🧠 Tech Stack

- **Python 3.10+**: Selenium, unittest, requests, SQLite  
- **JavaScript (Node.js)**: Cypress

---

## 💡 Future Enhancements

- [ ] Add negative login test cases  
- [ ] Integrate GitHub Actions for CI  
- [ ] Generate HTML reports with `pytest-html`  
- [ ] Add test data parameterization  
- [ ] Expand Cypress coverage to include form validation and error handling

---


