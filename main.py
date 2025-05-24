import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm QaraVideo Bot. Send me a YouTube link!")

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))  # PORT Fly.io ушын керек
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(drop_pending_updates=True)  # polling режим
