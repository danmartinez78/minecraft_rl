from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')
mineflayerViewer = require('prismarine-viewer').mineflayer

def connect(BOT_USERNAME):
  bot = mineflayer.createBot({ 'host': '192.168.0.229', 'port': 25566, 'username': BOT_USERNAME, 'hideErrors': False })

  @On(bot, 'spawn')
  def onspawn(*a):
    mineflayerViewer(bot, { 'output': '127.0.0.1:25567', 'width': 512, 'height': 512, 'firstPerson': True, 'port': 25568 })
    print('server started on *:25567')

  return bot