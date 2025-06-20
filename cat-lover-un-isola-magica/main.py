from turtleps import *

sfondo1 = "bg-seaside-2.gif"
sfondo2 = "bg-archipelago-1.gif"
pers1 = "ch-paladin-w.gif"
pers2 = "an-boar-1w.gif"
pers3 = "ch-slime-e.gif"
pers4 = "an-octopus-2f.gif"


screen = Screen()
screen.bgpic(sfondo1)






screen.register_shape(pers1)
await ge_init()
chiara = Sprite()

chiara.shape(pers1)
chiara.goto(100,-100)

screen.register_shape(pers2)
await ge_init()
roccia = Sprite()

roccia.shape(pers2)
roccia.goto (-100,100)
screen.register_shape(pers4)
await ge_init()
gino = Sprite()
gino.shape(pers4)
gino.goto(-150,-150)


await chiara.say("aaa aiutooo un mostro",3, dy=80)
await chiara.say("ti ucciderò con questa spada",3, dy=80)

await roccia.say("noo, non uccidermi non sono cattivo",3, dy=90)
await roccia.say("io sono amichevole",3, dy=90)
await chiara.say("ahh ok pensavo fossi cattivo",3, dy=90)

roccia.goto(100,100)

chiara.goto(-100,100)

await chiara.say("se vuoi possiamo essere amici",3,dy=80)
await roccia.say("ok,va bene...",3, dy=90)



await chiara.say("aahhh cos'è quello?",3,dy=80)

screen.register_shape(pers3)

await ge_init()
slime = Sprite()
slime.shape(pers3)
slime.goto (0,-50)
await roccia.say("tranquilla quello è una gelatina di mare",3, dy=90)
await roccia.say("ci porterà ad esplorare un pò il posto",3, dy=90)

await slime.say("ciao ragazzi!! venite con me",3)
await chiara.say("ok...",3,dy=80)

screen.bgpic(sfondo2)
await slime.slide(250,0)
await chiara.slide(250,0)
await roccia.slide(250,0)
await asyncio.gather(slime.slide(-100, -0, 2),
                     chiara.slide(-100, -0, 2),
                     roccia.slide(-100, -0, 2) )

slime.goto(-100,100)
chiara.goto(100,-100)
roccia.goto(0,0)

await slime.say("eccoci questa è la cascata più bella di tutto il posto",3)
await chiara.say("wow che bello!",3,dy=80)
await roccia.say("bellissimo!",3, dy=90)

async def click_gino(evento):
  await gino.say("blug!",2,dy=50)
  await gino.say("guark",2,dy=50)
  
gino.svg.onclick = click_gino

gino.goto(-100,-100)


