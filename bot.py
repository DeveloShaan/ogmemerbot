import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Yo, welcome to OG Memer Bot!\n\nType /meme to get a spicy meme 🔥")

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()
        meme_title = data["title"]
        meme_url = data["url"]
        await update.message.reply_photo(photo=meme_url, caption=meme_title)
    except:
        await update.message.reply_text("Oops! Meme machine broke 😅 Try again later.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("meme", meme))
app.run_polling()
