# External
from dotenv import dotenv_values
from fastapi.testclient import TestClient

# Project
from app.main import app


# Load environment variables from .env file
config = dotenv_values(".env")

client = TestClient(app, headers={"Authorization": f"Bearer {config["SECRET_TOKEN"]}"})
