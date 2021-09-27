from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')
mineflayerViewer = require('prismarine-viewer').mineflayer

def connect(BOT_USERNAME):
  bot = mineflayer.createBot({ 'host': '192.168.0.229', 'port': 25566, 'username': BOT_USERNAME, 'hideErrors': False })

  @On(bot, 'spawn')
  def onspawn(*a):
    mineflayerViewer(bot, { 'output': '127.0.0.1:3000', 'frames': -1, 'width': 512, 'height': 512, 'firstPerson': True, 'port': 3000 })
    print('server started on *:3000')

  return bot