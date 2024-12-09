import discord
import os
import BDD
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # Load the commands
    for filename in os.listdir('./BotCommands'):
        if filename.endswith('.py'):
            await bot.load_extension(f"BotCommands.{filename[:-3]}")
            print(f'Loaded : {filename}')
    print(f'Bot connected as : {bot.user}')


# Start the bot
if __name__ == "__main__":
    import config
    #BDD.add_conversation("<@>", "", "")  <- for inserting manualing people inside the db, use their id
    bot.run(config.APIKEY)
