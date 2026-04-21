from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.balances.balance import BalanceData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


class CoinSpotBalanceData(BalanceData):
    def __init__(
        self, balance_info: Any, asset_type: str = "SPOT", has_been_json_encoded: bool = False
    ) -> None:
        super().__init__(balance_info, has_been_json_encoded)
        self.exchange_name = "COINSPOT"
        self.asset_type = asset_type
        self.balance_data: dict[str, Any] | None = (
            balance_info if has_been_json_encoded and isinstance(balance_info, dict) else None
        )
        self.currency: str | None = None
        self.available: float | None = None
        self.locked: float | None = None
        self.all_data: dict[str, Any] | None = None
        self.server_time: float | None = None
        self.account_id: str | None = None
        self.account_type: str | None = None
        self.fee_tier: int | str | None = None
        self.max_withdraw_amount: float | None = None
        self.margin: float | None = None
        self.used_margin: float | None = None
        self.maintain_margin: float | None = None
        self.available_margin: float | None = None
        self.open_order_initial_margin: float | None = None
        self.open_order_maintenance_margin: float | None = None
        self.unrealized_profit: float | None = None
        self.interest: float | None = None
        self.local_update_time = time.time()
        self.has_been_init_data = False

    def init_data(self) -> "CoinSpotBalanceData":
        if not self.has_been_json_encoded:
            self.balance_data = (
                json.loads(self.balance_info) if isinstance(self.balance_info, str) else {}
            )
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        if isinstance(self.balance_data, dict):
            self.currency = from_dict_get_string(self.balance_data, "coin")
            self.available = from_dict_get_float(self.balance_data, "balance")
            self.locked = 0.0
            self.account_type = self.currency
            self.margin = self.available
            self.available_margin = self.available
            self.unrealized_profit = 0.0

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "asset_type": self.asset_type,
                "local_update_time": self.local_update_time,
                "currency": self.currency,
                "available": self.available,
                "locked": self.locked,
                "total": (self.available or 0.0) + (self.locked or 0.0),
            }
        return self.all_data

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_local_update_time(self) -> float:
        return float(self.local_update_time)

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_server_time(self) -> float | None:
        return self.server_time

    def get_account_id(self) -> str | None:
        return self.account_id

    def get_account_type(self) -> str | None:
        return self.account_type

    def get_fee_tier(self) -> int | str | None:
        return self.fee_tier

    def get_max_withdraw_amount(self) -> float | None:
        return self.max_withdraw_amount

    def get_margin(self) -> float | None:
        return self.margin

    def get_used_margin(self) -> float | None:
        return self.used_margin

    def get_maintain_margin(self) -> float | None:
        return self.maintain_margin

    def get_available_margin(self) -> float | None:
        return self.available_margin

    def get_open_order_initial_margin(self) -> float | None:
        return self.open_order_initial_margin

    def get_open_order_maintenance_margin(self) -> float | None:
        return self.open_order_maintenance_margin

    def get_unrealized_profit(self) -> float | None:
        return self.unrealized_profit

    def get_interest(self) -> float | None:
        return self.interest

    def get_symbol_name(self) -> str | None:
        return self.currency

    def get_currency(self) -> str | None:
        return self.currency

    def get_available(self) -> float | None:
        return self.available

    def get_locked(self) -> float | None:
        return self.locked

    def get_total(self) -> float:
        if self.available and self.locked:
            return self.available + self.locked
        return 0.0

    def is_zero_balance(self) -> bool:
        return not (self.available and self.available > 0) and not (self.locked and self.locked > 0)


class CoinSpotRequestBalanceData(CoinSpotBalanceData):
    pass


class CoinSpotWssBalanceData(CoinSpotBalanceData):
    pass
