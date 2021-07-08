


import tkinter as tk 
import threading

class MyWindow(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self) # <=> super().__init__()
        
        self.minsize(500,200)
        self.title("Just a test")
        
        
        
        self.counter=tk.IntVar()
        self.counter.set(0)
        
        nameL=tk.Label(self, text="Counter:")
        # Geometry Manager: placer, packer, gridder
        
        nameL.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        
        nameE=tk.Entry(self, textvariable=self.counter)
        nameE.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        
        clickB=tk.Button(self, text="start", command=self.start)
        clickB.grid(row=0, column=2, padx=10, pady=10)
        
        clearB=tk.Button(self, text="stop", command=self.stop)
        clearB.grid(row=0, column=3, padx=10, pady=10)
        
        self.loop=threading.Thread(target=self.worker)
        
        self.okToRun=True
        self.setMenu()
        
    def setMenu(self):
        import sys
        mainmenu = tk.Menu(self)  # MenuBar
         
        menuFile = tk.Menu(mainmenu)  # Menu File
        menuFile.add_command(label="Open", command=self.openFile)
        menuFile.add_command(label="Quit", command=sys.exit) 
  
        menuHelp = tk.Menu(mainmenu) # Menu Help
        menuHelp.add_command(label="About", command=self.about) 
        
        mainmenu.add_cascade(label = "File", menu=menuFile) 
        mainmenu.add_cascade(label = "Help", menu=menuHelp)
        
        # display the menu
        self.config(menu = mainmenu) 

    def about(self): 
        pass
    def worker(self):
        import time
        while self.okToRun:
            self.counter.set(self.counter.get()+1)
            time.sleep(1)
            
    def start(self): 
        if self.loop == None:
            self.loop=threading.Thread(target=self.worker)
            self.okToRun=True
            
        self.loop.start()
            
    def stop(self): 
        self.okToRun=False
        self.loop=None
        
    def hello(self):
        print("Hello", self.nameStr.get())
        
    def clear(self):
        self.nameStr.set("")
        self.telStr.set("")
        
    def openFile(self): 
        pass
              
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
