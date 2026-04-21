from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


_FALLBACK_REST_PATHS = {
    "get_exchange_info": "GET /pubapi/v2/latest",
    "get_tick": "GET /pubapi/v2/latest",
    "get_buy_price": "GET /pubapi/v2/buyprice",
    "get_sell_price": "GET /pubapi/v2/sellprice",
    "get_depth": "GET /pubapi/v2/orders/open",
    "get_deals": "GET /pubapi/v2/orders/completed",
    "get_balance": "POST /api/v2/my/balances",
    "get_account": "POST /api/v2/my/balances",
    "make_order_buy": "POST /api/v2/my/buy",
    "make_order_sell": "POST /api/v2/my/sell",
    "cancel_order_buy": "POST /api/v2/my/buy/cancel",
    "cancel_order_sell": "POST /api/v2/my/sell/cancel",
}


class CoinSpotExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "COINSPOT___SPOT"
        self.rest_url = "https://www.coinspot.com.au"
        self.wss_url = ""
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1",
            "5m": "5",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "4h": "240",
            "1d": "D",
        }
        self.legal_currency = ["AUD", "USDT", "USD", "BTC", "ETH"]


class CoinSpotExchangeDataSpot(CoinSpotExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
        self.api_key: str | None = None
        self.api_secret: str | None = None

    @staticmethod
    def get_symbol(symbol: str) -> str:
        return symbol

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]
