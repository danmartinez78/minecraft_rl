from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
mineflayerViewer = require('prismarine-viewer').mineflayer



random_number = id([]) % 1000 # Give us a random number upto 1000
BOT_USERNAME = f'colab_{random_number}'



bot = mineflayer.createBot({ 'host': '192.168.0.229', 'port': 25566, 'username': BOT_USERNAME, 'hideErrors': False })

@On(bot, 'spawn')
def onspawn(*a):
    mineflayerViewer(bot, { 'firstPerson': True, 'port': 25567 })
    print('server started on *:25567')

