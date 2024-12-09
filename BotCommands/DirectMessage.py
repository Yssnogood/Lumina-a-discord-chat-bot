import discord
import asyncio
import random
import ollama
import utils
import BDD
from discord.ext import commands

class DirectMessages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.ping_every_x_seconds())

    # Send message to a random user
    @commands.command(name="senddmTo")
    async def send_dmTo(self, ctx):
        user_list = BDD.get_users()
        user_to_notify = random.choice(user_list)[0]
        history = formatMemory(user_to_notify)
        history.append(utils.get_random_prompt())

        user_to_notify = int(user_to_notify[2:-1])



    async def ping_every_x_seconds(self):

        await self.bot.wait_until_ready()  

        while not self.bot.is_closed():
            try:
                user_list = BDD.get_users()
                user_to_notify = random.choice(user_list)[0]
                history = formatMemory(user_to_notify)
                history.append(utils.get_random_prompt())
                print(history[-1])

                user_to_notify = int(user_to_notify[2:-1])

                print(user_to_notify)
                stream = ollama.chat(
                    model='Lumina-llama',
                    messages=history,
                    stream=True
                )

                answer = ''
                for chunk in stream:
                    answer += chunk['message']['content']

                user = await self.bot.fetch_user(user_to_notify)
                BDD.add_conversation(f"<@{user_to_notify}>", " ", answer)

                if len(answer) > 2000:
                    await user.send(answer[:1999])
                    await user.send(answer[1999:])
                else:
                    await user.send(answer)
            except discord.HTTPException as e:
                print(f"Erreur lors de l'envoi du message : {e}")
            
            timer = random.randint(120,3600)
            print(timer, " or ", timer/60, " minutes ")
            await asyncio.sleep(timer)

    # Command to send a message to all people that interacted with the bot
    @commands.command(name="notifyall")
    async def notify_all(self, ctx):
        users_to_notify = BDD.get_users()
        user_message = utils.get_random_prompt()

        stream = ollama.chat(
            model='Lumina-llama',
            messages=user_message,
            stream=True
        )

        answer = ''
        for chunk in stream:
            answer += chunk['message']['content']

        for user_id in users_to_notify:
            user_id_int = int(user_id[0][2:-1])
            user = await self.bot.fetch_user(user_id_int)
            try:
                await user.send(answer)
            except discord.Forbidden:
                await ctx.send(f"Je ne peux pas envoyer de DM à {user.name}.")
            except discord.HTTPException as e:
                await ctx.send(f"Échec de l'envoi du message à {user.name}. Erreur : {e}")
            BDD.add_conversation(user_id[0], " ", answer)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(DirectMessages(bot))

def formatMemory(user):
    memory = BDD.get_all_conversation(user)
    messages = []

    for entry in memory:
        messages.append({"role": "user", "content": entry[2]})
        messages.append({"role": "assistant", "content": entry[3]})

    return messages
