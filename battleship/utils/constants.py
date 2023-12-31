import pygame

# z- in orizontal, i - columnt

#DISPLAY SETTINGS
WIDTH = 1280
HEIGHT = 720


#colors
COLOR_LIGHT = (170,170,170) 
COLOR_DARK = (100,100,100) 
COLOR_WHITE = (255,255,255)
COLOR_GREY = (115, 115, 115)
COLOR_BLUE = (51, 51, 255)
COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)

#FONT
FONT_SIZE = 12
BIGFONT = 32
FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
BIG_FONT = pygame.font.Font(pygame.font.get_default_font(),BIGFONT)

#IMAGE LOADER
ICON = pygame.image.load('battleship\\utils\\game_logo.jpg')
PLAYBUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\play_button.png'),(128,64))
QUITBUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\quit_button.png'),(128,64))
BACKGROUNDIMAGE = pygame.transform.scale(pygame.image.load('battleship\\utils\\background_image.jpg'),(WIDTH,HEIGHT))
OCEANBACKGROUND = pygame.transform.scale(pygame.image.load('battleship\\utils\\oceanview.jpg'),(WIDTH,HEIGHT))
EXPLODEICON = pygame.transform.scale(pygame.image.load('battleship\\utils\\explode.png'),(30,30))
WIN = pygame.transform.scale(pygame.image.load('battleship\\utils\\youwin.png'),(360,360))
LOOSE = pygame.transform.scale(pygame.image.load('battleship\\utils\\youlose.png'),(360,360))
WINNERBACKGROUND = pygame.transform.scale(pygame.image.load('battleship\\utils\\winnerbackground.jpg'),(WIDTH,HEIGHT))
SHUFFLE_BUTTON = pygame.transform.scale(pygame.image.load('battleship\\utils\\shuffle.png'),(50,50))
OCEAN_STORM = pygame.transform.scale(pygame.image.load('battleship\\utils\\oceanStorm.jpg'),(WIDTH,HEIGHT))
TEXTURE = pygame.transform.scale(pygame.image.load('battleship\\utils\\texture.jpg'),(300,500))

#TEXTS
COPYRIGHT = FONT.render('@copyright by Voda',True,COLOR_WHITE)
STRATEGY_PANEL = BIG_FONT.render('STRATEGY PANEL',True,COLOR_WHITE)
COMPUTER_BOARD = BIG_FONT.render('COMPUTER BOARD',True,COLOR_WHITE)
PLAYER_BOARD = BIG_FONT.render('PLAYER BOARD',True,COLOR_WHITE)

#BOARD 
BOARD_ROWS = 10
BOARD_COL = 10
SQUARE_SIZE = 55
SQUARE_SIZE_MINI = 40



#BOATS

BOAT_CARRIER = 5  
BOAT_BATTLESHIP = 4
BOAT_DESTROYER = 3
BOAT_SUBMARINE = 3
BOAT_PATROL = 2
IMG_BOAT_CARRIER = pygame.image.load('battleship\\utils\\carrier.png')
IMG_BOAT_BATTLESHIP = pygame.image.load('battleship\\utils\\battleship.png')
IMG_BOAT_DESTROYER = pygame.image.load('battleship\\utils\\destroyer.png')
IMG_BOAT_SUBMARINE = pygame.image.load('battleship\\utils\\submarine.png')
IMG_BOAT_PATROL = pygame.image.load('battleship\\utils\\patrol.png')
