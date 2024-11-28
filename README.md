# Telegram Bot YouTube Downloader

## Overview

This bot allows users to download YouTube videos or audio files directly from Telegram.  
It is implemented in Python using the `telebot`, `python-dotenv` and `yt-dlp` libraries.

---

## Features

- Download YouTube videos in MP4 format.
- Extract and download audio in MP3 format.
- Clean up temporary files automatically after use.

---

## Prerequisites

Before setting up the bot, ensure you have the following:

1. Python 3.8 or later installed.
2. Required Python libraries:  
   - Install them using the command:  
     ```bash
     pip install pyTelegramBotAPI yt-dlp python-dotenv
     ```

3. [FFmpeg](https://ffmpeg.org/) installed for video and audio processing.  
   - Follow [FFmpeg installation instructions](https://ffmpeg.org/download.html).

4. A Telegram bot token created via the [BotFather](https://t.me/BotFather).

---

## Setup Instructions

Follow these steps to set up the bot:

1. Clone this repository:

   ```bash
   git clone https://github.com/NOVHUN/telegram-youtube-downloader.git
   ```
2. Navigate to the project directory:

```bash
cd telegram-youtube-downloader
```
Replace <your-telegram-bot-token> in the script with your actual bot token.

Run the bot using the command:
```bash
python telebot_youtube_downloader.py
```