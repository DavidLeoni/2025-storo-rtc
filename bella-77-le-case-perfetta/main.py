from turtleps import *

sfondo1 = "bg-hills-2.gif"
sfondo2 = "bg-snow-mountain-1.gif"

pers1 ="ch-wizard-e.gif"
pers2 ="ch-arctic-kid-w.gif"
cibo1 ="fd-ice-cream-1f.gif"
cibo2 ="fd-watermelon2-f.gif"
cibo3 ="fd-taco-f.gif"

screen = Screen()
screen.bgpic(sfondo1)
screen.register_shape(pers1)
screen.register_shape(pers2)
screen.register_shape(cibo1)
screen.register_shape(cibo2)
screen.register_shape(cibo3)

await ge_init()
await asyncio.sleep(1)

nora = Sprite()
nora.shape(pers1)

luk = Sprite()
luk.shape(pers2)

nora.goto(-100, -100)
luk.goto(100, -100)


await nora.say("Ciao!", 2, dy=90)
#await nora.say("ciao !", 3, dx=-100, dy=200)
await luk.say("Hey!", 2)
await luk.say("Come ti chiami? Io Luk.", 2)
await nora.say("Bel nome, io mi chiamo Nora.", 2, dy=90)
await luk.say("È un bel nome da strega!", 4)
await nora.say ("Questa è la mia casa.", 2, dy=90)
await nora.say ("Cosa ne pensi?", 2, dy=90)
await luk.say ("Beh, è carina", 2)
await luk.say ("Ti porto a vedere la mia.", 2)

luk.shapesize(-1.0,1.0)
await luk.slide (250, -100, 2)
await nora.slide (300, -100, 2)

screen.bgpic(sfondo2)

async def pepe():

  luk.shapesize(1.0, 1.0)
  nora.goto(-100, -100)
  luk.goto(100, -100)

  await luk.say("Eccola, è stupenda vero?", 2)
  await nora.say("Wowo, fantastica!", 2, dy=90)
  await luk.say("Cade anche cibo dal cielo!!!", 2)
  await nora.say("No way!", 2, dy=90)

screen.bgpic(sfondo2)

ice=Sprite()
ice.shape(cibo1)

async def sale():
  while True:
    ice.goto(0, 200)
    await ice.slide(0, -250)

melon=Sprite()
melon.shape(cibo2)

async def sugar():
  while True:
    melon.goto(-100, 200)
    await melon.slide(-100, -250)
    
tacos=Sprite()
tacos.shape(cibo3)
    
async def paprica():
  while True:
    tacos.goto(100, 200)
    await tacos.slide(100, -250)
    
async def click_ice(evento):
  await ice.say("Puoi mangiarmi...", 2)
ice.svg.onclick = click_ice

async def click_melon(evento):
  await melon.say("...se riesci...", 2)
melon.svg.onclick = click_melon

async def click_tacos(evento):
  await tacos.say("...a prendermi!", 2)
tacos.svg.onclick = click_tacos



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
await asyncio.gather(pepe(), sale(), sugar(), paprica())






