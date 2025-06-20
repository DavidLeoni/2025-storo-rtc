import turtleps
from turtleps import *

from pyscript import document

tasti = set()

def tasto_down(evento):
  tasti.add(evento.key)

def tasto_up(evento):
  if evento.key in tasti:
    tasti.remove(evento.key)

document.onkeydown = tasto_down
document.onkeyup   = tasto_up
 
#pers1 = "https://vectorportal.com/storage/fQsdpOLBgw82I54Ua4Jd2IhXSr7qY0u4jxV082qZ.jpg"
#pers2 = "https://it.vecteezy.com/arte-vettoriale/12189164-mobile-telefono-con-triste-viso-su-schermo-rotto-smartphone-problema-con-tecnica-cartone-animato-piatto-illustrazione-scioccato-e-sorpreso-occhi-e"

screen = Screen ()
citta = "https://cdn.glitch.global/dac566dd-9fc8-4f9b-9ea1-174a1295f9ae/bg-ruins-2.gif?v=1748612106233"
screen.bgpic(citta)



pers1 = "tablet.png"
pers2 = "phone.png"

screen = Screen()
screen.register_shape(pers1)    
               
   


screen = Screen()
screen.register_shape(pers2)    
await ge_init()               

tablet = Sprite()
phone = Sprite()
tablet.shape(pers1) 
phone.shape(pers2)

 
phone.shapesize(0.2,0.2)
phone.forward (100)

tablet.shapesize(-0.3,0.3)
tablet.forward (-100)

await  phone.say("Ciao.",3, dy = 150)
await  tablet.say("Cosa ti sei fatto?",3, dy = 150)
await  phone.say("La mia padrona mi ha buttato dal balcone! ",3, dy = 150)
await  phone.say("E' un po' pazza!",3, dy = 150)
await  tablet.say("Non preoccuparti! ",3, dy = 150)
await  tablet.say("A Storo esistono degli eventi.", 3, dy = 150)
await  tablet.say("Ci sono dei volontari che riparano oggetti elettronici.",3, dy = 150)
await  phone.say("Ma devo pagare. Io sono al verde!",3, dy = 150 )
await  tablet.say("Assolutamente no, fanno tutto gratis.",3, dy = 150 )
await  tablet.say("E ti insegnano ad aggiustare gli oggetti.",3 , dy = 150)
await  tablet.say("Ma se vuoi puoi dare un piccolo contributo.",3 , dy = 150)
await  tablet.say("Servirà per comprare tutto quello che occorre.",3, dy = 150)






