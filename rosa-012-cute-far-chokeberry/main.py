from turtleps import *
 
sfondo1= "bg-seaside-2.gif"
sfondo2= "spiaggia-media2.png"
sfondo3= "bariera%20corallina%202.png"

pers1 = "ch-village-girl-e.gif"
pers2 = "ch-arctic-kid-e.gif"

screen = Screen()
screen.bgpic(sfondo1)
screen.register_shape(pers1) #comincia a caricare l'immagine
screen.register_shape(pers2)
  
await   ge_init()                                          #attende che tutte le immagini si siano caricate
await  asyncio.sleep(1)                                  #per forzare un'attesa di 1 secondo


jenny = Sprite()                                            #crea lo Sprite
jenny.shape(pers1)                                         #assegna l'immagine allo Sprite

bob = Sprite()                                          #crea lo Spite
bob.shape(pers2)                                       # allo Sprite


jenny.goto(-100,0)
bob.goto(-20,0)



await jenny.say ("Ciao!",3, dx=-20, dy=-90)                             #Parla per 3 secondi
await bob.say ("Ciao!",3, dx=20, dy=90 )                                #Parla per 3 seondi
await jenny.say ("Come stai?",3, dx=-20, dy=-90)                        #Parla per 3 secondi
await bob.say ("Bene! Vuoi andare a fare un bagno nel mare?",3, dx=20, dy=90)
await jenny.say ("Certo!",3, dx=-20, dy=-90)

await jenny.slide (-100, 30, 3)
await bob.slide (-50, 15, 3)



screen = Screen()                                        
screen.bgpic (sfondo2)                                
jenny.goto (-100,0)
bob.goto(-20, 0)

await bob.say ("Eccoci", 3, dx=-10, dy=90)
await jenny.say ("Andiamooo!!!!!", 3, dx=-50, dy=-90)

screen = Screen ()
screen.bgpic (sfondo3)
jenny.goto(-100, 0)
bob.goto(-20, 0)

