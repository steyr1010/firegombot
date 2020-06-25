import discord
import os
from configparser import ConfigParser
from discord.ext import commands, tasks
from itertools import cycle




config = ConfigParser()
config.read('config.ini', encoding="utf8")
prefix = config["setting"]["prefix"]
sangte = config["setting"]["sangte"]


status = cycle([f'{prefix}도움', sangte])


client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

 
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print('Discord.py 버전 : ' + discord.__version__)
    print("bot starting..")#봇 시작이라고 뜨게하기
    print("==========")
    guilds_count = len(client.guilds)
    members_count = 0

    for guild in client.guilds:
        members_count += len(guild.members)
    print("서버 수: " + str(guilds_count))
    print("멤버 수: " + str(members_count))
    change_status.start()




@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))




aceess_token = os.environ["BOT_TOKEN"]
client.run(access_token)
