from Tkinter import *

class Application(Frame):
    def Kai(self):
        self.FAHAD.pack_forget()

    def createLables(self):

        w = Label(root, text="Fahad") 	# Creates a label with words
        w.pack({"side":"top"}) 

        w = Label(root, text = "Press the botton with your name on it")
        w.pack({"side":"top"})

    def createWidjects(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side":"left"})

        self.KAI = Button(self) 
        self.KAI["text"] = "Happy birthday"
        self.KAI["command"] = self.Kai

       
        self.FAHAD = Button(master=None, text="Fahad", command= self.Fahad)
       
        self.FAHAD.pack({"side":"top"})

    def Fahad(self):
        self.KAI.pack({"side":"left"}) # Creats the Kai label through the command     

        

    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidjects()
        self.createLables()

root = Tk()
root.title("First app")
app = Application(master = root)
app.mainloop()
root.destroy()
