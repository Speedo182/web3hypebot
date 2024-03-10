# handlers/__init__.py

"""Initialize the Handlers Module for Web3HypeBot.

This module sets up handlers for various bot commands such as start, task management,
and airdrop operations.
"""

from .start import handle_start
from .task import handle_task
from .airdrop import handle_airdrop

__all__ = ["handle_start", "handle_task", "handle_airdrop"]
