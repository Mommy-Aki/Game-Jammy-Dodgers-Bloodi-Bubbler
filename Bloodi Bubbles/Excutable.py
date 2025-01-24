import tkinter
import pathlib
from subprocess import run as Play
import PIL

class Version():
    def __init__(self):
        with open("Assets\Common\Version","r") as V:
            self.Version = V.read()

Program = Version()
SysVersion = Program.Version

class Background():
    def __init__(self):
        # Background Settings
        self.BackgroundColour = "#000000"
        self.ButtonColour = "#FF0000"
        self.ButtonTextColour = "#000000"
        self.TextColour = "#FF0000"
        self.IntroText = "Welcome! We at Game Jammy Dodgers are proud to present:"
        self.StartText = "Enter Purgetory"
        self.ControlText = "How To Escape..."
        self.Title = "Bloodi Bubbler"
        self.Logo = "Assets\Textures\Logo\Edited Logo.png"
        self.ControlMenuText = f"""
#################################
Controls:

Arrow Keys: Move
SpaceBar: Pick Up Key / Unlock Door

You must stay still to collect Items!
######################################
Instructions:

You have entered an abandoned school, a sanctuary for the mysterious murdered victims of a passed killer... But little do you know,
the killer's spirit seems to lurk with the 
######################################
Build: {SysVersion}


[Click to Return to the Menu!]



"""


    def Run(self,event):
        try:
            Play(["python","Services\GameService.py"])
        except:
            exit()
        Credits = tkinter.Tk()
        Credits.attributes("-topmost",True)
        Credits.attributes("-toolwindow",True)
        Credits.resizable(False,False)
        Credits.title("Credits")
        Credits.minsize(375,200)
        Credits.maxsize(375,200)
        NewBack = tkinter.Frame(master=Credits,bg=self.BackgroundColour,width=800,height=400)
        CreditText = f"""

        Build {SysVersion} Created By:

    Aki Webster: Programmer
    Tori Taylor: Graphical Artist and Map Designer
    Jake Seaman: Concept Designer
    Oliver Palmer: Graphical Artist

"""

        Credited = tkinter.Label(text=CreditText,bg=self.BackgroundColour,fg=self.TextColour, master = NewBack,)

        NewBack.place(x=0,y=0)
        Credited.place(x=0,y=0)
        Credits.mainloop()
        return

    def ViewControls(self, event):
            def ReRun(event):
                try:
                    Play(["python","Excutable.py"])
                    exit()
                except:
                    exit()

            ControlPannel = tkinter.Tk()
            ControlPannel.attributes("-fullscreen",True)
            # Assets to place
            NewBackground = tkinter.Frame(master=ControlPannel,bg=self.BackgroundColour,width=1945,height=1100)
            ControlLabel = tkinter.Label(text=self.ControlMenuText,master=NewBackground,bg=self.BackgroundColour,fg=self.TextColour)
            # Order of Assets being placed
            NewBackground.place(x=-20,y=-20)
            ControlLabel.place(x=700,y=300)
            NewBackground.bind("<Button-1>",ReRun)
            ControlLabel.bind("<Button-1>",ReRun)
            ControlPannel.mainloop()


    def Create(self,event):
        
            MainWindow = tkinter.Tk()
            MainWindow.attributes("-fullscreen",True)
            # Assets to place
            Background = tkinter.Frame(master=MainWindow,bg=self.BackgroundColour,width=1945,height=1100)
            MainText = tkinter.Label(text=self.IntroText,bg=self.BackgroundColour,fg=self.TextColour,master=Background)
            StartButton = tkinter.Button(text=self.StartText,master=Background,bg=self.ButtonColour,fg=self.ButtonTextColour,width=100,height=2)
            ControlButton = tkinter.Button(text=self.ControlText,master=Background,bg=self.ButtonColour,fg=self.ButtonTextColour,width=100,height=2)
            MainLogo = tkinter.PhotoImage(file=self.Logo)
            LogoImage = tkinter.Label(image=MainLogo,bg=self.BackgroundColour,master=Background)
            # Order of where the assets are placed
            Background.place(x=-20,y=-20)
            MainText.place(x=800,y=150)
            StartButton.place(x=650,y=900)
            StartButton.bind("<Button-1>",self.Run)
            ControlButton.place(x=650,y=1000)
            ControlButton.bind("<Button-1>",self.ViewControls)
            LogoImage.place(x=710,y=200)


            MainWindow.mainloop()

    
    

if __name__ == "__main__":
    Main = Background()
    Main.Create("x")