from turtleps import *

sfondo1 = "bg-country.gif"
sfondo2 = "bg-forest-1.gif"

pers1 = "ch-village-girl-e.gif"
pers2 = "ch-bar-owner-e.gif"
pers3 = "d615e4f8-1a23-489b-84f8-1ad991995faf.image.png"

screen = Screen()
screen.bgpic(sfondo1)
screen.register_shape(pers1)
screen.register_shape(pers2)

await ge_init()
await asyncio.sleep (1)

jen = Sprite ()
jen.shape(pers1)

bob = Sprite ()
bob.shape(pers2)

jen.goto(60, -100)
bob.goto(100, -100)

await jen.say ("Ciao!", 3)
await bob.say ("Ciao, come stai?", 3)
await jen.say ("Bene, andiamo a fare una passeggiata?", 3)
await bob.say ("Si!", 3)
 
await asyncio.gather(jen.slide (220, -100, 3),
               bob.slide (220, -100, 2) )

screen = Screen()
screen.bgpic(sfondo2)
screen.register_shape(pers1)
screen.register_shape(pers2)
screen.register_shape(pers3)

await asyncio.sleep (2)

alien = Sprite()
alien.shape(pers3)


jen.goto(-220, -10)
bob.goto(-220, -10)
alien.goto(180, 180)

await asyncio.gather (jen.slide (5, -10, 3),
                    bob.slide (0, -10, 2) )
