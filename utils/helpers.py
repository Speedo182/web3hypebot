# utils/helpers.py

"""
Contains utility functions used across the Web3HypeBot.

These helper functions perform common tasks such as data formatting,
validations, and other shared operations required by various parts
of the bot.
"""

def format_task_message(task_info):
    """
    Formats a message to display task information.

    :param task_info: Dictionary containing task details.
    :return: Formatted string with task details.
    """
    message = f"Task: {task_info['name']}\nDescription: {task_info['description']}\nReward: {task_info['reward']}\n"
    return message

def validate_wallet_address(wallet_address):
    """
    Validates a given wallet address.

    :param wallet_address: String containing the wallet address.
    :return: Boolean indicating if the address is valid.
    """
    # Implement wallet address validation logic (e.g., regex match for format)
    return True  # Placeholder return. Replace with actual validation logic.

def calculate_reward_allocation(user_data, reward_pool):
    """
    Calculates the user's share in the reward pool based on task completion.

    :param user_data: Dictionary containing user's task completion details.
    :param reward_pool: Total available reward pool for allocation.
    :return: Amount allocated to the user.
    """
    # Implement reward calculation based on task completions and reward pool size
    return 0  # Placeholder return. Replace with actual calculation logic.

# Add more utility functions as needed for common tasks across the bot.
