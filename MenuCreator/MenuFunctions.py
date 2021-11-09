from tkinter import *
from tkinter import filedialog, ttk
from tkinter import scrolledtext

import os

class CreateMenuFuncion:
    def __init__(self, instancia_de_Tk):
        print('MenuCriation')
        

class ErroBoxHandle:
    def __init__(self, instancia_de_Tk):
        self.num_linhas = 1
        self.ErroScrolledText = scrolledtext.ScrolledText( font=("Courier",10, "bold"),width=10, height=3, state='disabled')
        self.ErroTextValue = "Robot Simulator SAC: Simulation Analyze and Control"
        self.ErroScrolledText.configure(state='normal')
        self.ErroScrolledText.insert(INSERT, (str(self.num_linhas)+":"+self.ErroTextValue+"\n"))
        self.ErroScrolledText.configure(state='disabled')
        self.ErroScrolledText.pack(side = BOTTOM, anchor = "w", expand = True , fill = 'both' )
        
        self.num_linhas += 1
        
        self.ErroScrolledText.see('end')
        
    
    def ErroBoxAtualiza(self):
        self.ErroScrolledText.configure(state='normal')
        self.ErroScrolledText.insert(INSERT, (str(self.num_linhas)+":"+self.ErroTextValue+"\n"))
        self.ErroScrolledText.configure(state='disabled')
        self.ErroScrolledText.see('end')
        self.num_linhas += 1
        
class Tab(Frame):

    def __init__(self, root, name, textvalue):
        Frame.__init__(self, root)

        self.root = root
        self.name = name
        self.text = textvalue
        self.path = []

        self.textWidget = Text(self, undo = True)
        self.textWidget.insert(  INSERT, self.text)
        self.textWidget.pack(side = LEFT,anchor = "w" ,expand = True, fill= 'both')

    def save_tab(self):

        #file = open(filedialog.asksaveasfilename(), 'w+')
        self.path = filedialog.asksaveasfilename()
        self.name = os.path.basename(self.path)
        
        if self.name[len(self.name)-4:len(self.name)] != '.txt':
            self.name = self.name + '.txt'
            self.path = self.path + '.txt'
            
        file = open(self.path, 'w+')

        
        file.write(self.textWidget.get("1.0", 'end-1c'))
        
        file.close()
        return self.name