# Selenium-Web-UI-Automation-Demo
# Selenium Python Demo Test
Test Descriptions
1. test_python_search.py::PythonOrgSearch::test_search_in_python_org
This test is implemented inside a unittest.TestCase class named PythonOrgSearch. It:

Opens the Chrome browser using Selenium WebDriver.

Navigates to the official Python website.

Verifies the page title contains "Python".

Finds the search input box (<input> element with name="q").

Types the search term "pycon" and submits the search.

Verifies the search results page does not contain the phrase "No results found." (meaning results were found).

Closes the browser.

This test validates that the search functionality on python.org works and returns results for valid queries.

2. test_python_search.py::test_search_in_python_org
This is a standalone test function (not in a class). It performs the same steps as the first test:

Opens Chrome.

Loads https://www.python.org.

Checks that the page title contains "Python".

Finds the search field.

Types "pycon" and submits.

Ensures "No results found." is not on the results page.

Closes the browser.

This function duplicates the first test's functionality but uses plain assertions outside of a unittest class.

3. test_python_search.py::test_downloads_link_exists
Another standalone test function that:

Opens Chrome.

Loads https://www.python.org.

Finds the "Downloads" link by its link text.

Asserts that the "Downloads" link exists (is not None).

Closes the browser.

This test verifies that a crucial navigation link ("Downloads") is present on the Python homepage.

Summary
Tests are defined in two styles: within a unittest.TestCase class and as standalone functions.

All tests open the browser, navigate to python.org, validate UI elements or page behavior, and close the browser.

All tests have passed successfully, confirming the tested pages and their elements behave as expected under Selenium WebDriver.

