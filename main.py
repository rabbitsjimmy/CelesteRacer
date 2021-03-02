import req as r
from keep_alive import keep_alive

command_list = ['$start']
race_channels = [816220790516613151, 816220819226886166]

@r.client.event
async def on_ready():
  print("We have logged in as {0.user}".format(r.client))

@r.client.event
async def on_message(message):
  if message.author == r.client.user:
    return
  msg = message.content

  if msg.startswith('$start'):
    valid_channel = False
    for channel in race_channels:
      if message.channel == r.client.get_channel(channel):
        valid_channel = True
    if valid_channel:
      await message.channel.send('5')
      await r.asyncio.sleep(1)
      await message.channel.send('4')
      await r.asyncio.sleep(1)
      await message.channel.send('3')
      await r.asyncio.sleep(1)
      await message.channel.send('2')
      await r.asyncio.sleep(1)
      await message.channel.send('1')
      await r.asyncio.sleep(1)
      await message.channel.send('GO')
    else:
      await message.channel.send('Wrong channel, go to a racing channel')


  if msg.startswith('$help'):
    #for cmnd in command_list:
    #  await message.channel.send('cmnd')
    await message.channel.send('Right now $start is the only command, use it to start a 5 second countdown')


keep_alive()
r.client.run(r.os.getenv("TOKEN"))