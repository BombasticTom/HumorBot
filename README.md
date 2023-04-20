# How to run?
You will need to install Python and a module called "discord". Basically, you would have to put the following line in the command prompt:

`pip install discord`

You will also need to make a new `Configuration.py` file in the `sources` folder. You should put in the following:
```py
# A Configuration class specifically made for organizing.
class Configuration:
    # PUT YOUR DISCORD BOT TOKEN HERE!
    TOKEN = 'YOUR-TOKEN-HERE'
```

Once done, you should be good to go. Just run the `main.py` file!

# How to use?

It's simple. Once the bot is online, send a message containing text `@BotName order pizza` (that is the only current feature for now).
