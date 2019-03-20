#test
import discord
from bs4 import BeautifulSoup
import requests
from Settings import TOKEN


web_page = "https://minecraft-statistic.net/en/server/158.69.123.42_25565.html"

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    #print("Channel:" + str(message.channel))
    #print("Server:" + str(message.server))
    #print("Message:" + str(message.content))
    #print("Author:" + str(message.author.name))
    if message.author == client.user:
        return

    if message.content.startswith('!stats'): #and str(message.channel) == "Direct Message with lastratalive":

        page_response = requests.get(web_page)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        updated = page_content.find('td', string = 'Updated:').parent.text

        players = page_content.find_all('div', {'class': 'col-md-2 col-sm-4 col-xs-3'})
        playerlist = []
        for player in players:            
            playerlist.append(player.find('a', {'class', 'c-black'}).text)
        msg = str(updated) + "Current Players: "+str(playerlist)  #'Boop {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)