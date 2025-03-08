import random
from collections import defaultdict
from utils.translations import get_translation
from utils.game_logic import get_themed_reply, get_power_up

# Global variables 🌐
fight_participants = {}
fight_scores = defaultdict(int)
fight_active = False
fight_theme = "default"
fight_titles = {}

def reply(update, context):
    """Handle user replies and update the fight scores."""
    global fight_active, fight_participants, fight_scores, fight_theme, fight_titles

    if not fight_active:
        return

    username = update.effective_user.username
    if username not in fight_participants:
        return

    fight_scores[username] += 1
    themed_reply = get_themed_reply(fight_theme, username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{themed_reply} @{username} {get_translation('scored_point', update.effective_chat.id)} {fight_scores[username]} {get_translation('points', update.effective_chat.id)} 💥")

    # Combo system 🔥
    if len(context.args) > 0 and context.args[0] in fight_participants:
        target_user = context.args[0].replace("@", "")
        if target_user in fight_scores:
            fight_scores[target_user] -= 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"{get_translation('combo_hit', update.effective_chat.id)} @{target_user} {get_translation('lost_point', update.effective_chat.id)} {fight_scores[target_user]} {get_translation('points', update.effective_chat.id)} 😨")

    # Critical hit chance 🎲
    if random.random() < 0.1:
        fight_scores[username] += 5
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{get_translation('critical_hit', update.effective_chat.id)} @{username} {get_translation('scored_points', update.effective_chat.id)} {fight_scores[username]} 💥")

    # Power-ups 🔥
    power_up = get_power_up(fight_theme)
    if power_up:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{power_up}")

    # Custom Titles 👑
    if username in fight_titles:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{get_translation('title_used', update.effective_chat.id, fight_titles[username], username)}")

def attack(update, context):
    """Allow users to attack other participants and reduce their score."""
    global fight_active, fight_scores

    if not fight_active:
        return

    if len(context.args) < 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text=get_translation("mention_attack_target", update.effective_chat.id))
        return

    target_user = context.args[0].replace("@", "")
    if target_user in fight_scores:
        fight_scores[target_user] -= 3
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{get_translation('attack_success', update.effective_chat.id, target_user)} {fight_scores[target_user]} {get_translation('points', update.effective_chat.id)} 💥")

def defend(update, context):
    """Allow users to defend themselves and gain points."""
    global fight_active, fight_scores

    if not fight_active:
        return

    username = update.effective_user.username
    if username in fight_scores:
        fight_scores[username] += 2
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{get_translation('defense_success', update.effective_chat.id, username)} {fight_scores[username]} {get_translation('points', update.effective_chat.id)} 🛡️")
