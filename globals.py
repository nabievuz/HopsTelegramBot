# GLOBALS.py - no joke, it is just a bunch of global variables

import telebot
dev = 197789555  # replace this with your ID, it is my ID (@FutureDreams)
bot_id = 1028934729  # replace this with your bot's ID, this is actually @Hopsrobot's ID
python_uz = -1001416540983  # this is the ID of our Python UZBEKISTAN group: @python_uz
test_group = -1001301145779  # this is the ID of private tet group, change it to yours
allowed_groups = [python_uz, test_group, -1001416540983, -1001301145779]  # modify this to allow groups
verified = [dev]  # modify this to add verified accounts, verified accounts won't get banned or restricted
should_log = True  # set it to False, and log function doesn't work
botlink = 'foodblogrobot'  # if your bot is @wonerbot, just write 'wonderbot'
token = "1028934729:AAHcGBQbAywIOPIAYOSmloIc0QGb_oSKM_k"  # this is your bot's token which you can get from @Botfather
telegraph_token = 'zXofNqn8yL8AM8DKpiLZoHQ6HQwbU4Mt1aGMy4U5N1'  # your Telegraph accounts' token, Google it to get more info
bot = telebot.TeleBot(token)  # single instance of bot
