# bt_api_coinspot

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_coinspot.svg)](https://pypi.org/project/bt_api_coinspot/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_coinspot.svg)](https://pypi.org/project/bt_api_coinspot/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_coinspot/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_coinspot/actions)
[![Docs](https://readthedocs.org/projects/bt-api-coinspot/badge/?version=latest)](https://bt-api-coinspot.readthedocs.io/)

---

> **CoinSpot exchange plugin for bt_api** — Unified REST API for **Spot** trading.

`bt_api_coinspot` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **CoinSpot** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-coinspot.readthedocs.io/ |
| Chinese Docs | https://bt-api-coinspot.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coinspot |
| PyPI | https://pypi.org/project/bt_api_coinspot/ |
| Issues | https://github.com/cloudQuant/bt_api_coinspot/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### 1 Asset Type

| Asset Type | Code | REST | Description |
|---|---|---|---|
| Spot | `COINSPOT___SPOT` | ✅ | Spot trading (Australian exchange) |

### Supported Operations

| Category | Operation | Spot |
|---|---|---|
| **Market Data** | `get_tick` / `get_ticker` | ✅ |
| | `get_all_tickers` | ✅ |
| | `get_depth` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_deals` | ✅ |
| **Trading** | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| **Account** | `get_balance` | ✅ |
| | `get_account` | ✅ |

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# Spot market data (public - no auth required)
ticker = api.get_tick("COINSPOT___SPOT", "BTC-AUD")

# Account balance (requires auth)
balance = api.get_balance("COINSPOT___SPOT")

# Place order (requires auth)
order = api.make_order(
    exchange_name="COINSPOT___SPOT",
    symbol="BTC-AUD",
    volume=0.001,
    price=50000,
    order_type="bid",
)
```

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_coinspot
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_coinspot
cd bt_api_coinspot
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## Quick Start

### 1. Install

```bash
pip install bt_api_coinspot
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("COINSPOT___SPOT", "BTC-AUD")
print(f"BTC/AUD spot price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="COINSPOT___SPOT",
    symbol="BTC-AUD",
    volume=0.001,
    price=50000,
    order_type="bid",
)
print(f"Order placed: {order}")
```

---

## Architecture

```
bt_api_coinspot/
├── plugin.py                           # register_plugin() — bt_api plugin entry point
├── registry_registration.py             # register_coinspot() — feeds / exchange_data registration
├── exchange_data/
│   └── __init__.py                  # CoinSpotExchangeDataSpot — exchange configuration
├── feeds/
│   ├── request_base.py               # CoinSpotRequestData — REST base class
│   └── live_coinspot/
│       ├── spot.py                  # CoinSpotRequestDataSpot — spot operations
│       └── __init__.py
├── containers/
│   ├── tickers/
│   │   └── coinspot_ticker.py    # Ticker container
│   ├── balances/
│   ├── orders/
│   ├── orderbooks/
│   ├── bars/
│   └── accounts/
└── errors/
```

---

## Supported Symbols

- **Spot**: `BTC-AUD`, `ETH-AUD`, `LTC-AUD`, and 100+ AUD trading pairs

---

## Exchange Code

```
COINSPOT___SPOT     # Spot trading (Australian Dollar market)
```

---

## Error Handling

All CoinSpot API errors are translated to bt_api_base `ApiError` subclasses.

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-coinspot.readthedocs.io/ |
| **中文** | https://bt-api-coinspot.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_coinspot/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 CoinSpot 交易所插件** — 为**现货**交易提供统一的 REST API。

`bt_api_coinspot` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **CoinSpot** 交易所。CoinSpot 是澳大利亚领先的加密货币交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-coinspot.readthedocs.io/ |
| 中文文档 | https://bt-api-coinspot.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coinspot |
| PyPI | https://pypi.org/project/bt_api_coinspot/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_coinspot/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 1 种资产类型

| 资产类型 | 代码 | REST | 说明 |
|---|---|---|---|
| 现货 | `COINSPOT___SPOT` | ✅ | 现货交易（澳元市场） |

### 支持的操作

| 类别 | 操作 | 现货 |
|---|---|---|
| **行情数据** | `get_tick` / `get_ticker` | ✅ |
| | `get_all_tickers` | ✅ |
| | `get_depth` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_deals` | ✅ |
| **交易** | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| **账户** | `get_balance` | ✅ |
| | `get_account` | ✅ |

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# 现货行情（公开接口，无需认证）
ticker = api.get_tick("COINSPOT___SPOT", "BTC-AUD")

# 账户余额（需要认证）
balance = api.get_balance("COINSPOT___SPOT")

# 下单（需要认证）
order = api.make_order(
    exchange_name="COINSPOT___SPOT",
    symbol="BTC-AUD",
    volume=0.001,
    price=50000,
    order_type="bid",
)
```

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_coinspot
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_coinspot
cd bt_api_coinspot
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_coinspot
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("COINSPOT___SPOT", "BTC-AUD")
print(f"BTC/AUD 现货价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="COINSPOT___SPOT",
    symbol="BTC-AUD",
    volume=0.001,
    price=50000,
    order_type="bid",
)
print(f"订单已下单: {order}")
```

---

## 架构

```
bt_api_coinspot/
├── plugin.py                           # register_plugin() — bt_api 插件入口点
├── registry_registration.py             # register_coinspot() — feeds / exchange_data 注册
├── exchange_data/
│   └── __init__.py                  # CoinSpotExchangeDataSpot — 交易所配置
├── feeds/
│   ├── request_base.py               # CoinSpotRequestData — REST 基类
│   └── live_coinspot/
│       ├── spot.py                  # CoinSpotRequestDataSpot — 现货操作
│       └── __init__.py
├── containers/
│   ├── tickers/
│   │   └── coinspot_ticker.py    # 行情容器
│   ├── balances/
│   ├── orders/
│   ├── orderbooks/
│   ├── bars/
│   └── accounts/
└── errors/
```

---

## 支持的交易对

- **现货**: `BTC-AUD`, `ETH-AUD`, `LTC-AUD` 等 100+ 澳元交易对

---

## 交易所代码

```
COINSPOT___SPOT     # 现货交易（澳元市场）
```

---

## 错误处理

所有 CoinSpot API 错误均翻译为 bt_api_base `ApiError` 子类。

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-coinspot.readthedocs.io/ |
| **中文文档** | https://bt-api-coinspot.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_coinspot/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com