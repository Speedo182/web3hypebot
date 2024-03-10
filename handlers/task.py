# handlers/task.py

"""
Manage user tasks in Web3HypeBot.

This script is responsible for tracking user tasks, verifying completion, and updating user status.
"""

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from utils.helpers import get_task_list, verify_task_completion, update_user_status
from database.db_manager import update_task_status

async def handle_tasks(update: Update, context: CallbackContext) -> None:
    """Provide the user with a list of tasks and track their completion."""
    user = update.effective_user
    tasks = get_task_list()

    # Send a message with the list of tasks
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello {user.first_name}, here are your tasks:\n\n{tasks}"
    )

    # Check for task completion
    if verify_task_completion(user.id):
        update_user_status(user.id, 'completed')
        update_task_status(user.id, 'complete')
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Congratulations on completing the tasks!"
        )

# This script can be extended with more functionalities such as:
# - Dynamic task generation based on user interaction.
# - Rewards allocation for task completion.
# - Real-time tracking of task status.

# Handler registration in bot.py
# application.add_handler(CommandHandler("tasks", handle_tasks))
