# CoinSpot Documentation

<!-- English -->
## English

Welcome to the **CoinSpot** documentation for bt_api.

**CoinSpot** is an Australian cryptocurrency exchange offering Spot trading. It is known for its strong presence in the Australian Dollar (AUD) market.

### Overview

`bt_api_coinspot` provides a unified interface to CoinSpot exchange through the bt_api plugin architecture. It supports:

- **Spot Trading**: Market data and order placement for spot pairs
- **Market Data**: Ticker, All Tickers, Order Book, Exchange Info, Trade History
- **Account**: Balance queries, Account information

### Installation

```bash
pip install bt_api_coinspot
```

### Quick Start

```python
from bt_api_py import BtApi

# Initialize without authentication (public data only)
api = BtApi()

# Spot ticker (public)
ticker = api.get_tick("COINSPOT___SPOT", "BTC-AUD")
print(f"BTC/AUD spot: {ticker}")

# With authentication
api_auth = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

# Get balance
balance = api_auth.get_balance("COINSPOT___SPOT")

# Place order
order = api_auth.make_order(
    exchange_name="COINSPOT___SPOT",
    symbol="BTC-AUD",
    volume=0.001,
    price=50000,
    order_type="bid",
)
```

### Supported Operations

#### Spot (COINSPOT___SPOT)

| Operation | Auth Required | Description |
|-----------|---------------|-------------|
| `get_tick` / `get_ticker` | No | Rolling ticker |
| `get_all_tickers` | No | All market tickers |
| `get_depth` | No | Order book depth |
| `get_exchange_info` | No | Market listings |
| `get_deals` | No | Trade execution records |
| `get_balance` | Yes | Asset balances |
| `get_account` | Yes | Account information |
| `make_order` | Yes | Place order |
| `cancel_order` | Yes | Cancel pending order |

### Supported Symbols

- **Spot**: `BTC-AUD`, `ETH-AUD`, `LTC-AUD`, and 100+ AUD trading pairs

### Exchange Codes

```
COINSPOT___SPOT     # Spot trading (Australian Dollar market)
```

### Error Handling

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("COINSPOT___SPOT")
except Exception as e:
    print(f"Error: {e}")
```

### More Information

- [GitHub Repository](https://github.com/cloudQuant/bt_api_coinspot)
- [Issue Tracker](https://github.com/cloudQuant/bt_api_coinspot/issues)
- [bt_api Documentation](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base Documentation](https://bt-api-base.readthedocs.io/)

---

## 中文

欢迎使用 bt_api 的 **CoinSpot** 文档。

**CoinSpot** 是一家澳大利亚加密货币交易所，提供现货交易。它在澳元（AUD）市场有很强的存在感。

### 概述

`bt_api_coinspot` 通过 bt_api 插件架构提供连接 CoinSpot 交易所的统一接口。支持：

- **现货交易**：现货交易对的市场数据和下单
- **行情数据**：行情、全行情、订单簿、交易所信息、成交历史
- **账户**：余额查询、账户信息

### 安装

```bash
pip install bt_api_coinspot
```

### 快速开始

```python
from bt_api_py import BtApi

# 初始化（无需认证，仅获取公开数据）
api = BtApi()

# 现货行情（公开接口）
ticker = api.get_tick("COINSPOT___SPOT", "BTC-AUD")
print(f"BTC/AUD 现货: {ticker}")

# 需要认证的操作
api_auth = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

# 获取余额
balance = api_auth.get_balance("COINSPOT___SPOT")

# 下单
order = api_auth.make_order(
    exchange_name="COINSPOT___SPOT",
    symbol="BTC-AUD",
    volume=0.001,
    price=50000,
    order_type="bid",
)
```

### 支持的操作

#### 现货 (COINSPOT___SPOT)

| 操作 | 需要认证 | 说明 |
|------|---------|------|
| `get_tick` / `get_ticker` | 否 | 滚动行情 |
| `get_all_tickers` | 否 | 所有市场行情 |
| `get_depth` | 否 | 订单簿深度 |
| `get_exchange_info` | 否 | 市场列表 |
| `get_deals` | 否 | 成交记录 |
| `get_balance` | 是 | 资产余额 |
| `get_account` | 是 | 账户信息 |
| `make_order` | 是 | 下单 |
| `cancel_order` | 是 | 取消挂单 |

### 支持的交易对

- **现货**: `BTC-AUD`, `ETH-AUD`, `LTC-AUD` 等 100+ 澳元交易对

### 交易所代码

```
COINSPOT___SPOT     # 现货交易（澳元市场）
```

### 错误处理

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSPOT___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("COINSPOT___SPOT")
except Exception as e:
    print(f"错误: {e}")
```

### 更多信息

- [GitHub 仓库](https://github.com/cloudQuant/bt_api_coinspot)
- [问题反馈](https://github.com/cloudQuant/bt_api_coinspot/issues)
- [bt_api 文档](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base 文档](https://bt-api-base.readthedocs.io/)