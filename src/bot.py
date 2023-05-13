from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update

import os
from dotenv import load_dotenv


load_dotenv()


async def channel_message_handler(update: Update, context):
    print(f"New message arrived: {update.message.text}")



if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()
    app.add_handler(MessageHandler(filters.ALL, channel_message_handler))

    app.run_polling()