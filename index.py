from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "8133649039:AAFLpgxN8TmzEjszY5zjoGaPX5wpkR8rKgk"

async def start(update: Update, context):
    await update.message.reply_text('স্বাগতম! টোকেন উপার্জন শুরু করুন!')

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()