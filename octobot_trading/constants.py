#  Drakkar-Software OctoBot-Trading
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library

# Strings
from octobot_commons.enums import TimeFrames

CURRENT_PORTFOLIO_STRING = "Current Portfolio :"
CONFIG_PORTFOLIO_INFO = "info"
CONFIG_PORTFOLIO_FREE = "free"
CONFIG_PORTFOLIO_USED = "used"
CONFIG_PORTFOLIO_TOTAL = "total"
REAL_TRADER_STR = "[Real Trader] "
SIMULATOR_TRADER_STR = "[Simulator] "

# Trader
CONFIG_TRADING = "trading"
CONFIG_TRADER = "trader"
CONFIG_TRADER_RISK = "risk"
CONFIG_TRADER_RISK_MIN = 0.05
CONFIG_TRADER_RISK_MAX = 1
CONFIG_TRADER_REFERENCE_MARKET = "reference-market"
DEFAULT_REFERENCE_MARKET = "BTC"

# Config
CONFIG_CRYPTO_CURRENCIES = "crypto-currencies"
CONFIG_CRYPTO_CURRENCY = "crypto-currency"
CONFIG_CRYPTO_PAIRS = "pairs"
CONFIG_CRYPTO_QUOTE = "quote"
CONFIG_CRYPTO_ADD = "add"

# Simulator
CONFIG_SIMULATOR = "trader-simulator"
CONFIG_STARTING_PORTFOLIO = "starting-portfolio"
SIMULATOR_CURRENT_PORTFOLIO = "simulator_current_portfolio"

# Exchange
CONFIG_EXCHANGES = "exchanges"
CONFIG_EXCHANGE_KEY = "api-key"
CONFIG_EXCHANGE_SECRET = "api-secret"
CONFIG_EXCHANGE_PASSWORD = "api-password"
CONFIG_EXCHANGE_WEB_SOCKET = "web-socket"
CONFIG_EXCHANGE_ENCRYPTED_VALUES = [CONFIG_EXCHANGE_KEY, CONFIG_EXCHANGE_SECRET, CONFIG_EXCHANGE_PASSWORD]

TESTED_EXCHANGES = ["binance", "coinbasepro", "kucoin2"]
SIMULATOR_TESTED_EXCHANGES = ["bitfinex", "bittrex", "coinbasepro", "kraken", "kucoin2", "poloniex", "cryptopia",
                              "bitmex"]

CONFIG_SIMULATOR_FEES = "fees"
CONFIG_SIMULATOR_FEES_MAKER = "maker"
CONFIG_SIMULATOR_FEES_TAKER = "taker"
CONFIG_SIMULATOR_FEES_WITHDRAW = "withdraw"
CONFIG_DEFAULT_FEES = 0.1
CONFIG_DEFAULT_SIMULATOR_FEES = 0

ORDER_CREATION_LAST_TRADES_TO_USE = 10
SIMULATOR_LAST_PRICES_TO_CHECK = 50

# Backtesting
CONFIG_BACKTESTING = "backtesting"
CONFIG_ANALYSIS_ENABLED_OPTION = "post_analysis_enabled"
BACKTESTING_DATA_OHLCV = "ohlcv"
BACKTESTING_DATA_TRADES = "trades"

BACKTESTING_DATA_FILE_EXT = ".data"
BACKTESTING_DATA_FILE_TIME_WRITE_FORMAT = '%Y%m%d_%H%M%S'
BACKTESTING_DATA_FILE_TIME_READ_FORMAT = BACKTESTING_DATA_FILE_TIME_WRITE_FORMAT.replace("_", "")
BACKTESTING_DATA_FILE_TIME_DISPLAY_FORMAT = '%d %B %Y at %H:%M:%S'
BACKTESTING_TIME_FRAMES_TO_DISPLAY = [TimeFrames.THIRTY_MINUTES.value,
                                      TimeFrames.ONE_HOUR.value,
                                      TimeFrames.FOUR_HOURS.value,
                                      TimeFrames.ONE_DAY.value]