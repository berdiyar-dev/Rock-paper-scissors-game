from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import random
from config import TOKEN_API

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Assalomu alaykum! Rock, Paper, Scissors o'yiniga xush kelibsiz! /play komandasini bosing.")

def play(update: Update, context: CallbackContext) -> None:
    options = ["Rock", "Paper", "Scissors"]
    user_choice = update.message.text.split(' ', 1)[1].capitalize()
    bot_choice = random.choice(options)

    if user_choice in options:
        if user_choice == bot_choice:
            result = "Durrang!"
        elif (user_choice == "Rock" and bot_choice == "Scissors") or \
             (user_choice == "Scissors" and bot_choice == "Paper") or \
             (user_choice == "Paper" and bot_choice == "Rock"):
            result = "Siz yutdingiz!"
        else:
            result = "Bot yutdi!"

        update.message.reply_text(f"Siz: {user_choice}\nBot: {bot_choice}\nNatija: {result}")
    else:
        update.message.reply_text("Noto'g'ri tanlov! Quyidagi tanlovlardan birini kiriting: Rock, Paper, Scissors")

def main() -> None:
    updater = Updater(TOKEN_API)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("play", play))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
