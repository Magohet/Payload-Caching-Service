from uuid import UUID

from fixtures import mock_service, client


def test_healthcheck(client):
    response = client.get("/api/payload/healthcheck")
    assert response.status_code == 200


def test_get_payload(client, mock_service):
    payload_id = UUID("1dbc5a57-a630-4b00-b7c4-5e96be346b95")
    response_data = {
        "id": "1dbc5a57-a630-4b00-b7c4-5e96be346b95",
        "list_1": [
            "1",
            "2"
        ],
        "list_2": [
            "3",
            "4"
        ],
        "result": "['1', '3', '2', '4']",
        "created_at": "2025-08-20T18:37:41.615994Z",
        "updated_at": None
    }

    mock_service.get_payload_by_id.return_value = response_data

    response = client.get(f"/api/payload/{payload_id}")
    assert response.status_code == 200
    assert response.json() == response_data
    mock_service.get_payload_by_id.assert_awaited_once_with(payload_id)


def test_create_payload(client, mock_service):
    request_data = {
        "list_1": ["1", "2"],
        "list_2": ["3", "4"]
    }

    response_data = {
        "id": "1dbc5a57-a630-4b00-b7c4-5e96be346b95",
        "result": "['1', '3', '2', '4']"
    }

    mock_service.create_payload.return_value = response_data

    response = client.post("/api/payload/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data
    mock_service.create_payload.assert_awaited_once()
