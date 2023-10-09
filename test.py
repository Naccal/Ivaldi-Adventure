import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

DISCORD_TOKEN = "..."

#bot = commands.Bot(command_prefix="!")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('NCS is ready')

@bot.command()
async def test(ctx, test=str):
  await ctx.send("Fuck off")
  #await message.channel.send(account)


bot.run(DISCORD_TOKEN)