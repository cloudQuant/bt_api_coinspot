from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orders.order import OrderData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


class CoinSpotOrderData(OrderData):
    def __init__(
        self,
        order_info: Any,
        symbol_name: str | None = None,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(order_info, has_been_json_encoded)
        self.exchange_name = "COINSPOT"
        self.symbol_name = symbol_name
        self.order_data: dict[str, Any] | None = order_info if has_been_json_encoded else None
        self.order_id: str | None = None
        self.order_type: str | None = None
        self.side: str | None = None
        self.price: float | None = None
        self.amount: float | None = None
        self.filled_amount: float | None = None
        self.status: str | None = None
        self.created_at: int | None = None
        self.all_data: dict[str, Any] | None = None
        self.local_update_time = time.time()
        self.has_been_init_data = False

    def init_data(self) -> "CoinSpotOrderData":
        if not self.has_been_json_encoded:
            self.order_data = (
                json.loads(self.order_info) if isinstance(self.order_info, str) else {}
            )
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        if isinstance(self.order_data, dict):
            self.order_id = from_dict_get_string(self.order_data, "id")
            self.order_type = from_dict_get_string(self.order_data, "type")
            self.side = from_dict_get_string(self.order_data, "side")
            self.price = from_dict_get_float(self.order_data, "rate")
            self.amount = from_dict_get_float(self.order_data, "amount")
            self.filled_amount = from_dict_get_float(self.order_data, "fulfilled")
            self.status = from_dict_get_string(self.order_data, "status")

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "order_id": self.order_id,
                "order_type": self.order_type,
                "side": self.side,
                "price": self.price,
                "amount": self.amount,
                "filled_amount": self.filled_amount,
                "status": self.status,
                "created_at": self.created_at,
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
        return "SPOT"

    def get_server_time(self) -> float | None:
        return None

    def get_local_update_time(self) -> float | None:
        return self.local_update_time

    def get_trade_id(self) -> str | None:
        return None

    def get_client_order_id(self) -> str | None:
        return None

    def get_cum_quote(self) -> float | None:
        return None

    def get_executed_qty(self) -> float | None:
        return self.filled_amount

    def get_symbol_name(self) -> str | None:
        return self.symbol_name

    def get_order_id(self) -> str | None:
        return self.order_id

    def get_order_size(self) -> float | None:
        return self.amount

    def get_order_price(self) -> float | None:
        return self.price

    def get_reduce_only(self) -> bool | None:
        return None

    def get_order_side(self) -> str | None:
        return self.side

    def get_order_status(self) -> str | None:
        return self.status

    def get_order_symbol_name(self) -> str | None:
        return self.symbol_name

    def get_order_time_in_force(self) -> str | None:
        return None

    def get_order_type(self) -> str | None:
        return self.order_type

    def get_order_avg_price(self) -> float | None:
        return self.price

    def get_origin_order_type(self) -> str | None:
        return self.order_type

    def get_position_side(self) -> str | None:
        return None

    def get_trailing_stop_price(self) -> float | None:
        return None

    def get_trailing_stop_trigger_price(self) -> float | None:
        return None

    def get_trailing_stop_callback_rate(self) -> float | None:
        return None

    def get_trailing_stop_trigger_price_type(self) -> str | None:
        return None

    def get_stop_loss_price(self) -> float | None:
        return None

    def get_stop_loss_trigger_price(self) -> float | None:
        return None

    def get_stop_loss_trigger_price_type(self) -> str | None:
        return None

    def get_take_profit_price(self) -> float | None:
        return None

    def get_take_profit_trigger_price(self) -> float | None:
        return None

    def get_take_profit_trigger_price_type(self) -> str | None:
        return None

    def get_close_position(self) -> bool | None:
        return None

    def get_order_offset(self) -> str | None:
        return None

    def get_order_exchange_id(self) -> str | None:
        return self.order_id

    def get_side(self) -> str | None:
        return self.side

    def get_price(self) -> float | None:
        return self.price

    def get_amount(self) -> float | None:
        return self.amount

    def get_filled_amount(self) -> float | None:
        return self.filled_amount

    def get_status(self) -> str | None:
        return self.status

    def is_order_type(self) -> bool:
        return self.order_type in ("buy", "sell")

    def is_side(self) -> bool:
        return self.side in ("buy", "sell")


class CoinSpotRequestOrderData(CoinSpotOrderData):
    pass


class CoinSpotWssOrderData(CoinSpotOrderData):
    pass
