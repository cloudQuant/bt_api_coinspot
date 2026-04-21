from __future__ import annotations

from bt_api_base.gateway.registrar import GatewayRuntimeRegistrar
from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry

from bt_api_coinspot import registry_registration as _registry_registration


def register_plugin(
    registry: type[ExchangeRegistry], runtime_factory: type[GatewayRuntimeRegistrar]
) -> PluginInfo:
    del runtime_factory
    _registry_registration.register_coinspot(registry)
    return PluginInfo(
        name="bt_api_coinspot",
        version="0.1.0",
        core_requires=">=0.15,<1.0",
        supported_exchanges=("COINSPOT___SPOT",),
        supported_asset_types=("SPOT",),
    )
