def test_get_activities_returns_activity_map(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert "Chess Club" in body
    assert "participants" in body["Chess Club"]
    assert isinstance(body["Chess Club"]["participants"], list)
