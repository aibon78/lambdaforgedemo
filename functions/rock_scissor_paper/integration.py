import pytest
import requests
from lambda_forge.constants import BASE_URL

@pytest.mark.integration(method="GET", endpoint="/rock-scissor-paper")
def test_rock-scissor-paper_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/rock-scissor-paper")

    assert response.status_code == 200 
