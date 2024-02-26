# # External
# from fastapi import status
# from fastapi.testclient import TestClient

# # Project
# from app.main import app


# client = TestClient(app)


# # region laps

# # region laps - good inputs


# def test_get_laps():
#     response = client.get("/laps/2023/5")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == []


# def test_get_laps_with_session_only():
#     response = client.get("/laps/2023/5?session=4")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == []


# def test_get_laps_with_driver_numbers_only():
#     response = client.get("/laps/2023/5?driver_numbers=1,44")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == []


# def test_get_laps_with_session_and_driver_numbers():
#     response = client.get("/laps/2023/5?session=4?driver_numbers=1,44")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == []


# # endregion laps - good inputs

# # region laps - bad inputs


# def test_get_laps_bad_driver_numbers():
#     response = client.get("/laps/2023/5?driver_numbers=0,1,13,44,83")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == []


# # endregion laps - bad inputs

# # endregion laps
