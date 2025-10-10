
# 🧪 Selenium Web UI Automation Demo

This project showcases automated UI testing using **Selenium WebDriver** and **Pytest** in Python. It validates core functionality and UI elements on [python.org](https://www.python.org), using both `unittest.TestCase` and standalone test functions.

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/mdiandrea/Selenium-Web-UI-Automation-Demo.git
cd Selenium-Web-UI-Automation-Demo
Install dependencies
bash
pip install -r requirements.txt
Run tests
bash
pytest
Generate an HTML report
bash
pytest --html=report.html
✅ Test Descriptions
PythonOrgSearch::test_search_in_python_org
Uses unittest.TestCase class

Opens Chrome and navigates to python.org

Verifies the page title contains "Python"

Searches for "pycon" and verifies that search results are displayed

test_search_in_python_org
Standalone function version of the above test

Performs the same steps using plain assert statements

test_downloads_link_exists
Opens Chrome and loads python.org

Locates the "Downloads" link by its text

Asserts that the link exists
