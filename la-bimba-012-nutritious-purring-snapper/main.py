from turtleps import *

sfondo1 = "peschereccio.jpg"
sfondo2 = "d55427a4-f7c5-4206-936a-5e1f40bc62cc.image.png"

pers1 = "ch-alien-1eb.gif"
pers2 = "ch-archeologist-e.gif"

screen = Screen()
screen.bgpic(sfondo1)
screen.register_shape(pers1)
screen.register_shape(pers2)

await ge_init()


isabella = Sprite()
isabella.shape(pers1)

tiffany = Sprite()
tiffany.shape(pers2)

isabella.goto(100, 0)
tiffany.goto(-100, 0)


await tiffany.say("Ciao" , 3, dy=80)
await isabella.say("Ciao! Come ti chiami?", 3, dy=80)
await tiffany.say("Tiffany, e tu?", 3, dy=80)
await isabella.say("Io Isabella!", 3, dy=80)
await tiffany.say("Perfetto! Preparati che andiamo sulla lunaaaa", 3,dy=80)

await isabella.slide(0, 250, 3)
await tiffany.slide(0, 250, 3)

screen = Screen()
screen.bgpic(sfondo2)
screen.register_shape(pers1)
screen.register_shape(pers2)

await ge_init()

isabella = Sprite()
isabella.shape(pers1)

tiffany = Sprite()
tiffany.shape(pers2)

isabella.goto(100, 0)
tiffany.goto(-100, 0)

await isabella.say("Perfetto, siamo arrivati!", 3, dy=80)
await tiffany.say("Che bella vista si vede da quassù!", 3, dy=80)
await isabella.say("Si, lo so. Ogni persona che conosco ama questo posto", 3, dy=80)

await isabella.slide(0, -250, 2)
await tiffany.slide(0, -250, 2)




