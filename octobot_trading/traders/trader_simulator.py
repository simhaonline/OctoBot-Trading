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

from octobot_trading.constants import SIMULATOR_CURRENT_PORTFOLIO, SIMULATOR_TRADER_STR

from octobot_trading.traders.trader import Trader
from octobot_trading.util import is_trader_simulator_enabled

""" TraderSimulator has a role of exchange response simulator
- During order creation / filling / canceling process"""


class TraderSimulator(Trader):

    NO_HISTORY_MESSAGE = "Starting a fresh new trading simulation session using trader simulator initial portfolio " \
                         "in configuration."

    def __init__(self, config, exchange_manager, previous_state_manager=None):
        self.simulate = True
        super().__init__(config, exchange_manager, previous_state_manager)

        self.trader_type_str = SIMULATOR_TRADER_STR

    @staticmethod
    def enabled(config):
        return is_trader_simulator_enabled(config)

    def _load_previous_state_if_any(self):
        loaded_previous_state = self.previous_state_manager.has_previous_state(self.exchange_manager)
        if not self.previous_state_manager.should_initialize_data() and loaded_previous_state:
            try:
                self._print_previous_state_info()
                self.loaded_previous_state = True
            except Exception as e:
                self.logger.warning(f"Error when loading trading history, will reset history. ({e})")
                self.logger.exception(e)
                self.previous_state_manager.reset_trading_history()
        else:
            self.logger.info(self.NO_HISTORY_MESSAGE)

    def _print_previous_state_info(self):
        current_portfolio = self.previous_state_manager.get_previous_state(self.exchange_manager, SIMULATOR_CURRENT_PORTFOLIO)
        self.logger.info(f"Resuming the previous trading session: current portfolio: {current_portfolio}")
