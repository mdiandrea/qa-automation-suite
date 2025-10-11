import requests

def test_invalid_api_request():
    url = "https://jsonplaceholder.typicode.com/posts/999999"  # unlikely to exist
    response = requests.get(url)

    assert response.status_code == 404 or response.json() == {}, "Expected 404 or empty response"