from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 Registration", url="https://google.com")],
        [InlineKeyboardButton("🎰 Monopoly", url="https://google.com")],
        [InlineKeyboardButton("🧡 Daddy Partners", url="https://google.com")]
    ]

    text = """
🎲 Welcome to Monopoly by Daddy Partners!

Monopoly is our in-house iGaming product built for affiliates, SEO teams, PPC specialists, media buyers and traffic owners looking to scale across Tier 2 and Tier 3 markets.

🚀 What we offer:
• Strong product with long-term growth potential
• Flexible partnership terms
• Fast support and direct communication
• New GEO opportunities

👑 CEO
🧩 CAO
🤝 Affiliate Manager
💳 Head of Payments

Choose an option below to get started.
"""

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
