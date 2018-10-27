import discord
from discord.ext.commands import Bot

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("!zodbot"):
        await client.send_message(message.channel, "```Whats up?```")
    elif message.content.startswith("!traya"):
        await client.send_message(message.channel, "```Revan lead jedi\nCLS Chew\nStrong zkru FO\nMagma under Thrawn lead\nzBastila with DN```")
    elif message.content.startswith("!revan"):
        await client.send_message(message.channel, "```Zaul & Slow Nest with high tenacity\nTarkin lead fast Thrawn \nTraya & fast Thrawn\nNS & zBarris```")
    elif message.content.startswith("!cls"):
        await client.send_message(message.channel, "```Rex & Wampa \nNightsisters \nEwoks\nTraya\nBastila\nGK & zBarris ```")
    elif message.content.startswith("!bastila"):
        await client.send_message(message.channel, "```JTR\nQira lead beffed Nest\nzMT lead NS\nStrong zKru lead FO\nThrawn lead Range, DT, Shore\nzBossk```")
    elif message.content.startswith("!palp"):
        await client.send_message(message.channel, "```**Without Traya**\nzBastila or zGmy lead jedi\nCLS\nRex lead Wampa, Visas\nNightsisters\n\n**With Traya**\nzBastila with DN\nzFinn resistance with fast Enfys\nCLS Chew\nRex lead DT, DN, CLS, Thrawn```")
    elif message.content.startswith("!jtr"):
        await client.send_message(message.channel, "```Nightsister\n```")
    elif message.content.startswith("!gk"):
        await client.send_message(message.channel, "```JTR\nCLS Chew```")
    elif message.content.startswith("!bossk"):
        await client.send_message(message.channel, "```zBastila lead jedi\nzKru lead FO\nzPalp lead sith/empire ```")
    elif message.content.startswith("!kru"):
        await client.send_message(message.channel, "```JTR\nCLS\nNightsisters\nzFinn with sidious(healing immunity)```")
    elif message.content.startswith("!qira"):
        await client.send_message(message.channel, "```CLS Chew\nJTR\nDroids```")
    elif message.content.startswith("!ns"):
        await client.send_message(message.channel, "```Imperial Troopers\nzBastila lead jedi\nCLS Chew\nPhoenix\nzBossk lead BH```")

    elif message.content.startswith("!zaul"):
        await client.send_message(message.channel, "```CLS lead, R2, Han Solo\n Yoda or Bastila lead Jedi\nFirst Order\nBounty Hunters```")
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTA1NzczODA5MDUyMTU1OTE3.DrYknw.820AigRbMO31U45FJXCjxmJekdw')
