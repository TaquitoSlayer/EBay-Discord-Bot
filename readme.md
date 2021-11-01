# CheckAFlip Discord Bot

BIG NOTE: there is now a 60 second delay that the developer of CheckAFlip has imposed. to respect him, i won't be adding a bypass to this dude to it being a free service and im basically piggybacking from it with this. go donate to them to their respective outlets.

This is pretty straight forward and EXTREMELY simple script - use ".ebay keyword" to find a product's average active selling price on Ebay.com along with it's completed/sold item pricing.

This uses the [CheckAFlip](http://www.checkaflip.com/) API which is actually pretty great in terms of ease of use, and would recommend taking a look at them and the API endpoints used if you want to expand this any further.

Follow me on [Twitter](https://twitter.com/taquitoslayer)

![FunkoFuckedTookStock](https://i.imgur.com/hfgacKK.png)

If you do decide to use this on your Discord server, I request that you don't remove my name from the script itself :) It helps others for support when adding it to their server! Also, the clout. The fucking clout.

### How to install and use
1. Make sure you install [Python3.6.6 (anything higher isn't currently supported by the discord module)](https://www.python.org/getit/) and [pip](https://pip.pypa.io/en/stable/installing/) followed by running the following in the same directory as checkflip.py
```bash
pip install -r requirements.txt
```
2. Get your Discord server [token](https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord) and set permissions while you're at it
3. Use your favorite text editor to add the token to the script
4. Run script
```bash
python checkaflip.py
```

## Thanks to
* [discord.py](https://github.com/Rapptz/discord.py) for it's amazing flexibility
* [idontcop](https://twitter.com/idontcop) for being my partner in crime the past couple years

## Future features:
* Use bot.commands so that you can extend the use of it to multiple sources - thanks to idontcop for this suggestion
