from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.accounts.account import AccountData


class CoinSpotAccountData(AccountData):
    def __init__(
        self,
        account_info: Any,
        symbol_name: str | None = None,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(account_info, has_been_json_encoded)
        self.exchange_name = "COINSPOT"
        self.asset_type = "SPOT"
        self.symbol_name = symbol_name
        self.account_data = account_info if has_been_json_encoded else None
        self.fee_tier: int | str | None = None
        self.max_withdraw_amount: float | None = None
        self.total_margin: float | None = None
        self.total_used_margin: float | None = None
        self.total_maintain_margin: float | None = None
        self.total_available_margin: float | None = None
        self.total_open_order_initial_margin: float | None = None
        self.total_position_initial_margin: float | None = None
        self.total_unrealized_profit: float | None = None
        self.total_wallet_balance: float | None = None
        self.balances: list[Any] = []
        self.positions: list[Any] = []
        self.local_update_time = time.time()
        self.has_been_init_data = False

    def init_data(self) -> CoinSpotAccountData:
        if not self.has_been_json_encoded:
            self.account_data = (
                json.loads(self.account_info) if isinstance(self.account_info, str) else {}
            )
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        if isinstance(self.account_data, dict):
            self.account_id = "COINSPOT_SPOT"
            self.account_type = "SPOT"
            self.can_deposit = True
            self.can_trade = True
            self.can_withdraw = True
            raw_balances = self.account_data.get("balances", self.account_data.get("balance", []))
            if isinstance(raw_balances, dict):
                self.balances = [raw_balances]
            elif isinstance(raw_balances, list):
                self.balances = raw_balances
            self.total_wallet_balance = 0.0
            self.total_available_margin = 0.0
            self.total_unrealized_profit = 0.0

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "account_id": self.account_id,
                "account_type": self.account_type,
                "can_deposit": self.can_deposit,
                "can_trade": self.can_trade,
                "can_withdraw": self.can_withdraw,
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

    def get_asset_type(self) -> str | None:
        return self.asset_type

    def get_server_time(self) -> int | float | None:
        return self.server_time

    def get_local_update_time(self) -> float:
        return float(self.local_update_time or 0.0)

    def get_account_id(self) -> str | None:
        return self.account_id

    def get_account_type(self) -> str | None:
        return self.account_type

    def get_can_deposit(self) -> bool | None:
        return self.can_deposit

    def get_can_trade(self) -> bool | None:
        return self.can_trade

    def get_can_withdraw(self) -> bool | None:
        return self.can_withdraw

    def get_fee_tier(self) -> int | str | None:
        return self.fee_tier

    def get_max_withdraw_amount(self) -> float | None:
        return self.max_withdraw_amount

    def get_total_margin(self) -> float | None:
        return self.total_margin

    def get_total_used_margin(self) -> float | None:
        return self.total_used_margin

    def get_total_maintain_margin(self) -> float | None:
        return self.total_maintain_margin

    def get_total_available_margin(self) -> float | None:
        return self.total_available_margin

    def get_total_open_order_initial_margin(self) -> float | None:
        return self.total_open_order_initial_margin

    def get_total_position_initial_margin(self) -> float | None:
        return self.total_position_initial_margin

    def get_total_unrealized_profit(self) -> float | None:
        return self.total_unrealized_profit

    def get_total_wallet_balance(self) -> float | None:
        return self.total_wallet_balance

    def get_balances(self) -> list[Any]:
        return self.balances

    def get_positions(self) -> list[Any]:
        return self.positions

    def get_spot_maker_commission_rate(self) -> float | None:
        return None

    def get_spot_taker_commission_rate(self) -> float | None:
        return None

    def get_future_maker_commission_rate(self) -> float | None:
        return None

    def get_future_taker_commission_rate(self) -> float | None:
        return None

    def get_option_maker_commission_rate(self) -> float | None:
        return None

    def get_option_taker_commission_rate(self) -> float | None:
        return None

    def get_margin(self) -> float | None:
        return self.total_wallet_balance

    def get_available_margin(self) -> float | None:
        return self.total_available_margin

    def get_unrealized_profit(self) -> float | None:
        return self.total_unrealized_profit


class CoinSpotRequestAccountData(CoinSpotAccountData):
    pass


class CoinSpotWssAccountData(CoinSpotAccountData):
    pass
