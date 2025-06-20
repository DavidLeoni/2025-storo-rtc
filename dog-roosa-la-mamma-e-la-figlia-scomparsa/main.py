from turtleps import *

sfondo1 = "bg-snow-mountain-1.gif"
sfondo2 = "bg-archipelago-1.gif"

pers1 = "ch-paladin-e.gif"
pers2 = "ch-village-girl-e.gif"
pers3 = "ch-arctic-kid-e.gif"
pers4 = "ch-village-aunt-e.gif"
pers5 = "ch-yeti-2e.gif"
pers6 = "ch-dragon-e.gif"
food1 = "fd-ice-cream-1f.gif" 
monster1 = "ch-dragon-e.gif"
screen = Screen()
screen.bgpic(sfondo1)
screen.register_shape(pers1)
screen.register_shape(pers4)
screen.register_shape(pers2)
screen.register_shape(monster1)


await ge_init()
await asyncio.sleep(1)

candy = Sprite()
candy.shape(pers1)
  
#giuseppo = Sprite () 
#giuseppo.shape(monster1)
#giuseppo.goto(-100,-100)

stella = Sprite()
stella.shape(pers2)

stella.goto(100,0)

await candy.say("ciao,che cosa succede?",2,dy=80)
await stella.say("sono scomparsa dalla mia mamma",2,dy=80)
await candy.say("ti posso aiutare!",2,dy=80)
await stella.say("davvero!",2)
await candy.say("conosco la tua mamma e sò dove abita",2,dy=80)
await stella.say("siiii!",2)


screen.bgpic(sfondo2)


sara = Sprite()
sara.shape(pers4)
sara.goto(-100,0)
await candy.say("eccola",4,dy=80)
await stella.say("ciao mamma",4,dy=80)
await sara.say("ciao, non ti trovavo a casa",2, dy=80) 
await sara.say("e ti ho cercato per tutta la città",4, dy=80)


#async def click_giuseppo(evento):
#  await giuseppo.say("bbbrrrrr",2)  
#  await giuseppo.say("ciao",2)
#  await giuseppo.say("siete in guai!",2)

            
            
            
            
            
          
          
          
    
