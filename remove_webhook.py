import os  # Import the os module
import telebot
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Telegram Bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Ensure the BOT_TOKEN is being correctly fetched
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing. Please set it in the .env file.")

bot = telebot.TeleBot(BOT_TOKEN)

# Telegram API URL to delete webhook
url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"

# Send request to delete the webhook
response = requests.get(url)

# Check if the webhook was deleted successfully
if response.status_code == 200:
    print("Webhook removed successfully.")
else:
    print(f"Failed to remove webhook. Status code: {response.status_code}")
