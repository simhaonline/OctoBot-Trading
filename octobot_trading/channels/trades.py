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
from asyncio import CancelledError

from octobot_channels import CHANNEL_WILDCARD
from octobot_channels.producer import Producer
from octobot_commons.logging.logging_util import get_logger

from octobot_trading.channels.exchange_channel import ExchangeChannel, ExchangeChannelProducer
from octobot_trading.enums import ExchangeConstantsOrderColumns


class TradesProducer(ExchangeChannelProducer):
    def __init__(self, channel):
        self.logger = get_logger(self.__class__.__name__)
        super().__init__(channel)
        self.channel = channel

    async def push(self, trades, old_trade=False):
        await self.perform(trades, old_trade=old_trade)

    async def perform(self, trades, old_trade=False):
        try:
            for trade in trades:
                symbol: str = self.channel.exchange_manager.get_exchange_symbol(
                    trade[ExchangeConstantsOrderColumns.SYMBOL.value])
                if CHANNEL_WILDCARD in self.channel.consumers or symbol in self.channel.consumers:
                    trade_id: str = trade[ExchangeConstantsOrderColumns.ID.value]

                    added: bool = await self.channel.exchange_manager.exchange_personal_data.handle_trade_update(
                        symbol,
                        trade_id,
                        trade,
                        should_notify=False)

                    if added:
                        await self.send_with_wildcard(symbol=symbol, trade=trade, old_trade=old_trade)
        except CancelledError:
            self.logger.info("Update tasks cancelled.")
        except Exception as e:
            self.logger.error(f"exception when triggering update: {e}")
            self.logger.exception(e)

    async def send(self, symbol, trade, old_trade=False, is_wildcard=False):
        for consumer in self.channel.get_consumers(symbol=CHANNEL_WILDCARD if is_wildcard else symbol):
            await consumer.queue.put({
                "exchange": self.channel.exchange_manager.exchange.name,
                "symbol": symbol,
                "trade": trade,
                "old_trade": old_trade
            })


class TradesChannel(ExchangeChannel):
    PRODUCER_CLASS = TradesProducer