from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')

random_number = id([]) % 1000 # Give us a random number upto 1000
BOT_USERNAME = f'colab_{random_number}'

bot = mineflayer.createBot({ 'host': '192.168.0.229', 'port': 25566, 'username': BOT_USERNAME, 'hideErrors': False })

# The spawn event 
once(bot, 'login')
bot.chat('I spawned')