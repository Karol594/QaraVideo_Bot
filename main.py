import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Сәлем! Мен QaraVideo Бот боламын. Видео жүктеп берейін.")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
