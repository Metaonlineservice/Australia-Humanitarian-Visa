import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇦🇺 به ربات معلومات ویزای استرالیا خوش آمدید\n\n"
        "1️⃣ ویزای بشردوستانه\n"
        "2️⃣ ویزای کاری\n"
        "3️⃣ ویزای تحصیلی"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")

app.run_polling()
