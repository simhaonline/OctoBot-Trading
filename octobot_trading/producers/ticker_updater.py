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
#  License along with this library.
import asyncio

from ccxt.base.errors import NotSupported

from octobot_trading.channels import TICKER_CHANNEL
from octobot_trading.channels.ticker import TickerProducer


class TickerUpdater(TickerProducer):
    CHANNEL_NAME = TICKER_CHANNEL
    TICKER_REFRESH_TIME = 64

    def __init__(self, channel):
        super().__init__(channel)
        self._added_pairs = []

    async def start(self):
        while not self.should_stop and not self.channel.is_paused:
            try:
                for pair in self.__get_pairs_to_update():
                    ticker: dict = await self.channel.exchange_manager.exchange.get_price_ticker(pair)

                    if ticker:
                        await self.push(pair, ticker)

                await asyncio.sleep(self.TICKER_REFRESH_TIME)
            except NotSupported:
                self.logger.warning(f"{self.channel.exchange_manager.exchange.name} is not supporting updates")
                await self.pause()
            except Exception as e:
                self.logger.exception(f"Fail to update ticker : {e}")

    def _cleanup_ticker_dict(self, ticker):
        try:
            ticker.pop("info")
            ticker.pop("symbol")
            ticker.pop("datetime")
        except KeyError as e:
            self.logger.error(f"Fail to cleanup ticker dict ({e})")
        return ticker

    def __get_pairs_to_update(self):
        return self.channel.exchange_manager.traded_pairs + self._added_pairs

    async def modify(self, added_pairs=None, removed_pairs=None):
        if added_pairs:
            self._added_pairs += [pair
                                  for pair in added_pairs
                                  if pair not in self.__get_pairs_to_update()]
            self.logger.info(f"Added pairs : {added_pairs}")

        if removed_pairs:
            self._added_pairs -= removed_pairs
            self.logger.info(f"Removed pairs : {removed_pairs}")

    async def resume(self) -> None:
        await super().resume()
        await self.run()
