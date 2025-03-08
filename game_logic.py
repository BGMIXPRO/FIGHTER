import random

def stop_fight(context):
    """Stop the timed fight and display the results."""
    global fight_active
    fight_active = False
    context.bot.send_message(chat_id=context.job.context.effective_chat.id, text=get_translation("timed_fight_ended", context.job.context.effective_chat.id))
    result(context.job.context, context)

def get_themed_reply(theme, username):
    """Get a themed reply based on the current fight theme."""
    themed_replies = {
        "default": f"Pow!",
        "anime": f"Nani?! {username}-san strikes back!",
        "wrestling": f"{username} with the devastating move!",
        "gaming": f"{username} scores a critical hit!"
    }
    return themed_replies.get(theme, "")

def get_power_up(theme):
    """Get a random power-up based on the current fight theme."""
    power_ups = {
        "default": None,
        "anime": "⚡ Anime power-up! 🌟",
        "wrestling": "🏆 Championship belt acquired! 💪",
        "gaming": "🎮 Level up! Unlocked new abilities! 🕹️"
    }
    return power_ups.get(theme, None)

def get_achievement_title(achievement):
    """Get the title for the given achievement."""
    achievement_titles = {
        "slayer": "🗡️ Slayer",
        "champion": "🏅 Champion",
        # Add more achievements and their titles here
    }
    return achievement_titles.get(achievement, achievement)
