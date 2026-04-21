from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_coinspot.feeds.live_coinspot.request_base import CoinSpotRequestData


@pytest.mark.asyncio
async def test_coinspot_async_request_allows_missing_extra_data(monkeypatch) -> None:
    request_data = CoinSpotRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="COINSPOT___SPOT",
    )

    async_request_mock = AsyncMock(return_value={"status": "ok", "prices": {}})
    monkeypatch.setattr(request_data, "async_http_request", async_request_mock)

    result = await request_data.async_request("GET /pubapi/v2/latest")

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == {"status": "ok", "prices": {}}
