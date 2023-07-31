import discord
from discord.ext import commands
from pathlib import Path
from discord import app_commands
import json
import os
import time
import random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@client.event
async def on_ready():
    print(f'a facut boot botu')
    await tree.sync(guild=discord.Object(id=932627128997007430))
    print('au mers comenzi')
@client.event
async def on_member_join(member):
    channel = client.get_channel(993835995990597663)
    await channel.send("buna " + str(member) + " si bine ai venit la cel mai pro server😎😎😎😎 (um defapt🤓)")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(993835995990597663)
    await channel.send(str(member) + " a plecat mai rapid decat taicasu lui")

@client.event
async def on_message(message):
    if(message.author.id == client.user.id):
        return
    else:
        leveledup = False
        backdir = os.getcwd()
        serverid = str(message.guild.id)
        author = str(message.author.id)
        os.chdir('levels')
        if(os.path.isfile(f"{serverid}.json") == False):
            open(f"{serverid}.json", "a")
            with open(f"{serverid}.json", "w") as file:
                appenddict = {
                    author:{
                    "xp": 0,
                    "levels": 0,
                    "neededxp": 100,
                    "multiplier": 1,
                    "timestamp": int(time.time())
                    }
                }
                json.dump(appenddict, file, indent=4)
        else:
            with open(f"{serverid}.json", "r") as file:
                data = json.load(file)
            if(not str(author) in data):
                appenddict = {
                    author:{
                        "xp": 0,
                        "levels": 0,
                        "neededxp": 100,
                        "multiplier": 1,
                        "timestamp": int(time.time())
                    }
                }
                data.update(appenddict)
                with open(f"{serverid}.json", "w") as file:
                    json.dump(data, file, indent=4)
        if(author in data):
            userdata = data[author]
            xp = userdata.get("xp")
            levels = userdata.get("levels")
            neededxp = userdata.get("neededxp")
            multiplier = userdata.get("multiplier")
            timestamp = userdata.get("timestamp")
            if ((timestamp + 20) <= int(time.time())):
                xpprimit = random.randint(20,30)
                xpprimit = xpprimit * multiplier
                xp += xpprimit
                if(xp >= neededxp):
                    xp = 0
                    neededxp = int(neededxp * 1.05)
                    levels += 1
                    leveledup = True
                timestamp = int(time.time())
                newdict = {
                    author:{
                        "xp": xp,
                        "levels": levels,
                        "neededxp": neededxp,
                        "multiplier": multiplier,
                        "timestamp": timestamp
                    }
                }
                data.update(newdict)
                with open(f"{serverid}.json", "w") as file:
                    json.dump(data, file, indent=4)
                    os.chdir(backdir)
        if(leveledup == True):
            channel = client.get_channel(1127958512799068220)
            await channel.send(f"hei, {message.author.mention}, ai levl {levels}🤓🤑  ")
        os.chdir(backdir)
        if(message.channel.id == 1126077966812709025):
            if message.author == client.user:
                return
            channel = client.get_channel(1126077966812709025)
            await channel.send('我名字叫 rares nicolas，你名字叫 edi。我的电话号码是0757489037，你的电话号码是  0742445235! 我是罗马尼亚人，你也是罗马尼亚人。很高兴认识你，edi. \n 我吃饭 和喝水，我也吃饭 和不喝水！我很高兴😊，你也很高兴？')
        
        

@tree.command(name = "macac", description = "rares se caca", guild=discord.Object(id=932627128997007430))
async def macac(interaction):
    await interaction.response.send_message("ma cac tare!")


@tree.command(name = "8bile", description = "8ball de buget", guild=discord.Object(id=932627128997007430))
@app_commands.describe(intrebare='intrebare care sa pui')
async def _8ball(interaction, intrebare:str):
    possibilities =  [
        "nu",
        "da",
        "probabil ca da",
        "probabil ca nu",
        "cred", 
        "nu cred",
        "bineinteles ca da",
        "bineinteles ca nu"
    ]
    
    response = random.choice(possibilities)
    await interaction.response.send_message(response)

@tree.command(name = "leaderboard", description = "arata leaderboard 🤓", guild=discord.Object(id=932627128997007430))
async def leaderboard(interaction):
    backdir = os.getcwd()
    i = 0
    field = f"**this is the leaderboard of {interaction.guild}** \n "
    serverid = interaction.guild.id
    with open(f"levels\{serverid}.json", "r") as file:
        dictdata = json.load(file)
        embed = discord.Embed(title=None)
        embed.color = discord.Color.blue()
        embed.set_thumbnail(url=interaction.guild.icon)
        data = dict(sorted(dictdata.items(), key=lambda item: (item[1]['levels'], item[1]['xp']), reverse=True))
        for keys in data.keys():
            name = await client.fetch_user(keys)
            field = field +  f"`{name}`: "

            userdata = data[keys]
            levels = userdata.get("levels")
            xp = userdata.get("xp")
            neededxp = userdata.get("neededxp")
            field = field + f"level {levels}, xp {xp} / {neededxp} \n "
            if(i == 10):
                i = 0
                field = field + "more..."
                break
            else:
                i += 1
        embed.add_field(name="Leaderboard", value=field)

    os.chdir(backdir)
    await interaction.response.send_message(embed=embed)

   
client.run('MTEyNjA4MTU5ODE5MDc4MDQ2OA.GE2evm.nWFG84aG5s5XQrOcyANYuKq4eQtKFCOhnw0I4Y')


