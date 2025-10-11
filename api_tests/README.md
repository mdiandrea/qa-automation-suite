🌐 API Test Suite
This module validates RESTful API endpoints using Python’s requests library and pytest. It simulates real-world backend QA workflows to ensure endpoint reliability, error handling, and data integrity.

📂 Folder Structure
Code
api_tests/
├── test_status_endpoint.py       # Basic status check for a valid endpoint
└── test_invalid_endpoint.py      # Error handling check for invalid input
🚀 How It Works
Sends GET requests to public API endpoints

Verifies HTTP status codes and response structure

Includes both success and failure scenarios

Uses pytest for test execution and reporting

✅ Sample Tests
Valid Endpoint Test

python
def test_api_status():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200
    assert "userId" in response.json()
Invalid Endpoint Test

python
def test_invalid_api_request():
    url = "https://jsonplaceholder.typicode.com/posts/999999"
    response = requests.get(url)

    assert response.status_code == 404 or response.json() == {}, "Expected 404 or empty response"
📊 Output Example
Code
api_tests/test_status_endpoint.py . [100%]
api_tests/test_invalid_endpoint.py . [100%]
2 passed in 1.61s
🧰 Requirements
Install dependencies:

bash
pip install requests pytest
Run tests:

bash
pytest api_tests/
🔧 Future Enhancements
Add token-based authentication and header validation

Parametrize tests for multiple endpoints and edge cases

Validate JSON schema using jsonschema

Log results to reports/api_report.txt

Integrate with CI/CD pipelines for automated regression
