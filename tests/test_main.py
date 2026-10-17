from app.main import app


def test_home_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "Homelab Status"
    assert response.json["status"] == "running"


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert "timestamp" in response.json
