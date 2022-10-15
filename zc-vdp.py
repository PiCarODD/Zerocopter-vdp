from urllib import response
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
import time

url = "https://www.zerocopter.com/cvd-programs"
webhookurl = "Put your webhook URL" ##webhook url

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
programs = soup.find_all(class_="heading-51")
for program in programs:
    vdp = program.text.strip()
    try:
        f = open("programs.txt", "r",encoding="utf-8")
    except:
        f = open('programs.txt','w+',encoding="utf-8")
    if vdp not in f.read():
        webhook = DiscordWebhook(url=webhookurl, content='New VDP program in ZC - '+vdp)
        time.sleep(2) #rate limit
        response = webhook.execute()
        f2 = open('programs.txt','a',encoding="utf-8")
        f2.write(vdp+"\n")



