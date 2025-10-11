🌐 API Test Suite
This module validates RESTful API endpoints using Python’s requests library and pytest. It’s built to simulate real-world backend QA workflows and ensure endpoint reliability, response structure, and data integrity.

📂 Folder Structure
Code
api_tests/
└── test_status_endpoint.py     # Basic status check for a public API
🚀 How It Works
Sends a GET request to a sample endpoint

Verifies the HTTP status code

Confirms expected keys exist in the JSON response

Uses pytest for test execution and reporting

✅ Sample Test
python
import requests

def test_api_status():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200
    assert "userId" in response.json()
📊 Output Example
Code
api_tests/test_status_endpoint.py . [100%]
1 passed in 0.96s
🧰 Requirements
Install dependencies with:

bash
pip install requests pytest
Run tests using:

bash
pytest api_tests/
🔧 Future Enhancements
Add token-based authentication and header validation

Parametrize tests for multiple endpoints

Validate JSON schema using jsonschema

Log results to reports/api_report.txt

Integrate with CI/CD pipelines for automated regression
