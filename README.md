
## Useful to always have
Keep [this](https://discordpy.readthedocs.io/en/latest/) saved somewhere, as this is the docs to discord.py@rewrite.
All you need to know about the library is defined inside here, even code that I don't use in this example is here.

# Optional tools
### PM2
PM2 is an alternative script provided by NodeJS, which will reboot your bot whenever it crashes and keep it up with a nice status. You can install it by doing `npm install -g pm2` and you should be done. Keep in mind that this PM2 file is made to work on my own Linux instance, you might need to change the `interpreter` value.
```
# Start the bot
pm2 start pm2.json

# Tips on common commands
pm2 <command> [name]
  start discord_bot.py    Run the bot again if it's offline
  list                    Get a full list of all available services
  stop discord_bot.py     Stop the bot
  reboot discord_bot.py   Reboot the bot
```
