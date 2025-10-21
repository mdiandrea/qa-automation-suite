# 🧪 QA Automation Suite – Selenium, Cypress, API, and SQL Testing

Welcome to my end-to-end QA automation suite! This project demonstrates robust testing across web UI, REST APIs, and SQL queries using both Python and JavaScript frameworks.

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
├── api_tests/                  # Python API tests
├── sql_tests/                  # SQL query tests
├── python_org_tests/           # UI tests for python.org
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

## 🧪 Sample Output

### ✅ Selenium Test
```
test_login_with_valid_credentials (test_login.TestLogin) ...
Waiting for username field...
Sending credentials...
✅ Login test passed.
ok
```

### ✅ Cypress Test
```
Public API Test
√ Fetches a random user and checks response structure (397ms)

Cypress Docs Smoke Test
√ Loads the homepage and checks key elements (3449ms)
```

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



