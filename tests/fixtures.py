import asyncio
import sys
from unittest.mock import AsyncMock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.router import router
from app.services import get_payload_service

test_app = FastAPI(debug=True, title="Test Caching Service")
test_app.include_router(router=router)


@pytest.fixture
def mock_service():
    return AsyncMock()


@pytest.fixture
def client(mock_service):
    test_app.dependency_overrides = dict()
    test_app.dependency_overrides[get_payload_service] = lambda: mock_service
    with TestClient(test_app) as c:
        yield c
    test_app.dependency_overrides.clear()


@pytest.fixture(scope="session", autouse=True)
def set_event_loop_policy():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
