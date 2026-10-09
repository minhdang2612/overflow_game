# Game mechanics:
# Phase 1:
# - Select number of players
# - Select colours for each players 
# - Place blocks - DONE
# Phase 2:
# - Choose to push or put
# - Choose buttons to push rows or columns
# - Push block animation - DONE
# - Put down blocker block - DONE
# - Change position of blocker block 
# - Remove blocker block
# - Put down BLACK block - DONE

# Tying the game together - Make a wireframe plan sort of thing 
# -> list out all the actions the players can take
# Then program the players taking turn thing -> make the game for 2-9 players 
# Then create a menu thing 

import pygame
from random import randint
from time import sleep

def WindowSetup():
    global Clock, GameActive, Screen, ThisGame
    pygame.init
    Clock = pygame.time.Clock()
    GameActive = True
    pygame.display.set_caption("Overflow")
    ScreenWidth = 1300
    ScreenHeight = 900
    Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
    ThisGame = Game()

def SetupGrid():
    # ThisGrid = [[randint(0,1) for i in range(7)] for j in range(7)]
    ThisGrid = [[-1 for i in range(7)] for j in range(7)]
    return ThisGrid

class Game:
    def __init__(self):
        self.Grid = SetupGrid()
        self.Turn = 0

    def SetUpPlayers(self, NumberOfPlayers):
        self.Players = [i for i in range(NumberOfPlayers)]

    def DrawGrid(self):
        CurrentColour = "Black"
        for Row in range(7):
            for Column in range(7):
                if self.Grid[Row][Column] == -1:
                    CurrentColour = "Grey"
                elif self.Grid[Row][Column] == 0:
                    CurrentColour = "Green"
                elif self.Grid[Row][Column] == 1:
                    CurrentColour = "Red"
                elif self.Grid[Row][Column] == 2:
                    CurrentColour = "Cyan"
                elif self.Grid[Row][Column] == 8:
                    CurrentColour = "Black"
                elif self.Grid[Row][Column] == 9:
                    CurrentColour = "Purple"
                RowCoordinate = 100*Row + 100
                ColumnCoordinate = 100*Column + 100
                pygame.draw.rect(Screen, CurrentColour, pygame.Rect(RowCoordinate,ColumnCoordinate,100,100))           
                pygame.draw.rect(Screen, "Black", pygame.Rect(RowCoordinate,ColumnCoordinate,100,100),1)

    def DrawButton(self):
        # Top and Bottom
        for Column in range(7):
            RowCoordinate = 100*Column + 125
            ColumnCoordinate = 25
            pygame.draw.rect(Screen, "Blue", pygame.Rect(RowCoordinate, ColumnCoordinate, 50,50))
            ColumnCoordinate = 825
            pygame.draw.rect(Screen, "Blue", pygame.Rect(RowCoordinate, ColumnCoordinate, 50,50))
        # Left and Right
        for Row in range(7):
            ColumnCoordinate = 100*Row + 125
            RowCoordinate = 25
            pygame.draw.rect(Screen, "Blue", pygame.Rect(RowCoordinate, ColumnCoordinate, 50,50))
            RowCoordinate = 825
            pygame.draw.rect(Screen, "Blue", pygame.Rect(RowCoordinate, ColumnCoordinate, 50,50))

    def MapScreenToButton(self):
        ButtonX, ButtonY = -1, -1
        if pygame.mouse.get_pressed()[0] == True:
            MouseX, MouseY = pygame.mouse.get_pos()
            # Top side buttons
            if MouseY >= 25 and MouseY <= 75:
                if MouseX >= 125 and MouseX <= 175:
                    ButtonX, ButtonY = 1,0
                elif MouseX >= 225 and MouseX <= 275:
                    ButtonX, ButtonY = 1,1
                elif MouseX >= 325 and MouseX <= 375:
                    ButtonX, ButtonY = 1,2
                elif MouseX >= 425 and MouseX <= 475:
                    ButtonX, ButtonY = 1,3
                elif MouseX >= 525 and MouseX <= 575:
                    ButtonX, ButtonY = 1,4
                elif MouseX >= 625 and MouseX <= 675:
                    ButtonX, ButtonY = 1,5
                elif MouseX >= 725 and MouseX <= 775:
                    ButtonX, ButtonY = 1,6
            # Bottom side buttons
            elif MouseY >= 825 and MouseY <= 875:
                if MouseX >= 125 and MouseX <= 175:
                    ButtonX, ButtonY = 3,0
                elif MouseX >= 225 and MouseX <= 275:
                    ButtonX, ButtonY = 3,1
                elif MouseX >= 325 and MouseX <= 375:
                    ButtonX, ButtonY = 3,2
                elif MouseX >= 425 and MouseX <= 475:
                    ButtonX, ButtonY = 3,3
                elif MouseX >= 525 and MouseX <= 575:
                    ButtonX, ButtonY = 3,4
                elif MouseX >= 625 and MouseX <= 675:
                    ButtonX, ButtonY = 3,5
                elif MouseX >= 725 and MouseX <= 775:
                    ButtonX, ButtonY = 3,6        
            else:
                # Left side buttons
                if MouseX >= 25 and MouseX <= 75:
                    if MouseY >= 125 and MouseY <= 175:
                        ButtonX, ButtonY = 0,0
                    elif MouseY >= 225 and MouseY <= 275:
                        ButtonX, ButtonY = 0,1
                    elif MouseY >= 325 and MouseY <= 375:
                        ButtonX, ButtonY = 0,2
                    elif MouseY >= 425 and MouseY <= 475:
                        ButtonX, ButtonY = 0,3
                    elif MouseY >= 525 and MouseY <= 575:
                        ButtonX, ButtonY = 0,4
                    elif MouseY >= 625 and MouseY <= 675:
                        ButtonX, ButtonY = 0,5
                    elif MouseY >= 725 and MouseY <= 775:
                        ButtonX, ButtonY = 0,6  
                # Right side buttons
                elif MouseX >= 825 and MouseX <= 875:
                    if MouseY >= 125 and MouseY <= 175:
                        ButtonX, ButtonY = 2,0
                    elif MouseY >= 225 and MouseY <= 275:
                        ButtonX, ButtonY = 2,1
                    elif MouseY >= 325 and MouseY <= 375:
                        ButtonX, ButtonY = 2,2
                    elif MouseY >= 425 and MouseY <= 475:
                        ButtonX, ButtonY = 2,3
                    elif MouseY >= 525 and MouseY <= 575:
                        ButtonX, ButtonY = 2,4
                    elif MouseY >= 625 and MouseY <= 675:
                        ButtonX, ButtonY = 2,5
                    elif MouseY >= 725 and MouseY <= 775:
                        ButtonX, ButtonY = 2,6         

        return ButtonX, ButtonY

    def RandomUpdateGrid(self):
        for Row in range(7):
            for Column in range(7):
                self.Grid[Row][Column] = randint(0,1)

    def UserSelectSquare(self, CurrentPlayer):
        if pygame.mouse.get_pressed()[0] == True:
            MouseX, MouseY = pygame.mouse.get_pos()
            if MouseX >= 101 and MouseX <= 799 and MouseY >= 101 and MouseY <= 799:
                MouseX = MouseX//100 - 1
                MouseY = MouseY//100 - 1
                self.Grid[MouseX][MouseY] = CurrentPlayer
                sleep(0.3)
                self.Turn += 1

    def UserSetBlockerToken(self):
        if pygame.mouse.get_pressed()[0] == True:
            MouseX, MouseY = pygame.mouse.get_pos()
            if MouseX >= 101 and MouseX <= 799 and MouseY >= 101 and MouseY <= 799:
                MouseX = MouseX//100 - 1
                MouseY = MouseY//100 - 1
                self.Grid[MouseX][MouseY] = 8

    def MapButtonToStartSquare(self):
        StartX, StartY = -1, -1
        ButtonX, ButtonY = self.MapScreenToButton()
        if ButtonX == 0:
            StartX = 0
            StartY = ButtonY
        elif ButtonX == 1:
            StartX = ButtonY
            StartY = 0
        elif ButtonX == 2:
            StartX = 6
            StartY = ButtonY
        elif ButtonX == 3:
            StartX = ButtonY
            StartY = 6
        return ButtonX, StartX, StartY

    def CheckBlockerTokenInRow(self, Row):
        BlockerToken = 8
        if BlockerToken in self.Grid[Row]:
            return True
        else:
            return False
    
    def CheckBlockerTokenInColumn(self, Column):
        BlockerToken = 8
        BlockerTokenPresent = False
        i = 0
        while i <= 6 and not(BlockerTokenPresent):
            if self.Grid[i][Column] == BlockerToken:
                BlockerTokenPresent = True
            else:
                i += 1
        return BlockerTokenPresent
    
    def PushSquares(self):
        # ButtonX, StartX, StartY = self.MapButtonToStartSquare()
        ButtonX, StartX, StartY = self.MapButtonToStartSquare()
        if ButtonX != -1 and StartX != -1 and StartY != -1:
            # Push right
            if ButtonX == 0 and self.CheckBlockerTokenInColumn(StartY) == False:
                for i in range(6,0,-1):
                    self.Grid[i][StartY] = self.Grid[i-1][StartY]
                self.Grid[StartX][StartY] = 9
            # Push down
            elif ButtonX == 1 and self.CheckBlockerTokenInRow(StartX) == False:
                for i in range(6,0,-1):
                    self.Grid[StartX][i] = self.Grid[StartX][i-1]
                self.Grid[StartX][StartY] = 9  
            # Push left
            elif ButtonX == 2 and self.CheckBlockerTokenInColumn(StartY) == False:
                for i in range(0,6):
                    self.Grid[i][StartY] = self.Grid[i+1][StartY]
                self.Grid[StartX][StartY] = 9  
            # Push up
            elif ButtonX == 3 and self.CheckBlockerTokenInRow(StartX) == False:
                for i in range(0,6):
                    self.Grid[StartX][i] = self.Grid[StartX][i+1]
                self.Grid[StartX][StartY] = 9
    
    def ChangeTurn(self, NumberOfPlayers, Turn):
        CurrentPlayer = Turn%NumberOfPlayers
        return CurrentPlayer

    def Run(self):
        self.DrawGrid()
        self.DrawButton()
        self.UserSelectSquare(self.ChangeTurn(3, self.Turn))
        # self.UserSetBlockerToken()
        if pygame.mouse.get_pressed()[0]:
            self.PushSquares()
            sleep(0.5)

def Main():
    global Clock, GameActive, Screen, ThisGame
    WindowSetup()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if GameActive:
            Screen.fill('White')
            ThisGame.Run()

        pygame.display.update()
        Clock.tick(60)

Main()