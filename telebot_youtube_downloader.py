import telebot
import yt_dlp
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Telegram Bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Ensure the BOT_TOKEN is being correctly fetched
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing. Please set it in the .env file.")

# # Replace with your Telegram Bot Token
# BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)

# Directory for temporary downloads
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Welcome! Send me a YouTube link, and I'll let you download the video as MP4 or MP3."
    )

@bot.message_handler(func=lambda message: 'youtube.com' in message.text or 'youtu.be' in message.text)
def handle_youtube_link(message):
    youtube_url = message.text.strip()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("Download MP4", callback_data=f"download|mp4|{youtube_url}"),
        telebot.types.InlineKeyboardButton("Download MP3", callback_data=f"download|mp3|{youtube_url}")
    )
    bot.send_message(message.chat.id, "Choose your download format:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("download"))
def download_video_or_audio(call):
    _, file_format, youtube_url = call.data.split('|')
    chat_id = call.message.chat.id

    try:
        ydl_opts = {
            "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
            "format": "bestvideo+bestaudio/best" if file_format == "mp4" else "bestaudio/best",
            "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}] if file_format == "mp3" else [],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            file_name = ydl.prepare_filename(info)
            if file_format == "mp3":
                file_name = file_name.rsplit('.', 1)[0] + ".mp3"

        bot.send_message(chat_id, f"Uploading {file_format.upper()} file...")
        with open(file_name, "rb") as file:
            if file_format == "mp4":
                bot.send_video(chat_id, file)
            else:
                bot.send_audio(chat_id, file)
        bot.send_message(chat_id, "Download complete!")
    except Exception as e:
        bot.send_message(chat_id, f"Error: {e}")
    finally:
        # Clean up temporary files
        for file in os.listdir(DOWNLOAD_FOLDER):
            os.remove(os.path.join(DOWNLOAD_FOLDER, file))

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
