import discord
import random
from discord.ext import commands, tasks
import datetime
import os
import time
from discord import message
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('.env')



client = commands.Bot(command_prefix="-")
client = discord.Client()

target_channel_id = '#mine-field'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = 'I\'m the human form of the 💯 emoji.'
        await message.channel.send(response)

    if message.content.startswith('Kon\'nichiwa'):
        await message.channel.send('Kon\'nichiwa')

    if message.content.startswith('Ohaiyo'):
        await message.channel.send('Ohaiyogozaimasu')

    if message.content.startswith('Konbanwa'):
        await message.channel.send('Konbanwa')


@client.event

async def on_ready():

    print("Bot is ready")

    print("checking time...")

    while True:# this is for the time checker

        time = datetime.datetime.today() # this line of code should be looped to update the time continuously

        if time.hour == 7:
            if time.minute == 00:
                if time.second == 1:
                    await client.get_channel(559631764415578114).send(f"Ohaiyogozaimasu!")# The discord bot here comes and grabs the channel id and sends a random message of yours!
                    # break

    while True:

        time = datetime.datetime.today()

        if time.hour == 12:

            if time.minute == 00:

                if time.minute == 1:
                    await client.get_channel(559631764415578114).send(f"Kon\'nichiwa")
                    # break


    while True:
    
        time = datetime.datetime.today()

        if time.hour == 17:

            if time.minute == 00:

                if time.minute == 1:
                    await client.get_channel(559631764415578114).send(f"Konbanwa")

client.run('ODQxNjQ5MjE2OTU3ODQxNDA4.YJp06g.fNaIB2fSaLm1V9Gtc7cVt7Sr2RU')