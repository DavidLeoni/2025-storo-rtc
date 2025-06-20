from turtleps import *
sfondo1 = "snow%20mountain.gif"
screen = Screen()
pers1 = "Alex.gif"
pers2 = "sophia.gif"

screen.bgpic(sfondo1)
screen.register_shape(pers1)
screen.register_shape(pers2)

await ge_init()

alex = Sprite()
alex.shape(pers1)

sophia = Sprite()
sophia.shape(pers2)

print("prova")

alex.goto(50,0)
sophia.goto(-50,0)

alex.shapesize(-1.0,1.0)

await alex.say("qui c'è molto freddo" , 3, dx=60             )
