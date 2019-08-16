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
	
client.run("NjExNDk1MDQyMjA0NDM0NDQy.XVa19Q.JSJ6WzKiTF-s0X7cp1KgTA3btnU")	
