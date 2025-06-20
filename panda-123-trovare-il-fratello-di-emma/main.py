from turtleps import *
import asyncio

sfondo1 = "black%20citty.gif"
sfondo2 = "bg-jungle-1.gif"

pers1 = "girl-from-the-village.gif"

pers2 = "lamica.gif"
pers3 = "lamicas%20brother.gif"

screen = Screen()
screen.bgpic(sfondo1)
screen.register_shape(pers1) 
screen.register_shape(pers2)
screen.register_shape(pers3)


await ge_init()
await asyncio.sleep(1)

rose = Sprite() 
rose.shape(pers1)

emma = Sprite()
emma.shape(pers2)

max = Sprite()
max.shape(pers3)

print("prova")

emma.goto(0, -100)
rose.goto(-40,-90)

emma.shapesize(-1.0,1.0)

await emma.say("Dov'è andato il mio fratello?", 3, dx=60, dy=60)
await rose.say("Non lo so", 3, dx=10, dy=60)
await emma.say("La mia mamma mi ucciderà se scopre", 3, dx=60, dy=60)
await emma.say("che ho perso il mio fratello!", 3, dx=60, dy=60)
await rose.say("Lo so. Ma non preoccuparti, ti aiuto a cercarlo", 3, dx=10, dy=60)
await emma.say("Veramente?", 3, dx=60, dy=60)
await rose.say("Sì", 3, dx=10, dy=60)
await emma.say("grazie!", 3, dx=60, dy=60)
await rose.say ("prego", 3, dx=10, dy=60)




emma.shapesize(1.0, 1.0)

await emma.slide(250, 90, 3)
await rose.slide(250, 90, 3)
await asyncio.gather(emma.slide(-10, -90, 1),
                     rose.slide(40, -80, 1))
screen.bgpic(sfondo2)
