from collections import defaultdict

translations = {
    "en": {
        "welcome": "Welcome to the Telegram Fight Bot! 👋 Use /fight to start a fight. [Join Channel](https://t.me/your_channel_link)",
        "help_text": """
        Available commands:
        /fight @user1 @user2 - Start a fight between the mentioned users 🥊
        /stop - Stop the current fight ✋
        /result - Show the leaderboard of the current fight 📊
        /timedfight <minutes> - Start a timed fight ⏱️
        /themedfight <theme> @user1 @user2 - Start a themed fight 🎨
        /title "Custom Title" @user - Give a user a custom fight title 👑
        /teamfight @user1 @user2 @user3 @user4 - Start a team fight 👥
        /duel @user - Challenge a user to a 1v1 duel ⚔️
        /attack @user - Attack a user to reduce their score 🔫
        /defend - Protect yourself from attacks 🛡️
        /help - Display the list of available commands
        /unlock <achievement> @user - Unlock an achievement for a user
        """,
        "fight_in_progress": "A fight is already in progress. Use /stop to end the current fight. 🛑",
        "mention_users": "Please mention at least two users to start a fight. 👥",
        "fight_started": "A new fight has started between {0}! 🔥",
        "no_active_fight": "There is no active fight to stop. 🤷‍♂️",
        "fight_stopped": "The fight has been stopped. 🛑",
        "no_active_fight_result": "There is no active fight to show the results for. 🤔",
        "leaderboard_header": "Leaderboard: 📊",
        "points": "points",
        "provide_duration": "Please provide the fight duration in minutes. ⏱️",
        "timed_fight_started": "A new timed fight has started! 🕰️ It will last for {0} minutes.",
        "mention_users_and_theme": "Please mention at least two users and the fight theme. 🎨",
        "themed_fight_started": "A new {0}-themed fight has started between {1}! 🎨",
        "provide_title_and_user": "Please provide a title and the user you want to give it to. 👑",
        "title_set": "The title '{1}' has been set for @{0}. 🏆",
        "mention_team_members": "Please mention the members of both teams. 👥",
        "team_fight_started": "A new team fight has started! 🆚 Team 1: {0} vs Team 2: {1} 🏆",
        "mention_duel_opponent": "Please mention the user you want to duel. ⚔️",
        "duel_started": "A duel has started between @{0} and @{1}! 🤺",
        "provide_achievement_and_user": "Please provide an achievement and the user you want to unlock it for.",
        "achievement_already_unlocked": "The achievement '{1}' has already been unlocked by @{0}.",
        "achievement_unlocked": "Congratulations, @{0} has unlocked the '{1}' achievement! 🎉"
    },
    "es": {
        "welcome": "¡Bienvenido al Telegram Fight Bot! 👋 Usa /fight para comenzar una pelea. [Únete al Canal](https://t.me/your_channel_link)",
        "help_text": """
        Comandos disponibles:
        /fight @usuario1 @usuario2 - Iniciar una pelea entre los usuarios mencionados 🥊
        /stop - Detener la pelea actual ✋
        /result - Mostrar el marcador de la pelea actual 📊
        /timedfight <minutos> - Iniciar una pelea cronometrada ⏱️
        /themedfight <tema> @usuario1 @usuario2 - Iniciar una pelea temática 🎨
        /title "Título Personalizado" @usuario - Dar a un usuario un título de pelea personalizado 👑
        /teamfight @usuario1 @usuario2 @usuario3 @usuario4 - Iniciar una pelea de equipos 👥
        /duel @usuario - Retar a un usuario a un duelo 1v1 ⚔️
        /attack @usuario - Atacar a un usuario para reducir su puntuación 🔫
        /defend - Protegerte de los ataques 🛡️
        /help - Mostrar la lista de comandos disponibles
        /unlock <logro> @usuario - Desbloquear un logro para un usuario
        """,
        "fight_in_progress": "Ya hay una pelea en curso. Usa /stop para terminar la pelea actual. 🛑",
        "mention_users": "Por favor, menciona al menos a dos usuarios para iniciar una pelea. 👥",
        "fight_started": "¡Una nueva pelea ha comenzado entre {0}! 🔥",
        "no_active_fight": "No hay ninguna pelea activa que detener. 🤷‍♂️",
        "fight_stopped": "La pelea ha sido detenida. 🛑",
        "no_active_fight_result": "No hay ninguna pelea activa cuyos resultados mostrar. 🤔",
        "leaderboard_header": "Marcador: 📊",
        "points": "puntos",
        "provide_duration": "Por favor, proporciona la duración de la pelea en minutos. ⏱️",
        "timed_fight_started": "¡Ha comenzado una nueva pelea cronometrada! 🕰️ Durará {0} minutos.",
        "mention_users_and_theme": "Por favor, menciona al menos a dos usuarios y el tema de la pelea. 🎨",
        "themed_fight_started": "¡Ha comenzado una nueva pelea con el tema de {0} entre {1}! 🎨",
        "provide_title_and_user": "Por favor, proporciona un título y el usuario al que quieres dárselo. 👑",
        "title_set": "El título '{1}' ha sido asignado a @{0}. 🏆",
        "mention_team_members": "Por favor, menciona a los miembros de ambos equipos. 👥",
        "team_fight_started": "¡Ha comenzado una nueva pelea de equipos! 🆚 Equipo 1: {0} vs Equipo 2: {1} 🏆",
        "mention_duel_opponent": "Por favor, menciona al usuario con el que quieres tener un duelo. ⚔️",
        "duel_started": "¡Un duelo ha comenzado entre @{0} y @{1}! 🤺",
        "provide_achievement_and_user": "Por favor, proporciona un logro y el usuario al que quieres desbloquearlo.",
        "achievement_already_unlocked": "El logro '{1}' ya ha sido desbloqueado por @{0}.",
        "achievement_unlocked": "¡Felicidades, @{0} ha desbloqueado el logro '{1}'! 🎉"
    }
}

def get_translation(key, chat_id, *args):
    """Get the translation for the given key and chat ID."""
    lang = "en"  # Default language
    if str(chat_id) in translations:
        lang = str(chat_id)
    
    translation = translations[lang].get(key, key)
    return translation.format(*args)
