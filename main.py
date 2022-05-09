import time # I use this module for the time.sleep() function
from nextcord import Interaction, SlashOption, ChannelType # This is required for application commands
from nextcord.abc import GuildChannel # This is required for application commands
from nextcord.ext import commands # This is for commands
from nextcord.utils import get
import nextcord # Imports the API thingy
import json
import os
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": ""}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

TOKEN = configData["Token"]

bot = commands.Bot(command_prefix=['tun!', 'Tun!', 'TUN!', '<@961323166158970880> ']) # Sets the prefix
mainServerID = 960634206835343401

@bot.event # This event prints in the console when the bot has logged in
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def gawguide(ctx):
    await ctx.channel.purge(limit=1)
    embed = nextcord.Embed(title="❓ How to donate to a giveaway! 🎉", description="👋 To donate to a Dank Memer giveaway, simply type `/donate-giveaway` and select the option from <@961323166158970880>. The prompts should guide you through the process!", color= nextcord.Color.green())
    embed.add_field(name= "🎉 The donation rules", value= "<a:rightarrow:971487442161000448> Giveaway prize must be worth 100k or more *per winner*\n<a:rightarrow:971487442161000448> You must respect our Giveaway Managers\n<a:rightarrow:971487442161000448> Giveaways cannot have more than 30 winners\n<a:rightarrow:971487442161000448> Giveaways should not last more than 2 weeks and should be longer than 10 seconds\n<a:rightarrow:971487442161000448> Giveaway message must follow all of the server's rules, and shouldn't promote anything or be troubling for other users\n<a:rightarrow:971487442161000448> Giveaway requirements must be reasonable\n<a:rightarrow:971487442161000448> **Our Giveaway Managers have every right to deny hosting your giveaway**")
    embed.set_footer(text= "❤️ Thank you for donating!")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/961295711041884242/961467821060132884/Discord_Server_Logo_Attempt_1_1.png")
    await ctx.send(embed=embed)

@bot.command() # Command to see the bot's ping in an embed
async def ping(ctx):
    embed = nextcord.Embed(title="Pong! 🏓", description=f"{round(bot.latency * 1000, 1)}ms", color=nextcord.Color.green())
    await ctx.reply(embed=embed)

@bot.command()
async def timer(ctx, duration: int, unit: str="m"):
    if unit == "s":
        timeInSeconds = duration
    elif unit == "m":
        timeInSeconds = duration * 60
    elif unit == "h":
        timeInSeconds = duration * 60 * 60
    elif unit == "d":
        timeInSeconds = duration * 60 * 60 * 24
    elif unit == "w":
        timeInSeconds = duration * 60 * 60 * 24 * 7
    elif unit == "mo":
        timeInSeconds = duration * 60 * 60 * 24 * 30
    elif unit == "y":
        timeInSeconds = duration * 60 * 60 * 24 * 365
    embed = nextcord.Embed(title= "⏲️ Timer!", description= f"You have set a timer for {duration}{unit}!", color= nextcord.Color.green())
    embed.set_footer(text=f"{ctx.message.author}")
    await ctx.reply(embed=embed)
    time.sleep(timeInSeconds)
    await ctx.send(f"<@{ctx.message.author.id}>, your timer has ended!")

@commands.has_permissions(manage_channels= True)
@bot.command(aliases = ["pu", "clear", "delete"]) # Purge command
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"✅ Successfully purged {amount} messages!", delete_after=(5))

@bot.command() # Owner only command to change the bot's status on discord
async def status(ctx, type, statusmessage: str="default"):
    if ctx.message.author.id == 688330308688543744:
        if statusmessage == "default":
            await bot.change_presence(status=nextcord.Status(type), activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"a dank memer server"))
            await ctx.reply(f"✅ Successfully changed status to **{type}** with **default message**!")
        elif statusmessage == "none":
            activity = nextcord.Game(name=statusmessage)
            await bot.change_presence(status=nextcord.Status(type), activity=None)
            await ctx.reply(f"✅ Successfully changed status to **{type}** with **no message!**")
        elif statusmessage != "default" and statusmessage != "none":
            activity = nextcord.Game(name=statusmessage)
            await bot.change_presence(status=nextcord.Status(type), activity=activity)
            await ctx.reply(f"✅ Successfully changed status to **{type}** with message **{statusmessage}**!")
    else:
        await ctx.reply(":x: This is an owner only command!")

@bot.slash_command(name="donate-giveaway", description="Donate to a Dank Memer giveaway!", guild_ids=[mainServerID])
async def gawdono(interaction:Interaction, duration:str, winners:int, requirements:str, prize:str, message:str, not_claimed_action:str):
    embed = nextcord.Embed(color= nextcord.Color.green(), title= "🎉 Giveaway donation!", description= f"**Time:** {duration}\n**Winners:** {winners}\n**Requirements:** {requirements}\n**Prize:** {prize}\n**Message:** {message}\n**Not claimed action:** {not_claimed_action}")
    embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/961295711041884242/961467821060132884/Discord_Server_Logo_Attempt_1_1.png")
    embed.set_footer(text= f"{interaction.user}", icon_url= f"{interaction.user.avatar}")
    pingManagers = nextcord.AllowedMentions(roles=True)
    await interaction.response.send_message("<@&961386803754061844>", embed=embed, allowed_mentions=pingManagers)


bot.run(TOKEN) # Runs the bot