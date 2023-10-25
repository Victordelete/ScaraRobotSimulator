# -*- coding: utf-8 -*-
"""
Criado em 08/11/2021

@author: Victor Hugo Marques
Modelo 16

Funções já funcionando
Acrescimo de handle de arquivo
Funcionamento da simulação
Funciomento do controle
Handle de erros do compilador
"""

#IMPORTAR ARQUIVOS E FONTES  
from tkinter import *
from tkinter import filedialog, ttk

import os
import MenuCreator.MenuFunctions

import Graphics.GraphicsBase

import Compilador.CompilateBase

class Janela:
    def __init__(self, instancia_de_Tk):
        instancia_de_Tk.title('RSAC: Robot Simulation Analyze and Control')
        instancia_de_Tk.geometry('1366x768')
        
        principal=Menu(instancia_de_Tk)
        #Itens para FILE
        Files=Menu(principal)
        Files.add_command(label="New",command=self.New)
        Files.add_command(label="Open",command=self.Open)
        Files.add_command(label="Save",command=self.Save)
        Files.add_command(label="Close",command=instancia_de_Tk.destroy)
        principal.add_cascade(label="Files",menu=Files)
        
        #Itens para TOOLS
        Tools=Menu(principal)
        Tools.add_command(label="Debug",command=self.Debug)
        Tools.add_command(label="Compilate",command=self.Compilate)
        Tools.add_command(label="Simulate",command=self.Simulate)
        Tools.add_command(label="Control",command=self.Control)
        principal.add_cascade(label="Tools",menu=Tools)
        
        #Itens para OPTIONS
        Options=Menu(principal)
        Options.add_command(label="Serial Port Close",command=self.SerialPortClose)
        Options.add_command(label="Simulation Test",command=self.SimulationTest)
        Options.add_command(label="Control Test",command=self.ControlTest)
        principal.add_cascade(label="Options",menu=Options)
        
        #Item para HELP
        principal.add_command(label="Help",command=self.Help)
        
        #SETANDO AS CONFIGURAÇÕES DE MENU
        instancia_de_Tk.configure(menu=principal)
        
        #####################################################################         
        #CAIXA DE TEXTO
        self.tabs = {'ky': 0}
        #Keep a record of the open tabs in a list.
        self.tab_list = []
        self.notebook = ttk.Notebook(instancia_de_Tk)
        self.notebook.pack(side = LEFT,anchor = "w" ,expand = True, fill= 'both')
            
        ##################################################################### 
        #CAIXA PARA DEMONSTRAÇÃO DE ERRO        
        self.ErroBox = MenuCreator.MenuFunctions.ErroBoxHandle(instancia_de_Tk)
        
        ##################################################################### 
        #VISÃO DO ROBÔ
        self.graphicsVar = Graphics.GraphicsBase.GraphicsFunctions(instancia_de_Tk)
        
        ##################################################################### 
        #objeto interna de compilação
        self.CompilateText = Compilador.CompilateBase.CompilateFunction(instancia_de_Tk )

        
    #####################################################################        
    #DEFINIÇÕES DO ITEM FILE
    def New(self):
        textvalue = ""
        
        if self.tabs['ky'] < 20:
            self.tabs['ky'] += 1
            self.add_tab('Document' + str(self.tabs['ky']), textvalue)
        #seleciono para visão o arquivo novo
        self.notebook.select(self.notebook.index('end')-1)
    
    def add_tab(self, name, textvalue):
        tab = MenuCreator.MenuFunctions.Tab(self.notebook, name , textvalue)
        self.notebook.add(tab, text=name)
        self.tab_list.append(tab)
     
    def get_tab(self):
        #pega a tab da tablist
        tab = self.tab_list[self.notebook.index('current')]
        return tab   
        
    def Open(self):
        file = open(filedialog.askopenfilename(), 'r+')
        self.text_value = file.read()
        title = os.path.basename(file.name)
        self.add_tab(title, self.text_value ) #crio uma nova tab para o arquivo aberto
        self.notebook.select( self.notebook.index('end')-1)
        
        file.close()
        
    def Save(self) :
        tab_to_save = self.get_tab()
        
        self.tab_list[self.notebook.index('current')].name = tab_to_save.save_tab()
        self.notebook.tab( self.notebook.index('current') , text = self.tab_list[self.notebook.index('current')].name )
        
    
    ##################################################################### 
    #DEFINIÇÕES DO ITEM TOOLS
    def Debug(self):
        print("Debug") 
        
    def Compilate(self):
        #salvo para garantir que nao tera mudanças
        #imprimo mensagem de salve
        self.ErroBox.ErroTextValue = ("Deseja salvar o arquivo "+self.tab_list[self.notebook.index('current')].name+":")
        self.ErroBox.ErroBoxAtualiza()
        self.Save()
        
        #imprimo mensagem de compilação
        self.ErroBox.ErroTextValue = ("Arquivo "+self.tab_list[self.notebook.index('current')].name+" salvo com sucesso.")
        self.ErroBox.ErroBoxAtualiza()
        
        #compilando arquivo
        #mensagem de compilação
        self.ErroBox.ErroTextValue = ("Compilando o arquivo "+self.tab_list[self.notebook.index('current')].name+ ".")
        self.ErroBox.ErroBoxAtualiza()
        
        #declaro novo objeto ou atualizo para conter o esperado da compilação
        self.CompilateText.InicioCompilacao(self.tab_list[self.notebook.index('current')].name)

        #imprimo mensagem de compilação
        self.ErroBox.ErroTextValue = ("Arquivo compilado com sucesso.\n")
        self.ErroBox.ErroBoxAtualiza()
        
        
    def Simulate(self) :
        self.ErroBox.ErroTextValue = "Preparando movimentação do robo."
        self.ErroBox.ErroBoxAtualiza()
        
        self.ErroBox.ErroTextValue = "Robo em movimento..."
        self.ErroBox.ErroBoxAtualiza()
        
        self.graphicsVar.controle = 0
        
        self.graphicsVar.move_handle_funtion(self.CompilateText.list_lines_comp)
            
        if self.graphicsVar.ani_state == False:
            self.ErroBox.ErroTextValue = "Movimento finalizado.\n"
            self.ErroBox.ErroBoxAtualiza()
       
        
    def Control(self):        
        self.ErroBox.ErroTextValue = "Preparando movimentação do robo."
        self.ErroBox.ErroBoxAtualiza()
        
        self.ErroBox.ErroTextValue = "Robo em movimento..."
        self.ErroBox.ErroBoxAtualiza()
        
        self.graphicsVar.controle = 1
        
        self.graphicsVar.porta_serial = serial.Serial('COM6', 57600)
        
        self.graphicsVar.move_handle_funtion(self.CompilateText.list_lines_comp)
            
        if self.graphicsVar.ani_state == False:
            self.ErroBox.ErroTextValue = "Movimento finalizado.\n"
            self.ErroBox.ErroBoxAtualiza()      
        

    #####################################################################  
    #DEFINIÇÕES DO ITEM OPTIONS
    def SerialPortClose(self):
        self.graphicsVar.porta_serial.close()
        #Fecho a porta serial
        
    def SimulationTest(self):
        print("SimulationTest")
        
    def ControlTest(self):
        print("ControlTest")
        self.tab_list[0].Tab.textWidget()
        
    #####################################################################         
    def Help(self) :
        self.ErroBox.ErroTextValue = ("You can read the manual contacting:\n  victorh_delete@hotmail.com\n")
        self.ErroBox.ErroBoxAtualiza()

raiz = Tk()
Janela(raiz)
raiz.mainloop()