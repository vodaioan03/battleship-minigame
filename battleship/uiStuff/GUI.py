import random
import time
import pygame
pygame.init()
from domain.board import *
from domain.boat import *
from utils.constants import *

class GUI:
  
  def __init__(self) -> None:
    self.playerBoats = []
    self.computerBoats = []
    self.isOnMenu= True
    self.inStrategy = False
    self.isPlaying = False
    self.inWinner = False
    self.mouseDown = False
    self.rect = None
    self.turn = 'Player'
    self.winner = None
    self.debug = False
    self.message = ''
    
  def playerName(self,playerName):
    self.playerName = playerName
    
  def quitGame(self):
    self.isOnMenu= False
    self.inStrategy = False
    self.isPlaying = False
    self.inWinner = False
    
  
  def createBoatsForComputer(self):
    for each in self.computerBoats:
      while each.boardSquare[0] == -1:
        number = random.randint(1,100)
        if number % 2 == 0:
          each.changeAlign()
        each.position = (random.randint(SQUARE_SIZE+340,SQUARE_SIZE*10+340), random.randint(SQUARE_SIZE+40,SQUARE_SIZE*10+40))
        each.draw()
        self.computerBoard.verifyCoordsinSquare(each)
    
    
    
  #MAIN MENU 
  def mainMenu(self):
    while self.isOnMenu:
      self.uiInterface.fill(COLOR_BLACK)
      self.uiInterface.blit(BACKGROUNDIMAGE,(0,0))
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          #PLAY BUTTON
          if WIDTH/2-80 <= mousePos[0] <= WIDTH/2+48 and HEIGHT/2+50 <= mousePos[1] <= HEIGHT/2+114: 
            self.isOnMenu = False
            self.inStrategy = True
            break
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.quitGame()
            break
          
      self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-80,HEIGHT/2+50)) 
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      pygame.display.update() 
    
    
  #STRATEGY PANEL
  def strategyPanel(self):
    if self.inStrategy:
      self.createBoats() 
      
    while self.inStrategy:
      self.uiInterface.fill(COLOR_BLACK)
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
          # QUIT BUTTON
          if event.button == 1:
            if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
              self.quitGame()
              break
            #START BUTTON
            if WIDTH/2-100 <= mousePos[0] <= WIDTH/2+28 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16 and self.playerBoard.ones == self.playerBoard.oneNeeded: 
              self.inStrategy = False
              self.isPlaying = True
              break
            self.rect = self.verifyPositionBoat(mousePos)
            if self.rect != None:
              self.playerBoard.boatTaken(self.rect)
            self.mouseDown = True
          elif event.button == 3:
            self.rect = self.verifyPositionBoat(mousePos)
            if self.rect != None and self.rect.isAdded != True:
              self.rect.changeAlign()
            else:
              self.rect = None
        if event.type == pygame.MOUSEBUTTONUP:
          if self.rect != None:
            self.playerBoard.verifyCoordsinSquare(self.rect)
          self.mouseDown = False
          self.rect = None
        if event.type == pygame.MOUSEMOTION and self.mouseDown and self.rect != None:
          self.rect.position = mousePos
      self.create_board()
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT, (20,HEIGHT-20))  
      self.uiInterface.blit(STRATEGY_PANEL,(WIDTH/2-120,50))
      if self.playerBoard.ones == self.playerBoard.oneNeeded:
        self.uiInterface.blit(PLAYBUTTON , (WIDTH/2-100,HEIGHT-80)) 
      pygame.display.update() # UPDATE GAME WINDOW
    
    
    
  def playingPanel(self):
    if self.isPlaying:
      self.computerBoard.boardview()
      self.createBoatsForComputer()
      
      for each in self.playerBoats:
        each.setSquareSize(SQUARE_SIZE_MINI)
      for each in self.computerBoats:
        each.setSquareSize(SQUARE_SIZE_MINI)
    while self.isPlaying:
      self.uiInterface.fill(COLOR_BLACK)
      self.uiInterface.blit(OCEANBACKGROUND,(0,0))
      
      if self.turn == 'Computer':
        self.uiInterface.blit(self.message,(120+SQUARE_SIZE_MINI+40,600))
        self.endtime = time.time()
        if self.endtime - self.start_time > 2:
          self.message = self.sendShot()
          self.message = BIG_FONT.render(self.message,True,COLOR_WHITE)
          self.turn = 'Player'
      if self.turn == 'Player' and self.message != '':
        self.uiInterface.blit(self.message,(740+SQUARE_SIZE_MINI+40,600))
      
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.quitGame()
            break
          if self.turn == 'Player':
            if SQUARE_SIZE_MINI+80 <= mousePos[0] <= SQUARE_SIZE_MINI*(BOARD_ROWS+1)+80 and SQUARE_SIZE_MINI+150 <= mousePos[1] <= SQUARE_SIZE_MINI*(BOARD_COL+1)+150:
              if self.computerBoard.checkShoot(mousePos):
                self.message = self.computerBoard.boardShot(mousePos)
                self.message = BIG_FONT.render(self.message,True,COLOR_WHITE)
                self.turn = 'Computer'
                self.start_time = time.time()
              else:
                print("Invalid Shot!")
          else:
            print("Isn't your turn.")
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_F1:
            self.debug = not self.debug
          if self.debug:
            if event.key == pygame.K_F2:
              self.winner = 1
            if event.key == pygame.K_SPACE:
              self.playerBoard.boatShots = self.playerBoard.oneNeeded - 1
            if event.key == pygame.K_F3:
              self.computerBoard.boatShots = self.computerBoard.oneNeeded - 1
              
      #CREATE EMPTY BOARD
      self.playerBoard.boardPlaying(700,150,PLAYER_BOARD)
      self.computerBoard.boardPlaying(80,150,COMPUTER_BOARD)
      
      #CREATE VIEW BOATS
      self.createBoatsView()
      if self.debug:
        self.createComputerBoatsView()
        
      #ADD SHOTS ON THE BOARD
      self.computerBoard.addShotsOnMap()
      self.playerBoard.addShotsOnMap()
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      
      pygame.display.update() #
      
      if self.computerBoard.boatShots == self.computerBoard.oneNeeded:
        self.winner = 1 #PLAYER
      elif self.playerBoard.boatShots == self.playerBoard.oneNeeded:
        self.winner = 2 #COMPUTER
      
      if self.winner != None:
        self.isPlaying = False
        self.inWinner = True
      
      
  def winnerPanel(self):
    while self.inWinner:
      self.uiInterface.fill((100,100,100))
      self.uiInterface.blit(WINNERBACKGROUND,(0,0))
      
      for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
          self.quitGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          
          # QUIT BUTTON
          if WIDTH-140 <= mousePos[0] <= WIDTH-12 and HEIGHT-80 <= mousePos[1] <= HEIGHT-16: 
            self.quitGame()
            break
      self.uiInterface.blit(QUITBUTTON , (WIDTH-140,HEIGHT-80)) 
      self.uiInterface.blit(COPYRIGHT,(20,HEIGHT-20))
      if self.winner == 1:
        self.uiInterface.blit(WIN,(450,150))
      else:
        self.uiInterface.blit(LOOSE,(450,150))
      
      pygame.display.update() #

  def sendShot(self):
    squarei = random.randint(1,BOARD_ROWS)
    squarez = random.randint(1,BOARD_ROWS)
    while self.playerBoard.logicBoard[squarei][squarez] == 2:
      squarei = random.randint(1,BOARD_ROWS)
      squarez = random.randint(1,BOARD_ROWS)

    coords = self.playerBoard.getCoordsForSquare(squarei,squarez)
    return self.playerBoard.boardShot(coords)
    
  def create_board(self):
    self.playerBoard.boardview()
    pygame.draw.rect(self.uiInterface,COLOR_BLUE,[0,95,300,500])
    self.createBoatsView()
    
  def createBoatsView(self):
    for each in self.playerBoats:
      each.draw()
  
  def createComputerBoatsView(self):
    for each in self.computerBoats:
      each.draw()
    
  def createBoats(self):
    self.playerBoard = Board(self.uiInterface)
    self.boatCarrier = Boat('Carrier',IMG_BOAT_CARRIER,BOAT_CARRIER,10,105,COLOR_BLACK,self.uiInterface,self.playerBoard)
    self.boatBattleship = Boat('Battleship',IMG_BOAT_BATTLESHIP,BOAT_BATTLESHIP,80,105,COLOR_BLACK,self.uiInterface,self.playerBoard)
    self.boatDestroyer = Boat('Destroyer',IMG_BOAT_DESTROYER,BOAT_DESTROYER,170,105,COLOR_BLACK,self.uiInterface,self.playerBoard)
    self.boatSubmarine = Boat('Submarine',IMG_BOAT_SUBMARINE,BOAT_SUBMARINE,100,375,COLOR_BLACK,self.uiInterface,self.playerBoard)
    self.boatPatrol = Boat('Patrol',IMG_BOAT_PATROL,BOAT_PATROL,170,375,COLOR_BLACK,self.uiInterface,self.playerBoard) 
    
    self.playerBoats = [self.boatCarrier,self.boatBattleship,self.boatDestroyer,self.boatSubmarine,self.boatPatrol]
    
    self.computerBoard = Board(self.uiInterface)
    self.computerBoatCarrier = Boat('Carrier',IMG_BOAT_CARRIER,BOAT_CARRIER,10,105,COLOR_BLACK,self.uiInterface,self.computerBoard)
    self.computerBoatBattleship = Boat('Battleship',IMG_BOAT_BATTLESHIP,BOAT_BATTLESHIP,80,105,COLOR_BLACK,self.uiInterface,self.computerBoard)
    self.computerBoatDestroyer = Boat('Destroyer',IMG_BOAT_DESTROYER,BOAT_DESTROYER,170,105,COLOR_BLACK,self.uiInterface,self.computerBoard)
    self.computerBoatSubmarine = Boat('Submarine',IMG_BOAT_SUBMARINE,BOAT_SUBMARINE,100,375,COLOR_BLACK,self.uiInterface,self.computerBoard)
    self.computerBoatPatrol = Boat('Patrol',IMG_BOAT_PATROL,BOAT_PATROL,170,375,COLOR_BLACK,self.uiInterface,self.computerBoard) 
    
    self.computerBoats = [self.computerBoatCarrier,self.computerBoatBattleship,self.computerBoatDestroyer,self.computerBoatSubmarine,self.computerBoatPatrol]
    
    
  def verifyPositionBoat(self,mousePos):
    for each in self.playerBoats:
      if each.position[1] <= mousePos[1] <= (each.position[1] + each.height) and each.position[0] <= mousePos[0] <= (each.position[0] + each.width):
        return each
    return None
  
  def startGame(self):
    self.uiInterface = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('BattleShip - Minigame')
    pygame.display.set_icon(ICON)

    #MAIN MENU
    self.mainMenu()
         
    # STRATEGY PANEL
    self.strategyPanel()
    # PLAYING PANEL
    self.playingPanel()
    # WINNER PANEL
    self.winnerPanel()
      
    pygame.quit()