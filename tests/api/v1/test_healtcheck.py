from fastapi import status
from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient) -> None:
    response = client.get("/v1/healthcheck/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
