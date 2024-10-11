import discord

# Fungsi untuk mengatur aktivitas dan status bot
async def set_activity(bot, config):
    activity_type = config['activity']['type']
    activity_name = config['activity']['name']

    # Menentukan aktivitas bot berdasarkan config
    if activity_type == 'playing':
        activity = discord.Game(name=activity_name)
    elif activity_type == 'streaming':
        activity = discord.Streaming(name=activity_name, url="http://twitch.tv/streamer")  # URL streaming
    elif activity_type == 'watching':
        activity = discord.Activity(type=discord.ActivityType.watching, name=activity_name)
    elif activity_type == 'listening':
        activity = discord.Activity(type=discord.ActivityType.listening, name=activity_name)
    else:
        raise ValueError(f"Invalid activity type: {activity_type}")

    # Mengganti status bot
    await bot.change_presence(activity=activity)