from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orderbooks.orderbook import OrderBookData


class CoinSpotOrderBookData(OrderBookData):
    def __init__(
        self,
        orderbook_info: Any,
        symbol_name: str | None = None,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(orderbook_info, has_been_json_encoded)
        self.exchange_name = "COINSPOT"
        self.symbol_name = symbol_name
        self.order_book_data: Any = orderbook_info if has_been_json_encoded else None
        self.asset_type = "SPOT"
        self.local_update_time = time.time()
        self.server_time: float | None = None
        self.order_book_symbol_name: str | None = symbol_name
        self.bid_price_list: list[float] | None = None
        self.ask_price_list: list[float] | None = None
        self.bid_volume_list: list[float] | None = None
        self.ask_volume_list: list[float] | None = None
        self.bid_trade_nums: list[int] | None = None
        self.ask_trade_nums: list[int] | None = None
        self.all_data: dict[str, Any] | None = None
        self.has_been_init_data = False

    def init_data(self) -> "CoinSpotOrderBookData":
        if not self.has_been_json_encoded:
            self.order_book_data = (
                json.loads(self.order_book_info) if isinstance(self.order_book_info, str) else {}
            )
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        if isinstance(self.order_book_data, dict):
            bids_raw = self.order_book_data.get("buyorders", [])
            asks_raw = self.order_book_data.get("sellorders", [])
            self.bid_price_list = [float(item.get("price", 0.0)) for item in bids_raw]
            self.ask_price_list = [float(item.get("price", 0.0)) for item in asks_raw]
            self.bid_volume_list = [float(item.get("amount", 0.0)) for item in bids_raw]
            self.ask_volume_list = [float(item.get("amount", 0.0)) for item in asks_raw]
            self.bid_trade_nums = [0 for _ in bids_raw]
            self.ask_trade_nums = [0 for _ in asks_raw]

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "asset_type": self.asset_type,
                "order_book_symbol_name": self.order_book_symbol_name,
                "server_time": self.server_time,
                "bid_price_list": self.bid_price_list,
                "ask_price_list": self.ask_price_list,
                "bid_volume_list": self.bid_volume_list,
                "ask_volume_list": self.ask_volume_list,
                "bid_trade_nums": self.bid_trade_nums,
                "ask_trade_nums": self.ask_trade_nums,
                "local_update_time": self.local_update_time,
            }
        return self.all_data

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name or ""

    def get_local_update_time(self) -> float | None:
        return self.local_update_time

    def get_symbol_name(self) -> str | None:
        return self.symbol_name

    def get_asset_type(self) -> str | None:
        return self.asset_type

    def get_server_time(self) -> float | None:
        return self.server_time

    def get_bid_price_list(self) -> list[float] | None:
        self.init_data()
        return self.bid_price_list

    def get_ask_price_list(self) -> list[float] | None:
        self.init_data()
        return self.ask_price_list

    def get_bid_volume_list(self) -> list[float] | None:
        self.init_data()
        return self.bid_volume_list

    def get_ask_volume_list(self) -> list[float] | None:
        self.init_data()
        return self.ask_volume_list

    def get_bid_trade_nums(self) -> list[int] | None:
        self.init_data()
        return self.bid_trade_nums

    def get_ask_trade_nums(self) -> list[int] | None:
        self.init_data()
        return self.ask_trade_nums


class CoinSpotRequestOrderBookData(CoinSpotOrderBookData):
    pass


class CoinSpotWssOrderBookData(CoinSpotOrderBookData):
    pass
