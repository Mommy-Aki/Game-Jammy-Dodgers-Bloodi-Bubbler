import pygame
from pygame.locals import *
from random import randint
from time import sleep as wait
import tkinter

DebugBarriers = False

class Game:
    def __init__(self):
        self.Running = True
        self.SurfDisplay = False
        self.ScreenSize = self.weight, self.height = 1920, 1080
        self.Clock = pygame.time.Clock()
        self.Floor = 0
        self.RoomChange = False
        

   
    def Init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.ScreenSize, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.Running = True
        

        global MainPlayer
        global BubbleEnemy
        global Goal
        global ObjectList

        MainPlayer = Player()
        BubbleEnemy = BloodiBub([1850,375])
        BubbleEnemy.Mode = 1
        Goal = BloodiBub([1364,200])
        Goal.Mode = 0
        ObjectList = []

        if self.Floor != 0 and self.Floor != 1:
            self.floor = 0

        if self.Floor == 0:
            # Locked doors
            ODoor = Object(True, [110,20], True, "#FF7F27", [250,280], "Square", True, True, "Orange Key")
            GDoor = Object(True, [110,20], True, "#00FF00", [660,460], "Square", True, True, "Green Key")
            ESCDoor = Object(True, [120,20], True, "#00F3FF", [1364,280], "Square", True, True, "Blue Key")
            # Barriers
            Barrier = Object(True, [150,700], DebugBarriers, "#FFFF00", [874,800], "Square", False, False, "")
            Barrier = Object(True, [900,150], DebugBarriers, "#FFFF00", [1400,950], "Square", False, False, "")
            Barrier = Object(True, [150,900], DebugBarriers, "#FFFF00", [1850,500], "Square", False, False, "")
            Barrier = Object(True, [900,20], DebugBarriers, "#FFFF00", [1150,460], "Square", False, False, "")
            Barrier = Object(True, [900,20], DebugBarriers, "#FFFF00", [185,460], "Square", False, False, "")
            Barrier = Object(True, [140,8000], DebugBarriers, "#FFFF00", [0,600], "Square", False, False, "")
            Barrier = Object(True, [9000,140], DebugBarriers, "#FFFF00", [185,0], "Square", False, False, "")
            Barrier = Object(True, [1000,20], DebugBarriers, "#FFFF00", [800,280], "Square", False, False, "")
            Barrier = Object(True, [504,320], DebugBarriers, "#FFFF00", [1053,130], "Square", False, False, "")
            Barrier = Object(True, [504,320], DebugBarriers, "#FFFF00", [1675,130], "Square", False, False, "")
            Barrier = Object(True, [900,20], DebugBarriers, "#FFFF00", [2150,460], "Square", False, False, "")
            Barrier = Object(True, [1000,20], DebugBarriers, "#FFFF00", [-300,280], "Square", False, False, "")
            Barrier = Object(True, [7000,150], DebugBarriers, "#FFFF00", [0,1020], "Square", False, False, "")
            # Dropped Items
            BKey = Object(False, [20,20], True, "#00F3FF", [500, 200],"Square", True, False, "Blue Key")
            GKey = Object(False, [20,20], True, "#00FF00", [1750, 850],"Square", True, False, "Green Key")
            OKey = Object(False, [20,20], True, "#FF7F27", [500, 850],"Square", True, False, "Orange Key")
            

            
        
            
    
    def RunEvent(self, event):
        if event.type == pygame.QUIT:
            self.Running = False
        
        if self.RoomChange:
            if self.Floor == 0:
                self.Floor = 1
                self.RoomChange = False
                ObjectList.clear()
                BubbleEnemy.Rage += 5
                MainPlayer.Position[1] += 9
                BubbleEnemy.Position = [0,0]


        
            

    def MainLoop(self):
        
        BubbleEnemy.AI()
        Goal.AI()
        

        # Movement
        KeyPress = pygame.key.get_pressed()
        if KeyPress[pygame.K_UP]:
            CanMove = True
            GhostMove = MainPlayer.Position[1] - MainPlayer.Walkspeed
            for item in ObjectList:
                if not item.IsWall:
                    continue
                if MainPlayer.Position[0] in range(item.Position[0] - int(item.ObjectSize[0]/2),(item.Position[0] + int(item.ObjectSize[0]/2)) + 1) and GhostMove in range(item.Position[1] - int(item.ObjectSize[1]/2),(item.Position[1] + int(item.ObjectSize[1]/2)) + 1):
                    CanMove = False
                
            if CanMove:
                MainPlayer.Position[1] = GhostMove

        elif KeyPress[pygame.K_RIGHT]:
            CanMove = True
            GhostMove = MainPlayer.Position[0] + MainPlayer.Walkspeed
            for item in ObjectList:
                if not item.IsWall:
                    continue

                if GhostMove in range(item.Position[0] - int(item.ObjectSize[0]/2),(item.Position[0] + int(item.ObjectSize[0]/2)) + 1) and MainPlayer.Position[1] in range(item.Position[1] - int(item.ObjectSize[1]/2),(item.Position[1] + int(item.ObjectSize[1]/2)) + 1):
                    CanMove = False
            
            if CanMove:
                MainPlayer.Position[0] = GhostMove

        elif KeyPress[pygame.K_DOWN]:
            CanMove = True
            GhostMove = MainPlayer.Position[1] + MainPlayer.Walkspeed
            for item in ObjectList:
                if not item.IsWall:
                    continue
                if MainPlayer.Position[0] in range(item.Position[0] - int(item.ObjectSize[0]/2),(item.Position[0] + int(item.ObjectSize[0]/2)) + 1) and GhostMove in range(item.Position[1] - int(item.ObjectSize[1]/2),(item.Position[1] + int(item.ObjectSize[1]/2)) + 1):
                    CanMove = False
                
            if CanMove:
                MainPlayer.Position[1] = GhostMove

        elif KeyPress[pygame.K_LEFT]:
            CanMove = True
            GhostMove = MainPlayer.Position[0] - MainPlayer.Walkspeed
            for item in ObjectList:
                if not item.IsWall:
                    continue
                
                if GhostMove in range(item.Position[0] - int(item.ObjectSize[0]/2),(item.Position[0] + int(item.ObjectSize[0]/2)) + 1) and MainPlayer.Position[1] in range(item.Position[1] - int(item.ObjectSize[1]/2),(item.Position[1] + int(item.ObjectSize[1]/2)) + 1):
                    CanMove = False
          
            if CanMove:
                MainPlayer.Position[0] = GhostMove
        
        elif KeyPress[pygame.K_SPACE]:
            RemoveStore = []
            for item in ObjectList:
                if not item.IsUsable:
                    continue
                
                Distance = ((MainPlayer.Position[0] - item.Position[0])**2 + (MainPlayer.Position[1] - item.Position[1])**2)**0.5

                if Distance <= 70:
                    if item.IsLocked:
                        if item.ConnectedItem in MainPlayer.Inventory:
                            MainPlayer.Inventory.remove(item.ConnectedItem)
                            RemoveStore.append(item)
                            BubbleEnemy.Rage += 5
                    else:
                        MainPlayer.Inventory.append(str(item.ConnectedItem))
                        RemoveStore.append(item)
                        BubbleEnemy.Rage += 5
            if len(RemoveStore) > 0:
                for item in RemoveStore:
                    ObjectList.remove(item)

                


        
        wait(self.Clock.tick(60) / 1250)

    def Render(self):
        Instance._display_surf.fill("black")
        BackGroundImage = pygame.image.load(f"Assets\Textures\Maps\Floor{self.Floor}\Background.png")
        Instance._display_surf.blit(BackGroundImage, (-10,-25))

        
        
        for item in ObjectList:
                if item.ShapeType == "Square" and item.Visible == True:
                    pygame.draw.rect(Instance._display_surf, item.Colour, pygame.Rect(item.Position[0] - item.ObjectSize[0]/2, item.Position[1] - item.ObjectSize[1]/2, item.ObjectSize[0], item.ObjectSize[1]))
                elif item.ShapeType == "Circle" and item.Visible == True:
                    pygame.draw.circle(Instance._display_surf, item.Colour, item.Position, item.ObjectSize)
                else:
                    pass

        pygame.draw.circle(Instance._display_surf, "white", pygame.Vector2(MainPlayer.Position[0],MainPlayer.Position[1]), MainPlayer.size)
        pygame.draw.circle(Instance._display_surf, "red", pygame.Vector2(BubbleEnemy.Position[0],BubbleEnemy.Position[1]), BubbleEnemy.Size)
        pygame.display.flip()

    def CleanUp(self):
        exit()
    
    def Run(self):
        if self.Init() == False:
            self.Running = False
        while self.Running:
            for event in pygame.event.get():
                self.RunEvent(event)
            self.MainLoop()
            self.Render()
        self.CleanUp()
    
class Object():
    def __init__(self, IsInteractable, Size:list, Visible, Colour, Position:list, ShapeType, IsUsable, IsLocked, ConnectedItem):
        self.IsWall = IsInteractable # determines if the user can pass through or not, good for making decor
        self.ShapeType = ShapeType
        self.ObjectSize = Size # determines the object's size
        self.WallSize = self.ObjectSize
        self.Visible = Visible
        self.Colour = Colour
        self.IsUsable = IsUsable
        self.IsLocked = IsLocked
        self.ConnectedItem = ConnectedItem
        
        self.Position = Position
        
        ObjectList.append(self)

class Player:
    def __init__(self):
        self.size = 20
        self.Position = [100,375]
        self.Walkspeed = 10
        self.Inventory = []
        
    pass

class BloodiBub:
    def __init__(self, StartPos):
        self.IsPopped = False # determines if pop is stunned
        self.Position = StartPos # x,y on the screen
        self.Mode = 1 # determines the mode pop is in
        self.BaseSpeed = 1
        self.Rage = 0
        self.Size = 25
        self.DetectionRange = 300
    
    def AI(self):
        if self.IsPopped == True:
            self.Position = [100000,100000]
            return

        def Chase(Distance):
            
            if self.Rage >= 10 or Distance <= self.DetectionRange:
               
            
                NewDirection = [self.Position[0] - MainPlayer.Position[0], self.Position[1] - MainPlayer.Position[1]]

                if NewDirection[0]**2 > NewDirection[1]**2:
                    if NewDirection[0] > -1: #positive
                        self.Position[0] -= NewWalkSpeed
                    else: #negative
                        self.Position[0] += NewWalkSpeed

                elif NewDirection[0]**2 < NewDirection[1]**2:
                    if NewDirection[1] > -1: #positive
                        self.Position[1] -= NewWalkSpeed
                    else: #negative
                        self.Position[1] += NewWalkSpeed

                else:
                    RandomDirection = randint(0, 1)
                    if NewDirection[RandomDirection] > -1: #positive
                        self.Position[RandomDirection] -= NewWalkSpeed
                    else: #negative
                        self.Position[RandomDirection] += NewWalkSpeed
        
        NewWalkSpeed = self.BaseSpeed + (self.Rage + 1)*0.12

        Distance = abs(((self.Position[0] - MainPlayer.Position[0])**2 + (self.Position[1] - MainPlayer.Position[1])**2)**0.5)

        if self.Mode == 1:
            Chase(Distance)
        

            
        if Distance <= MainPlayer.size + self.Size:
            Instance.CleanUp()

        


if __name__ == "__main__": # runs the game
    Instance = Game()
    Instance.Run()