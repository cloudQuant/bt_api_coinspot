from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.tickers.ticker import TickerData
from bt_api_base.functions.utils import from_dict_get_float


class CoinSpotTickerData(TickerData):
    def __init__(
        self,
        ticker_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(ticker_info, has_been_json_encoded)
        self.exchange_name = "COINSPOT"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.ticker_data: dict[str, Any] | None = (
            ticker_info if has_been_json_encoded and isinstance(ticker_info, dict) else None
        )
        self.ticker_symbol_name: str | None = symbol_name
        self.server_time: float | None = None
        self.last_price: float | None = None
        self.bid_price: float | None = None
        self.ask_price: float | None = None
        self.bid_volume: float | None = None
        self.ask_volume: float | None = None
        self.last_volume: float | None = None
        self.has_been_init_data = False

    def init_data(self) -> "CoinSpotTickerData":
        if not self.has_been_json_encoded:
            if isinstance(self.ticker_info, str):
                self.ticker_data = json.loads(self.ticker_info)
            else:
                self.ticker_data = {}
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        ticker = self.ticker_data or {}
        data = ticker
        if isinstance(ticker, dict) and ticker.get("status") == "ok":
            prices = ticker.get("prices", {})
            if isinstance(prices, dict) and self.symbol_name in prices:
                data = prices.get(self.symbol_name, {})
            else:
                data = prices

        if isinstance(data, dict):
            self.last_price = from_dict_get_float(data, "last")
            self.bid_price = from_dict_get_float(data, "bid")
            self.ask_price = from_dict_get_float(data, "ask")

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if not self.ticker_data:
            raise NotImplementedError
        self.init_data()
        return {
            "exchange_name": self.exchange_name,
            "symbol_name": self.symbol_name,
            "asset_type": self.asset_type,
            "ticker_symbol_name": self.ticker_symbol_name,
            "server_time": self.server_time,
            "bid_price": self.bid_price,
            "ask_price": self.ask_price,
            "bid_volume": self.bid_volume,
            "ask_volume": self.ask_volume,
            "last_price": self.last_price,
            "last_volume": self.last_volume,
            "local_update_time": self.local_update_time,
        }

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_local_update_time(self) -> float:
        return self.local_update_time

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_ticker_symbol_name(self) -> str | None:
        return self.ticker_symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_server_time(self) -> float | None:
        return self.server_time

    def get_bid_price(self) -> float | None:
        self.init_data()
        return self.bid_price

    def get_ask_price(self) -> float | None:
        self.init_data()
        return self.ask_price

    def get_bid_volume(self) -> float | None:
        return self.bid_volume

    def get_ask_volume(self) -> float | None:
        return self.ask_volume

    def get_last_price(self) -> float | None:
        self.init_data()
        return self.last_price

    def get_last_volume(self) -> float | None:
        return self.last_volume


class CoinSpotRequestTickerData(CoinSpotTickerData):
    pass


class CoinSpotWssTickerData(CoinSpotTickerData):
    pass


__all__ = ["CoinSpotRequestTickerData", "CoinSpotTickerData"]
