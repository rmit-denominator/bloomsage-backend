from fastapi.testclient import TestClient
from main import app  # Updated import statement

client = TestClient(app)


def test_get_data() -> None:
    """
    Test getting data
    """
    response = client.get("/data")
    assert (
        response.status_code == 200
    ), f"Expected status code 200, but got {response.status_code}."

def test_upload_image():
    with open("test_image.jpg", "rb") as f:
        image_data = f.read()

    response = client.post("/upload/", files={"image": image_data})

    assert response.status_code == 200
    data = response.json()
    assert "species" in data
    assert "recommendations" in data

