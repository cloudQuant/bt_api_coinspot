from __future__ import annotations

from bt_api_base.feeds.capability import Capability

from bt_api_coinspot.feeds.live_coinspot.request_base import CoinSpotRequestData


class CoinSpotRequestDataSpot(CoinSpotRequestData):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_DEPTH,
            Capability.GET_DEALS,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
        }

    def __init__(self, data_queue=None, **kwargs) -> None:
        super().__init__(data_queue, **kwargs)

    def get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_ticker(self, symbol, extra_data=None, **kwargs):
        return self.get_tick(symbol, extra_data, **kwargs)

    async def async_get_ticker(self, symbol, extra_data=None, **kwargs):
        return await self.async_get_tick(symbol, extra_data, **kwargs)

    def get_all_tickers(self, extra_data=None, **kwargs):
        path, params, extra = self._get_all_tickers(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_all_tickers(self, extra_data=None, **kwargs):
        path, params, extra = self._get_all_tickers(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        del count
        path, params, extra = self._get_depth(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        del count
        path, params, extra = self._get_depth(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_deals(
        self, symbol, count=100, start_time=None, end_time=None, extra_data=None, **kwargs
    ):
        del count, start_time, end_time
        path, params, extra = self._get_deals(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_deals(
        self,
        symbol,
        count=100,
        start_time=None,
        end_time=None,
        extra_data=None,
        **kwargs,
    ):
        del count, start_time, end_time
        path, params, extra = self._get_deals(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def make_order(
        self,
        symbol,
        volume,
        price,
        order_type,
        offset="open",
        post_only=False,
        client_order_id=None,
        extra_data=None,
        **kwargs,
    ):
        del offset, post_only, client_order_id
        path, body, extra = self._make_order(
            symbol, volume, price, order_type, extra_data, **kwargs
        )
        return self.request(path, body=body, extra_data=extra, is_sign=True)

    async def async_make_order(
        self,
        symbol,
        volume,
        price,
        order_type,
        offset="open",
        post_only=False,
        client_order_id=None,
        extra_data=None,
        **kwargs,
    ):
        del offset, post_only, client_order_id
        path, body, extra = self._make_order(
            symbol, volume, price, order_type, extra_data, **kwargs
        )
        return await self.async_request(path, body=body, extra_data=extra, is_sign=True)

    def cancel_order(self, symbol, order_id, extra_data=None, **kwargs):
        del symbol
        side = kwargs.pop("side", "buy")
        path, body, extra = self._cancel_order(order_id, side, extra_data, **kwargs)
        return self.request(path, body=body, extra_data=extra, is_sign=True)

    async def async_cancel_order(self, symbol, order_id, extra_data=None, **kwargs):
        del symbol
        side = kwargs.pop("side", "buy")
        path, body, extra = self._cancel_order(order_id, side, extra_data, **kwargs)
        return await self.async_request(path, body=body, extra_data=extra, is_sign=True)

    def get_balance(self, symbol=None, extra_data=None, **kwargs):
        del symbol
        path, body, extra = self._get_balance(extra_data, **kwargs)
        return self.request(path, body=body, extra_data=extra, is_sign=True)

    async def async_get_balance(self, symbol=None, extra_data=None, **kwargs):
        del symbol
        path, body, extra = self._get_balance(extra_data, **kwargs)
        return await self.async_request(path, body=body, extra_data=extra, is_sign=True)

    def get_account(self, symbol="ALL", extra_data=None, **kwargs):
        del symbol
        path, body, extra = self._get_account(extra_data, **kwargs)
        return self.request(path, body=body, extra_data=extra, is_sign=True)

    async def async_get_account(self, symbol="ALL", extra_data=None, **kwargs):
        del symbol
        path, body, extra = self._get_account(extra_data, **kwargs)
        return await self.async_request(path, body=body, extra_data=extra, is_sign=True)
