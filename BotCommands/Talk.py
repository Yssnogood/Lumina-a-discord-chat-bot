import discord
import ollama
import BDD
from discord.ext import commands

class Talk(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='t', help='Let you speak with Lumina')
    async def Talk(self, ctx, args):

        user_name = ctx.author.mention
        history = formatMemory(user_name)
        history.append({'role':'user', 'content': args})
        print(args)
        print(history)

        stream = ollama.chat(
        model='Lumina-llama',
        messages=history,
        stream=True
        )

        answer=''
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            answer+=chunk['message']['content']


        BDD.add_conversation(user_name, args, answer)

        print(answer)
        print('Lumina has spoken')
        if len(answer)>2000:
            await ctx.send(f" {answer[0:1999]}")
            await ctx.send(f" {answer[1999:]}")
            return
        await ctx.send(f" {answer}")

async def setup(bot):
    await bot.add_cog(Talk(bot))


def formatMemory(user):

    memory = BDD.get_all_conversation(user)
    messages = []

    for i in range (len(memory)):
        messages.append({"role":"user","content":memory[i][2]})
        messages.append({"role":"assistant","content":memory[i][3]})

    return messages