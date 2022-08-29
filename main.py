import patoolib
import time
import discord
from discord import *
import requests
from datetime import datetime
import os
asd = 1
while(True):
    time.sleep(60)
    os.remove(f"{asd}.rar")
    patoolib.create_archive(f"{asd}.rar", ("save",))
    webhook = Webhook.from_url('YOUR_WEBHOOK_ID', adapter=RequestsWebhookAdapter())
    with open(file=f'{asd}.rar', mode='rb') as f: 
        my_file = discord.File(f)
        webhook.send(f'{datetime.now()}', username='webhook', file=my_file)