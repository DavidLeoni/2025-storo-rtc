from turtleps import *
from pyscript import document

tasti = set()

def tasto_down(evento):
  print(evento.key)
  tasti.add(evento.key)

def tasto_up(evento):
  if evento.key in tasti:
    tasti.remove(evento.key)
    
document.onkeydown = tasto_down
document.onkeyup   = tasto_up

attesa = 0.02
metallo = False 
carta = False

async def muovi_pinza():
  global metallo  
  global carta
  
  while True:
    pinza.color ('grey')
    
    if "ArrowUp" in tasti:
      pinza.y += 4
    if "ArrowRight" in tasti:
      pinza.x += 4
    if "ArrowLeft" in tasti:
      pinza.x -= 4
    if "ArrowDown" in tasti:
      pinza.y -= 4
    
    if " " in tasti:
      metallo = False
    
    if pinza.x <-100 and pinza.y <-100 : 
      metallo = True 
      
    if " " in tasti:
      carta = False
      
    if pinza.x >100 and pinza.y >-100:
      carta = True
      
    await asyncio.sleep(attesa)
      
async def muovi_moka():
  
  while True:
    if metallo :
      rifiutopesante.goto(pinza.x, pinza.y)
      
    await asyncio.sleep(attesa)

async def muovi_bicchiere():
  
  while True:
    if carta : 
      rifiutoleggero.goto(pinza.x, pinza.y)
      
    await asyncio.sleep(attesa)

screen = Screen()

            
#ipinza = "https://cdn.glitch.global/27978cd8-fd10-4f21-b25d-a92799195e85/pinza-removebg-preview.png?v=1748006934750"
  
ipinza = "pinza.png"

irifiutopesante = "moka.png"

irifiutoleggero = "bicchiere.png"

iomino = "omino1.gif"

terrasfondo = "sfondo1.gif"

icestino = "cestino.png"
  
screen.register_shape(ipinza)    # registriamo immagine

screen.register_shape(icestino)    # registriamo immagine
screen.register_shape(iomino)    # registriamo immagine

screen.register_shape (irifiutopesante)

screen.register_shape (irifiutoleggero)

await ge_init()                # attende caricamento 

screen.bgpic (terrasfondo)

rifiutopesante = Sprite ()

rifiutoleggero = Sprite ()

omino = Sprite ()

pinza = Sprite ()

cestino = Sprite ()

pinza.shape(ipinza)


omino.shape(iomino)

rifiutopesante.shape (irifiutopesante)

rifiutoleggero.shape (irifiutoleggero)

cestino.shape(icestino)

rifiutoleggero.shapesize (0.15,0.15)

rifiutopesante.shapesize (0.125,0.125)

pinza.shapesize (0.125,0.125)

cestino.shapesize (0.3,0.3)

cestino.goto (60, 50)

omino.goto (-60, 50)

rifiutoleggero.goto (100, -65)

rifiutopesante.goto (-150, -150)

pinza.to_foreground ()







await asyncio.gather(muovi_pinza(),
                     muovi_moka(),
                     muovi_bicchiere())
