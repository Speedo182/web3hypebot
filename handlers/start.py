# handlers/start.py

"""
Handle the /start command in Web3HypeBot.

This script initiates the bot interaction by welcoming users and providing them
with initial instructions or options.
"""

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from utils.helpers import get_welcome_message

async def handle_start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message and basic instructions when the bot is started."""
    user = update.effective_user
    welcome_message = get_welcome_message(user.first_name)

    # Send a message to the user with a welcome text and initial instructions
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=welcome_message,
    )

# This script can be expanded with more functionalities such as:
# - Registering the user in the database.
# - Providing dynamic user-specific instructions.
# - Offering quick access to main features like tasks or airdrops.
