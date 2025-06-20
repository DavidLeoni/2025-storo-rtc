from turtleps import *
sfondo1 ="bg-seaside-2.gif"
sfondo2 ="bg-space-1.gif"
pers1 = "ch-paladin-e.gif"
pers2 = "ch-wizard-w.gif"
pers3 = "ch-slime-e.gif"
pers4 = "ch-arctic-kid-e.gif"
anim1 = "anh-chicken-dt.gif"
screen = Screen()
screen.bgpic(sfondo1)

screen.register_shape(pers1)
screen.register_shape(pers2)
screen.register_shape(pers3)
screen.register_shape(pers4)
screen.register_shape(anim1)
await ge_init()

cookies = Sprite()
cookies.shape(pers1)
cookies.goto (0,0)

pollo = Sprite()
pollo.shape(anim1)
pollo.goto (-150,-120)

async def click_pollo(evento):
  await pollo.say("drin drin snack in arrivo drin dron e continua la festa",7)
  await pollo.say("gnam gnam il mc in arrivo gnam gnam e lo starbucks",7)
pollo.svg.onclick = click_pollo  


await cookies.say("oh no mi sono persa nell'isola di Cook",2, dy=75)

viky = Sprite()
viky.shape(pers2) 
viky.goto (-100,100)

await viky.say ("skibidi dob dob dob... sono Viky e dono ironia a tutti",5, dy=75)
await cookies.say("ma chi sei vai via",2, dy=75)

skibidi = Sprite()
skibidi.shape(pers3)
skibidi.goto (-50,-120)
skibidi.to_background()

pizza = Sprite()
pizza.shape(pers4)
pizza.goto (100,-120)

await skibidi.say("ciao sono skibidi vengo da un bidone",3, dy=60)
await cookies.say("aiuto un altro essere strano!",2, dy=75)                
await viky.say("ma come ti permetti di definirci esseri strani?",4, dy=75)
await cookies.say("scusate se vi ho ferito",2, dy=75)
await skibidi.say("accettiamo le scuse",2, dy=60)
await viky.say("esatto",2, dy=75)
await cookies.say (" allora vi mostro il mio fratellino",3, dy=75)
await skibidi.say ("io ho paura di spaventarlo",3, dy=60)
await viky.say ("tranquillo non lo spaventerai",3, dy=75)





await viky.say ("se no gli do una pozione.. che bella idea!",4, dy=75)
await cookies.say ("no non ci penso neanche",3, dy=75)
await cookies.say ("ha solo 2 anni ",2, dy=75)
await pizza.say ("ciao a tutti!",2, dy=50)
await pizza.say ("ma se andassimo sullo spazio??",2, dy=50)
await cookies.say ("e se andassimo comunque",3, dy=75)
await cookies.say ("magari si chiedi a Viky",2, dy=75)
await cookies.say ("lui ha tutte le pozioni pensa te!",2, dy=75)
await pizza.say ("forte",2, dy=75)

screen.bgpic(sfondo2)

await pizza.slide (0,150,3)

await viky.slide (150,0,3)
await cookies.say ("sei felice Pizza?",2, dy=75)
await pizza.say ("si sono super felice!",2, dy=50)
await viky.say ("io non molto perchè non ci sono risorse",3, dy=75)
await viky.say ("io me ne vado vi lascio qui",3, dy=75)
await cookies.say ("nooo ci ha lasciato qui da sole",3, dy=75)
await viky.say ("scherzetto non vi lascio mica qua da sole!",3, dy=75)
await pizza.say ("ok...",2, dy=50)
await cookies.say ("ma dai Viky.. non fare così",3, dy=75)
await viky.say ("va bene mamma mia non mi stressare",3, dy=75)
await pizza.say ("cosa ha detto Viky sorellona?",3, dy=50)
await cookies.say ("niente.. ritorniamo sull'isola",3, dy=75)
await pizza.say ("si, sto iniziando ad avere paura",3, dy=50)
await skibidi.say ("!! un asteroide tutti al riparo !!",3, dy=60)

screen.bgpic(sfondo1)
pizza.goto(100,-100)
viky.goto(-100,100)
                                   
await pizza.say ("ahhhh, cosa è successo?",2, dy=50)
await cookies.say ("stavamo tutti dormendo mi sa",3, dy=75)  
await viky.say ("secondo i miei calcoli ha ragione Cookies",4, dy=75)
await skibidi.say ("secondo me no perchè io vengo da un bidone si ma..",5, dy=60)
await pizza.say ("finisci la frase",2, dy=50)
await skibidi.say ("ero troppo piccolo ma so solo che lo spazio è fatto così",5, dy=60)
await viky.say ("ti faccio un test per il cervello così puoi ricordarti",5, dy=75)
await skibidi.say ("ok.. ma se non succede mi devi il fratello di Cookies",5, dy=60)
await cookies.say ("noooo, ti darà 70 noci di cocco",3, dy=75)   
await pizza.say ("finiamo il gioco dai..",2, dy=50)
await cookies.say ("ok Viky!! Finisci il gioco su!",3, dy=75)
await viky.say ("perfetto al mio 3 vi salutiamo",3, dy=75)
await skibidi.say (" 3,2,1 ciaooooooo al prossimo gioco",3, dy=60)



