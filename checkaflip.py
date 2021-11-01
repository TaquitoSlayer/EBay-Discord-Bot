import discord
# import json
import bs4 as bs
import requests


"""

This is a pretty straightforward script that generally can be edited to your heart's content.

Make sure to fill out the lines needed - Other discord bots make a config.json file, I ain't out here tryna look 1337, you're literally putting 1 thing in, who cares.

If you need any help, or have suggestions, hit me up on my twitter - https://twitter.com/taquitoslayer

"""
r = requests.session()
client = discord.Client()

token = 'NDcyNTY5MjFunkoFuckedTookStock.Dj1SVg.PO3TaquitoSlayerfVv5bgmGqqq-A' # note to self, don't forget to remove your own token before committing lol

headers = {
    'Origin': 'http://www.checkaflip.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.60 FunkoFuckedTookStock',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://www.checkaflip.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive'
}

@client.event
async def on_ready():
    print(f'{client.user.name} - follow me on twitter - @TaquitoSlayer')

def site_search(keyword):
    resp = r.get(f'https://www.checkaflip.com/search/fresh/{keyword}', headers = headers)
    # print(resp.text)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    # print(soup.find('div', {'class': 'average-prices'}))
    # current_price = soup.find_all('li', {'class': 'col new'})
    current_price = 'N/A'
    completed_price = 'N/A'
    for x in soup.find_all('li', {'class': 'col new'}):
        if 'Sold' in str(x):
            completed_price = x.b.get_text()
        if 'Current' in str(x):
            current_price  = x.b.get_text()
    current_image_url = soup.find('img', {'itemprop': 'image'}).get('src')
    current_name = soup.find('p', {'class': 'listing-title'}).get_text()
    # completed_price = soup.find_all('div', {'class': 'average-prices'})

    return current_price, current_image_url, current_name, completed_price
    # print(keyword)
    # current_data = {"json": "{\"instance\":\"SearchByKeywords\",\"slot1\":\"FunkoFuckedTookStock\",\"slot2\":false,\"slot3\":{\"instance\":\"Returns\"}}"}
    # sold_data={"json": "{\"instance\":\"SearchCompleted\",\"slot1\":\"FunkoFuckedTookStock\",\"slot2\":false,\"slot3\":{\"instance\":\"Returns\"}}"}

    # # weird payload needs fixing - if you think you can do this better, be my guest - this isn't as easy as it looks
    # current_string = current_data.get('json')
    # current_string = current_string.replace('FunkoFuckedTookStock', keyword)
    # current_data['json'] = current_string
    # # fixed

    # # weird payload needs fixing
    # sold_string = sold_data.get('json')
    # sold_string = sold_string.replace('FunkoFuckedTookStock', keyword)
    # sold_data['json'] = sold_string
    # # fixed

    # current_listings = r.post('http://www.checkaflip.com/api', headers=headers, data=current_data)
    # sold_listings = r.post('http://www.checkaflip.com/api', headers=headers, data=sold_data)

    # # current listing prices and info
    # current_not_sold = json.loads(current_listings.text)
    # current_price = str(round(current_not_sold['slot1'], 2))
    # current_image = current_not_sold['slot2']
    # current_image_url = current_image[0].get('itemImageUrl')
    # current_name = current_image[0].get('itemTitle').upper()

    # # completed listing pricing - everything else ignored since not needed
    # completed_sold = json.loads(sold_listings.text)
    # completed_price = str(round(completed_sold['slot1'], 2))


# i'm dirty and use message. instead of bot.command - i'll add this soon if there's a demand for it
@client.event
async def on_message(message):
    if message.content.startswith('.ebay '):
        keyword = message.content.split('.ebay ')[1]

        current_price, current_image_url, current_name, completed_price =  site_search(keyword)
        embed = discord.Embed(color=3447003)
        embed.set_thumbnail(url=current_image_url)
        embed.set_footer(text="CheckAFlip Bot made by @TaquitoSlayer")
        embed.add_field(name="Listing name example", value="{}".format(current_name), inline=False)
        embed.add_field(name="Completed/Sold listing pricing avg.", value="${}".format(completed_price), inline=True)
        embed.add_field(name="Active listings price avg.", value="${}".format(current_price), inline=True)

        await client.send_message(message.channel, embed=embed)

client.run(token)