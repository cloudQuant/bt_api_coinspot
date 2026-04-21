from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _coinspot_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_coinspot.exchange_data import CoinSpotExchangeDataSpot
from bt_api_coinspot.feeds.live_coinspot.spot import CoinSpotRequestDataSpot


def register_coinspot(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("COINSPOT___SPOT", CoinSpotRequestDataSpot)
    registry.register_exchange_data("COINSPOT___SPOT", CoinSpotExchangeDataSpot)
    registry.register_balance_handler("COINSPOT___SPOT", _coinspot_balance_handler)
