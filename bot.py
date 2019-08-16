import discord
from discord.ext import commands
import asyncio
import time

client = discord.Client()

@client.event
async def on_ready():
	print("logging in")
	print("loading logs")
	print("logged in")
	
client.run()	
