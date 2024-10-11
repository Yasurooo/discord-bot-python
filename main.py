import discord
from discord.ext import commands
from config.status import set_activity  # Ensure set_activity is an async function
import logging
import json
import os
import asyncio

# Setup the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Patched to config.json
config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.json')

# Loaded the config.json
with open(config_path) as config_file:
    config = json.load(config_file)

# Intents Permissions
intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents, case_insensitive=True)
bot.remove_command('help')

# Function to load commands from cogs
async def load_cogs():
    for folder in os.listdir('./cogs'):
        folder_path = os.path.join('./cogs', folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith('.py') and filename != '__init__.py':
                    try:
                        logger.info(f"Loading cog: cogs.{folder}.{filename[:-3]}")
                        await bot.load_extension(f'cogs.{folder}.{filename[:-3]}')
                    except Exception as e:
                        logger.error(f"Failed to load cog {filename[:-3]}: {e}")

# Handler Online and syncing Commands               
@bot.event
async def on_ready():
    logger.info(f"Bot is Online")
    try:
        synced = await bot.tree.sync()
        logger.info(f"Successfully added {len(synced)} slash commands")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")

    # Set activity after bot is ready
    await set_activity(bot, config)
    logger.info("Bot is online and ready to assist!")

# Setup the main
async def main():
    logger.info("Starting the bot, please wait")
    await load_cogs()
    try:
        await bot.start(config['token'])
    except Exception as e:
        logger.error(f"Error while running the bot: {e}")

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
