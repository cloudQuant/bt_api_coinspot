from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.bars.bar import BarData


class CoinSpotBarData(BarData):
    def __init__(
        self,
        bar_info: Any,
        symbol_name: str | None = None,
        period: str | None = None,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(bar_info, has_been_json_encoded)
        self.exchange_name = "COINSPOT"
        self.symbol_name = symbol_name
        self.period = period
        self.bar_data: Any = bar_info if has_been_json_encoded else None
        self.open_time: int | None = None
        self.open_price: float | None = None
        self.high_price: float | None = None
        self.low_price: float | None = None
        self.close_price: float | None = None
        self.volume: float | None = None
        self.server_time: float | int | None = None
        self.asset_type = "SPOT"
        self.all_data: dict[str, Any] | None = None
        self.local_update_time = time.time()
        self.has_been_init_data = False

    def init_data(self) -> "CoinSpotBarData":
        if not self.has_been_json_encoded:
            self.bar_data = json.loads(self.bar_info) if isinstance(self.bar_info, str) else []
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        if isinstance(self.bar_data, list) and len(self.bar_data) >= 5:
            self.open_time = int(float(self.bar_data[0])) * 1000
            self.open_price = float(self.bar_data[1])
            self.high_price = float(self.bar_data[2])
            self.low_price = float(self.bar_data[3])
            self.close_price = float(self.bar_data[4])
            if len(self.bar_data) > 5:
                self.volume = float(self.bar_data[5])

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "period": self.period,
                "open_time": self.open_time,
                "open_price": self.open_price,
                "high_price": self.high_price,
                "low_price": self.low_price,
                "close_price": self.close_price,
                "volume": self.volume,
                "local_update_time": self.local_update_time,
            }
        return self.all_data

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name or ""

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_server_time(self) -> float | int | None:
        return self.server_time

    def get_local_update_time(self) -> float | int | None:
        return self.local_update_time

    def get_period(self) -> str | None:
        return self.period

    def get_open_time(self) -> float | int:
        return self.open_time or 0

    def get_open_price(self) -> float | int:
        return self.open_price or 0.0

    def get_high_price(self) -> float | int:
        return self.high_price or 0.0

    def get_low_price(self) -> float | int:
        return self.low_price or 0.0

    def get_close_price(self) -> float | int:
        return self.close_price or 0.0

    def get_volume(self) -> float | int:
        return self.volume or 0.0

    def get_amount(self) -> float | int:
        return 0.0

    def get_close_time(self) -> float | int:
        return self.get_open_time()

    def get_quote_asset_volume(self) -> float | int:
        return 0.0

    def get_base_asset_volume(self) -> float | int:
        return self.get_volume()

    def get_num_trades(self) -> int:
        return 0

    def get_taker_buy_base_asset_volume(self) -> float | int:
        return 0.0

    def get_taker_buy_quote_asset_volume(self) -> float | int:
        return 0.0

    def get_bar_status(self) -> bool | int:
        return True


class CoinSpotRequestBarData(CoinSpotBarData):
    pass


class CoinSpotWssBarData(CoinSpotBarData):
    pass
