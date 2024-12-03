import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7875972983:AAHg3Vl73g1x_5GdSTVJqHVVHpwVDi6lH3s'  # Replace with your bot token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}! Welcome to the bot!")

@dp.message(Command("help"))
async def send_help(message: types.Message):
    help_text = "I can assist you with the following commands:\n- /faq\n- /support\n- /application"
    await message.answer(help_text)

# Handle FAQ command
@dp.message(Command("faq"))
async def faq_command(message: types.Message):
    faq_text = """
    FAQ:
    1. How can I connect with support?
    - Use the /support command.
    2. How can I submit an application or comment?
    - Use the /application command.
    """
    await message.answer(faq_text)

# Handle /support command (for connecting to the admin)
@dp.message(Command("support"))
async def support_command(message: types.Message):
    admin_chat_id = '-1002369796801'  # Replace with actual admin chat ID
    await bot.send_message(admin_chat_id, f"New support request from {message.from_user.full_name}: {message.text}")
    await message.answer("Your message has been forwarded to the admin.")

# Handle /application command (for submitting applications/comments)
@dp.message(Command("application"))
async def application_command(message: types.Message):
    await message.answer("Please provide your application details. Admin will review it.")


if __name__ == '__main__':
    dp.run_polling(bot)

