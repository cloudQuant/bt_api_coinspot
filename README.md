# bt_api_coinspot

CoinSpot exchange package for `bt_api`.

## Installation

```bash
pip install bt_api_coinspot
```

## Usage

When installed alongside `bt_api_py`, the package is discovered automatically by the unified plugin loader.

## Supported Exchanges

- COINSPOT___SPOT

## Authentication

CoinSpot uses HMAC-SHA512 authentication for private endpoints. Provide your API key and secret when initializing.

## API Endpoints

- REST: `https://www.coinspot.com.au`

## Symbol Format

CoinSpot uses coin shortnames (e.g., `BTC`, `ETH`) rather than trading pairs.
