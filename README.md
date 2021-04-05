# Sleepy Maid
Based on [discord_bot.py](https://github.com/AlexFlipnote/discord_bot.py) by [AlexFlipnote](https://github.com/AlexFlipnote). This is a utility bot made for some of my server ans other server I like. I will not provide any support on hosting this bot because this is made for specific server.


## Useful to always have
Keep [this](https://discordpy.readthedocs.io/en/latest/) saved somewhere, as this is the docs to discord.py@rewrite.
All you need to know about the library is defined inside here, even code that I don't use in this example is here.

## Optional tools
### PM2
PM2 is an alternative script provided by NodeJS, which will reboot your bot whenever it crashes and keep it up with a nice status. You can install it by doing `npm install -g pm2` and you should be done. Keep in mind that this PM2 file is made to work on my own Linux instance, you might need to change the `interpreter` value.
```
# Start the bot
pm2 start pm2.json

# Tips on common commands
pm2 <command> [name]
  start sleepymaid    Run the bot again if it's offline
  list                Get a full list of all available services
  stop sleepymaid     Stop the bot
  reboot sleepymaid   Reboot the bot
```
