import json
import hashlib
import secrets
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# بارگذاری تنظیمات
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["TOKEN"]
ADMIN_CHAT_ID = config["ADMIN_CHAT_ID"]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 سلام! برای خرید اتصال از /buy استفاده کنید.")

def buy(update: Update, context: CallbackContext):
    update.message.reply_text("💰 لطفاً رسید پرداخت را ارسال کنید.")

def handle_payment(update: Update, context: CallbackContext):
    if update.message.photo:
        context.bot.send_photo(
            chat_id=ADMIN_CHAT_ID,
            photo=update.message.photo[-1].file_id,
            caption=f"💳 پرداخت جدید از @{update.message.from_user.username}"
        )
        update.message.reply_text("✅ رسید شما دریافت شد و در حال بررسی است.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(MessageHandler(Filters.photo, handle_payment))

    print("🤖 ربات فعال شد!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
