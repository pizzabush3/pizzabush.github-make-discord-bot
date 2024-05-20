# Instructions  

## Step 1: Setup

1. [Create a bot in discord and get a token](https://docs.replit.com/tutorials/python/build-basic-discord-bot-python#creating-a-bot-in-discord-and-getting-a-token)
2. [Set ALL permissions to ON](https://docs.replit.com/tutorials/python/build-basic-discord-bot-python#privileged-gateway-intents)
3. [Add your bot to the server](https://docs.replit.com/tutorials/python/build-basic-discord-bot-python#adding-your-discord-bot-to-your-discord-server)
4. Make a channel for your bot
5. Add your bot to your bot channel

## Step 2: Programming

Modify the two functions in `my_bot.py`.

The `should_i_respond` function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users

The `respond` function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
