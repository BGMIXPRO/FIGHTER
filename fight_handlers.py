from collections import defaultdict
from utils.translations import get_translation
from utils.game_logic import get_achievement_title

# Global variables 🌐
fight_participants = {}
fight_scores = defaultdict(int)
fight_active = False
fight_duration = 60  # 1 minute
fight_theme = "default"
fight_titles = {}
user_achievements = defaultdict(list)

def start(update, context):
    """Start the bot and display the welcome message."""
    join_button = InlineKeyboardButton(text="Join Channel ✅", url="https://t.me/FIGHTIN_GROUP")
    keyboard = InlineKeyboardMarkup([[join_button]])
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_translation("welcome", update.effective_chat.id), reply_markup=keyboard)

def help(update, context):
    """Display the available commands and their descriptions."""
    help_text = get_translation("help_text", update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def unlock_achievement(update, context):
    """Unlock an achievement for a user."""
    if len(context.args) < 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_translation("provide_achievement_and_user", update.effective_chat.id))
        return

    achievement = context.args[0]
    username = context.args[1]

    if achievement in user_achievements[username]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_translation("achievement_already_unlocked", update.effective_chat.id, username, achievement))
        return

    user_achievements[username].append(achievement)
    title = get_achievement_title(achievement)
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_translation("achievement_unlocked", update.effective_chat.id, username, title))

# Rest of the code remains the same
