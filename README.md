# Selenium-Web-UI-Automation-Demo
# Selenium Python Demo Test
This repository includes a simple Selenium test written in Python that automates a search on python.org.

Test Description
Opens Chrome browser

Navigates to https://www.python.org

Verifies the page title contains "Python"

Types "pycon" in the search box and submits

Checks that the search results page does not contain "No results found."

Closes the browser

Running the Test
Make sure you have the dependencies installed:

python -m pip install selenium
Run the test from the command line:

cd C:\Users\skiny\Documents\selenium
python test_python_search.py
You will see Chrome open and the test perform the search automatically. The test will output the results and close the browser when finished.

Optional: Running Tests with pytest
You can also run tests using pytest:

Install pytest:

python -m pip install pytest
Rename your test file with test_ prefix, for example test_search.py

Run pytest inside the test folder:

pytest
This will run all test cases and provide a detailed report.
