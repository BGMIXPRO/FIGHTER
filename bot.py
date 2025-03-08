"""
Telegram Fight Bot 🤖
A Telegram bot that allows users to engage in a "fight" by replying to each other, with various gameplay features, leaderboard functionality, and an achievement system.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, filters, InlineKeyboardButton, InlineKeyboardMarkup
from fight_handlers import start, help, fight, stop, result, timedfight, themedfight, title, teamfight, duel, unlock_achievement
from combat_handlers import reply, attack, defend
from game_logic import stop_fight
from translations import get_translation

def start(update, context):
    """Start the bot and display the welcome message."""
    join_button = InlineKeyboardButton(text="Join Channel", url="https://t.me/your_channel_link")
    keyboard = InlineKeyboardMarkup([[join_button]])
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_translation("welcome", update.effective_chat.id), reply_markup=keyboard)

def help(update, context):
    """Display the available commands and their descriptions."""
    help_text = get_translation("help_text", update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def main():
    """Set up the bot and add the necessary handlers."""
    updater = Updater(token='7611645869:AAGc1VrSQ4nsavRd7xlYMdK8As9VSwbZsII', use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("fight", fight))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("result", result))
    dispatcher.add_handler(CommandHandler("timedfight", timedfight))
    dispatcher.add_handler(CommandHandler("themedfight", themedfight))
    dispatcher.add_handler(CommandHandler("title", title))
    dispatcher.add_handler(CommandHandler("teamfight", teamfight))
    dispatcher.add_handler(CommandHandler("duel", duel))
    dispatcher.add_handler(CommandHandler("unlock", unlock_achievement))

    # Add message handlers
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    dispatcher.add_handler(CommandHandler("attack", attack))
    dispatcher.add_handler(CommandHandler("defend", defend))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
