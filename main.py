import os
import asyncio
from dotenv import load_dotenv
import discord
from utils.agent import agent

load_dotenv()

try:
    bot_token = os.environ["DISCORD_TOKEN"]
except KeyError:
    print("Error: DISCORD_TOKEN not found in the environment variables.")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        try:
            print(f"Message from {message.author}: {message.content}")

            async with message.channel.typing():
                # Runs the agent.run() function in a separate thread to prevent blocking
                answer = await asyncio.to_thread(agent.run, message.content)
                await message.channel.send(answer)
        except Exception as e:
            print(f"Error handling message: {e}")
            await message.channel.send(f"Au secours <@364818633668558848> ! Il semblerait que j'ai un problème 😱 Voici le message d'erreur : {e} ")

client.run(bot_token)