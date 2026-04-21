"""Tests for CoinspotExchangeData container."""

from __future__ import annotations

from bt_api_coinspot.exchange_data import CoinSpotExchangeData


class TestCoinSpotExchangeData:
    """Tests for CoinSpotExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = CoinSpotExchangeData()

        assert exchange.exchange_name == "COINSPOT___SPOT"
