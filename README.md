# **Telegram to Discord Bridge**


<p align="center">
  <a href="https://telegram.org/" target="blank">
    <img src="https://cdn.worldvectorlogo.com/logos/telegram-1.svg" width="200" alt="NextJS Logo" />
  </a>
  &emsp;
  <a href="https://discord.com/" target="blank">
    <img src="https://cdn.worldvectorlogo.com/logos/discord.svg" width="175" alt="NextJS Logo" />
  </a>
</p>

## Welcome to [Telegram to Discord message forwarder](https://github.com/RedSocks25/Telegram-to-Discord-Bridge). 

This bot is coded in the way that let the user catch messages for any chat where the bot is integrated and redirect all the new messages to any and multiple Discord Servers you want.

The code can serve multi purpose tasks, since is a bridge between Telegram and Discord. So if you want to add new functionalities, just change the code you need. For now is a message forwarder. For you? Could be something else.

# Dependencies
### Before installing the project, ensure that you have pip updated
```bash
python -m pip install --upgrade pip
```

There are to libraries needed for Python in order to run this bot
* `python-telegram-bot` (v 20.3)
```bash
pip install python-telegram-bot==20.3
```
* `discord.py` (v 2.2.3)
```bash
pip install discord.py==2.2.3
```

# Deploy the project

After installing the dependencies needed, you need to add a `.env` file on the root of the project to securely store the keys needed.

Inside of the project you will find a `.env.template` with all the needed variables defined but not assigned. Just gather each of one and delete the `.template` extension from the `.env.template` file.