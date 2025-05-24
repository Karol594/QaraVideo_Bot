import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен алу - .env емес, тікелей
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Start command from user {update.effective_user.id}")
    await update.message.reply_text("Сәлем! Мен QaraVideo ботпын. YouTube сілтемесін жіберіңіз!")

def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN табылмады!")
        return
    
    logger.info("Бот іске қосылуда...")
    
    # Application жасау
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Хендлерлер
    application.add_handler(CommandHandler("start", start))
    
    # Polling басла
    logger.info("Polling басталды...")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
