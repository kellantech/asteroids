import pygame, sys,math,random, string
from pygame.locals import *
import leader
global main,MAXA
MAXA = 20


main = pygame.display.set_mode((650, 650))
global black, white, red, write_text,font,showl
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

global pointd,missle,astroid,cu
pointd = {100:70,200:50,400:40,}


gcu = False

class missle:
    def __init__(self,rect,xs,ys):
      self.rect = rect
      self.xs = xs
      self.ys = ys
      self.color = random.choice([(255,0,0),(0,0,255),(0,255,0)])

class astroid(pygame.sprite.Sprite):
      def __init__(self,x,y,xs,ys,):
        
        self.points = random.choice((100,100,100,100,200,200,400))
        sz = pointd[self.points]
        self.image = pygame.image.load(random.choice(['a1.png','a2.png','a3.png']))
        self.image = pygame.transform.scale(self.image, (sz,sz))
        self.image = pygame.transform.rotate(self.image,random.randrange(-180,180))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y] 
        self.type = type
        self.xs = xs
        self.ys = ys


pygame.init()
font = pygame.font.SysFont('arial',30)
def write_text(t,sur,x=50,y=50):

    tr = font.render(str(t),True,white)
    sur.blit(tr,(x,y))

def showl():
    lead = leader.top10()
    y = 1
    main.fill(black)
    
    write_text("leaderboard:", main, 200,50)
    for l in lead:
      y += 1
      write_text(l, main, 200,50*y)

    
    pygame.display.update()
    while True:
      for event in pygame.event.get():
          if event.type == QUIT: sys.exit()
          if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()


def main_(tn,cu):
  mu = False
  na = 0
  circrad = 0
  iss=False

  MSPEED = 5
  SPINSPEED = math.pi/90
  LNLEN = 30
  score = 0

  
  crclcolors = ((0,0,255),(50, 245, 245),(160, 127, 201))
  crclc = random.choice(crclcolors)
    
  

  

  
  pygame.display.set_caption('!')
  clock = pygame.time.Clock()

  

  middle = 650/2

  player = pygame.Rect((middle,middle),(30,30))
  player.center = (middle,middle)
  

  m = []
  astroids = []

  rotation = math.pi

  lnpt =  (middle+math.sin(rotation)*LNLEN,\
           middle+math.cos(rotation)*LNLEN)

  itr = 0
  ca = 0

  tss = 1000

  
  crcl = pygame.draw.circle(main,(0,0,255),[middle,middle],circrad,5)

  while True:
      main.fill(black)
      if not cu:
        pygame.draw.circle(main,(50, 245, 245),(30,30),15,3)
      if iss:
        crcl = pygame.draw.circle(main,crclc,[middle,middle],circrad,5)
        circrad += 5
        if circrad > 300:
          iss = False
          circrad = 0
          crcl = pygame.draw.circle(main,crclc,[middle,middle],circrad,5)
        
      pygame.draw.rect(main,white,player)
      pygame.draw.line(main, white, (middle,middle), lnpt, 3)
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
            
          if event.type == KEYDOWN:
            if event.key == K_c:
              if not cu:
                iss = True
                cu = True
            if event.key == K_SPACE:
              if na < MAXA:
                m.append(\
                  missle(pygame.Rect(middle,middle,3,3),\
                                MSPEED*math.sin(rotation),\
                                MSPEED*math.cos(rotation),)
                  )
                na +=1

              else:
                if ca == 0: 
                  ca = itr
      keys = pygame.key.get_pressed()
      if keys[K_RIGHT]:
              
              rotation -= SPINSPEED
              lnpt =  (middle+math.sin(rotation)*LNLEN,\
           middle+math.cos(rotation)*LNLEN)


              
      if keys[K_LEFT]:
              rotation += SPINSPEED
              lnpt =  (middle+math.sin(rotation)*LNLEN,\
           middle+math.cos(rotation)*LNLEN)
      for mi in m:
        
        
        
        pygame.draw.rect(main,mi.color,mi.rect)
        mi.rect.top += mi.ys
        mi.rect.left += mi.xs


      for a in astroids:
        a.rect.centery += a.ys
        a.rect.centerx += a.xs
        main.blit(a.image,a.rect)
        if a.rect.colliderect(player) or player.colliderect(a.rect):
          
          return score,cu
        if a.rect.colliderect(crcl):
            
            score+= a.points
            
            a.rect.center = (random.randrange(65000,6500000000),random.randrange(65000,6500000000),)
        
        for mi2 in m:
          if mi2.rect.colliderect(a.rect) or a.rect.colliderect(mi2.rect):
              score+= a.points
              
              mi.rect.center = (random.randrange(65000,6500000000),random.randrange(65000,6500000000),) 
              a.rect.center = (random.randrange(65000,65000000),random.randrange(65000,6500000000),)
      if score> tss:
        cu = False
        
        tss = tss + 5000
        print(tss)
      if na >= MAXA:
        if ca + 180 <= itr and ca != 0:
          na = 0
          ca = 0
      if itr % 1200 == 0:
        na = 0
        ca = 0
      if circrad > 50:
        crclc = crclcolors[1]
      if circrad > 200:
        crclc = crclcolors[2]
      if itr%65 == 0:
        
        cn = random.randrange(0,8)
        if cn == 0:
          sy =  random.uniform(.2,2)
          sx = random.uniform(.2,2)
          astroids.append(astroid(0,0,sx, sy))
        if cn == 1:
          sy2 = -random.uniform(.2,2)
          sx2 = -random.uniform(.2,2)
          
          astroids.append(astroid(650,650,sx2, sy2))
        if cn == 2 :
          sy3 = -random.uniform(.2,2)
          sx3= random.uniform(.2,2)
          
          astroids.append(astroid(0,650,sx3, sy3))
        if cn == 3:
          sy4 = random.uniform(.2,2)
          sx4 = -random.uniform(.2,2)
          
          astroids.append(astroid(650,0,sx4, sy4))
        if cn == 4:
          sy5 = random.uniform(.5,2)
          sx5 = random.uniform(-2,2)
          
          astroids.append(astroid(325,0,sx5, sy5))
        if cn == 5:
          sy6 = -random.uniform(.5,2)
          sx6 = random.uniform(-2,2)
          
          astroids.append(astroid(325,600,sx6, sy6))
        if cn == 6:
          sy7 = random.uniform(-2,2)
          sx7 = random.uniform(.5,2)
          
          astroids.append(astroid(0,325,sx7, sy7))
        if cn == 7:
          sy8 = random.uniform(-2,2)
          sx8 = -random.uniform(.5,2)
          
          astroids.append(astroid(600,325,sx8, sy8))

      itr+=1
      write_text(score,main)
      write_text(str(tn)+" tries left",main,500)
      pygame.display.update()
      clock.tick(60)


def get_init(sc):
    chars = ['_','_','_']
    cin = 0
    cval = -1
    while True:

      main.fill(black)
      write_text("please enter your initals",main,200,100)

      write_text(' '.join(chars),main,200,300)

      for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_UP:

              cval += 1
              cval %= len(string.ascii_uppercase)

              chars[cin] = string.ascii_uppercase[cval]

          if event.key == K_DOWN:

              cval -= 1
              cval %= len(string.ascii_uppercase)

              chars[cin] = string.ascii_uppercase[cval]

          if event.key == K_RETURN:
            if cin < 2:
              cin += 1
              cval = -1
            else:
              leader.add_entry(''.join(chars),sc)
              showl()

      pygame.display.update()


def wait(cs):
  main.fill(black)
  write_text("press any key to continue",main,200,200)
  write_text(f"your current score is {cs}",main,200,300)
  pygame.display.update()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT: sys.exit()
      if event.type == KEYDOWN: return


sco,gcu = main_(2,False)
wait(sco)



sco2, gcu2 = main_(1 , gcu)
sco += sco2
gco = gcu2 or gcu

wait(sco)
sco3, gcu3 = main_(0, gcu)
sco += sco3


get_init(sco)
