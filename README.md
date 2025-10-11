🧪 QA Automation Suite
Welcome to the QA Automation Suite, a modular testing framework designed to showcase manual and automated testing across web UI, backend SQL, and RESTful APIs. This project reflects real-world QA workflows and highlights precision, structure, and strategy in software testing.

📁 Folder Overview
Folder	Description
selenium_tests/	Automated UI tests using Selenium WebDriver
sql_tests/	SQL scripts and Python-based validations for backend data integrity
api_tests/	RESTful API tests using Python and requests
reports/	HTML and log-based test execution reports
screenshots/	Captured screenshots from Selenium runs, especially on failure
🛠 Tech Stack
Python 3.x

Selenium WebDriver

Pytest

Requests

Pure SQL (engine-agnostic)

Standard libraries for reporting and file I/O

🚀 Getting Started
Clone the repository

bash
git clone https://github.com/mdiandrea/qa-automation-suite.git
cd qa-automation-suite
Install dependencies

bash
pip install -r requirements.txt
Run Selenium tests

bash
pytest selenium_tests/
Run API tests

bash
pytest api_tests/
Run SQL validations

bash
python sql_tests/test_queries.py
🎯 Purpose
This suite was built to demonstrate:

End-to-end test coverage across UI, backend, and services

Clean folder structure and modular test design

Real-world QA workflows including reporting and debugging

Engine-agnostic SQL testing for flexible backend validation