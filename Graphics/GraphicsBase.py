from tkinter import *

import numpy as np

from matplotlib.figure import Figure

from matplotlib.backend_bases import key_press_handler

import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk )

import VisualData.Peca1_dados
import VisualData.Peca2_dados
import VisualData.Peca3_dados
import VisualData.Peca4_dados


class GraphicsFunctions:
    def __init__(self, instancia_de_Tk):
         #angulo de variação da movimentação, via de regra é 1 mas acrescenta-se dessa forma para pode renderizar em variações 
        self.lista_instrucoes = []
        
        #maiores de angulo        
        self.delta1 = 1.0
        self.delta2 = 1.0
        self.delta3 = 1
        
        #variável que define a posição atual das juntas do robô
        self.teta1_atual = 0.0
        self.teta2_atual = 0.0
        self.altura3_atual = 0.0
        
        #variável que define a posição futura das juntas do robô
        self.teta1_novo = 0.0
        self.teta2_novo = 0.0
        self.altura3_novo = 0.0
        
        self.ref_ponto1 = np.array([0.0,65.0,280.0])
        self.ref_ponto2 = np.array([0.0,230.0,280.0])
        
        ##########################################
    
        self.fig = Figure(figsize=(8,5), dpi=110)

        self.canvas_robo = FigureCanvasTkAgg(self.fig, master = instancia_de_Tk)  # A tk.DrawingArea.
        self.canvas_robo.draw()
        
        self.ax = self.fig.add_subplot(111, projection="3d")

        #self.ax.add_collection3d(Poly3DCollection(self.verts))

        #self.ax.scatter3D(0.0,0.0,0.0)
        #self.ax.scatter3D(400,400.0,350.0)
        #self.ax.scatter3D(-400.0,400.0,350.0)
        
        self.ax.add_collection3d(Poly3DCollection(peca4_verts, 
         facecolors='orange', linewidths=1, edgecolors='k', alpha=.2)) 
        
        self.ax.add_collection3d(Poly3DCollection(peca3_verts, 
         facecolors='blue', linewidths=1, edgecolors='k', alpha=.9))

        self.ax.add_collection3d(Poly3DCollection(peca2_verts, 
         facecolors='yellow', linewidths=1, edgecolors='k', alpha=.9))

        self.ax.add_collection3d(Poly3DCollection(peca1_verts, 
         facecolors='green', linewidths=1, edgecolors='k', alpha=.9))
        
        
        self.canvas_robo.get_tk_widget().pack(side=TOP , fill=BOTH, expand=1)
        
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=2)
        
        self.ani.event_source.stop() #movimentação inicia parada
        
        self.ani_state = False
        
    def moving_stop(self):
        self.ani.event_source.stop()
        self.ani_state = False
        
    def moving_start(self):
        self.ani.event_source.start()
        self.ani_state = True

    #def move_handle_funtion(self, move_kind, new_point):
    def move_handle_funtion(self, lista_instrucoes):
        
        self.lista_instrucoes = lista_instrucoes
        
        self.InterpretaInit()
        
        #rearranjo o novos pontos de movimentação
        
        #inicio a movimentação
        self.moving_start()
        
        
####################################################################

    #função para animar
    def animate(self, i ):
        #eixos a serem movimentados
        movimento1 = 0
        movimento2 = 0
        movimento3 = 0
        
        temp = [[]]
        
        #se eu estiver com movimento acionado para 1
        if self.teta1_novo != self.teta1_atual:
            if self.teta1_novo > self.teta1_atual:
                self.teta1_atual += abs(self.delta1) #adiciono a varação minima de teta1
                self.delta1 = abs(self.delta1)       #a variação é positiva
                
            if self.teta1_novo < self.teta1_atual:
                self.teta1_atual -= abs(self.delta1) #retiro a varação minima de teta1
                self.delta1 = (-1)*abs(self.delta1)       #a variação é negativa
            movimento1 = 1
            
        if self.teta2_novo != self.teta2_atual:
            if self.teta2_novo > self.teta2_atual:
                self.teta2_atual += abs(self.delta2) #adiciono a varação minima de teta2
                self.delta2 = abs(self.delta2)       #a variação é positiva
                
            if self.teta2_novo < self.teta2_atual:
                self.teta2_atual -= abs(self.delta2) #retiro a varação minima de teta2
                self.delta2 = (-1)*abs(self.delta2)       #a variação é negativa
            movimento2 = 1
            
        if self.altura3_novo != self.altura3_atual:
            if self.altura3_novo > self.altura3_atual:
                self.altura3_atual += abs(self.delta3) #adiciono a varação minima de altura3
                self.delta3 = abs(self.delta3)       #a variação é positiva
                
            if self.altura3_novo < self.altura3_atual:
                self.altura3_atual -= abs(self.delta3) #retiro a varação minima de altura3
                self.delta3 = (-1)*abs(self.delta3)       #a variação é negativa
            movimento3 = 1
            
        #se acabar minhas instruções a serem executadas
        if len(self.lista_instrucoes) == 0:
            self.moving_stop()
            
        #analiso se tem movimento da instrução anterior
        if movimento1 == 0 and movimento2 == 0 and movimento3 == 0 and len(self.lista_instrucoes) != 0:
            #excluo o primeiro item de instrução
            self.lista_instrucoes = self.lista_instrucoes[1:len(self.lista_instrucoes)]
            
            #se não houver mais instruções eu paro a movimentação
            if len(self.lista_instrucoes) != 0:
                self.InterpretaInit()
            
                        
            if len(self.lista_instrucoes) == 0:
                self.moving_stop()
       
        #limpa a tela
        self.ax.clear()
        
        #define limites para o ambiente de trabalho
        self.ax.scatter3D(0,-400,0, facecolors = "black", alpha = 0.0) ###importante usar um volume quadrado para não deformar a visão durante movimento
        self.ax.scatter3D(400,400,350, facecolors = "black", alpha = 0.0)
        self.ax.scatter3D(-400,400,350, facecolors = "black", alpha = 0.0)
        
        #self.ax.plot([0,400,0], [0,0,0],color='black')#linewidths=1, edgecolors='k', alpha=.9
        #self.ax.plot([0,-400,0], [0,0,0],color='black')
        
        #impressão de ponto de referencia para movimentação dos elos
        #self.ax.scatter3D(200+self.ref_ponto2[0], self.ref_ponto2[1], self.ref_ponto2[2], facecolors = "black" )
        
        if movimento1 == 1 :
            #movento o braço 1 em relação ao ponto fixo [0,65,280] self.ref_ponto1
            for i in range(len(peca2_verts)):
                for j in range(len(peca2_verts[i])):
                    peca2_verts[i][j] = peca2_verts[i][j] - self.ref_ponto1
                    peca2_verts[i][j] = self.rotacionando(peca2_verts[i][j], self.delta1)
                    peca2_verts[i][j] = peca2_verts[i][j] + self.ref_ponto1
                    
            #movento o braço 1 em relação ao ponto fixo [0,65,280]
            for i in range(len(peca3_verts)):
                for j in range(len(peca3_verts[i])):
                    peca3_verts[i][j] = peca3_verts[i][j] - self.ref_ponto1
                    
                    peca3_verts[i][j] = self.rotacionando(peca3_verts[i][j], self.delta1)
                    
                    peca3_verts[i][j] = peca3_verts[i][j] + self.ref_ponto1
            
            #movento o braço 1 em relação ao ponto fixo [0,65,280]
            for i in range(len(peca4_verts)):
                for j in range(len(peca4_verts[i])):
                    peca4_verts[i][j] = peca4_verts[i][j] - self.ref_ponto1
                    peca4_verts[i][j] = self.rotacionando(peca4_verts[i][j], self.delta1)
                    peca4_verts[i][j] = peca4_verts[i][j] + self.ref_ponto1
            
            #corrigindo posicionamento do ponto de referencia
            self.ref_ponto2 = self.ref_ponto2 - self.ref_ponto1
            self.ref_ponto2 = self.rotacionando(self.ref_ponto2 , self.delta1) #rotacionando ponto de referencia 2
            self.ref_ponto2 = self.ref_ponto2 + self.ref_ponto1
            
#######################################################################################
        #movimento do braço 2 em relação ao ponto fixo [0, 230, 280]
        if movimento2 == 1 :           
            #movento o braço 1 em relação ao ponto fixo [0, 230, 280]
            for i in range(len(peca3_verts)):
                for j in range(len(peca3_verts[i])):
                    peca3_verts[i][j] = peca3_verts[i][j] - self.ref_ponto2
                    peca3_verts[i][j] = self.rotacionando(peca3_verts[i][j], self.delta2)
                    peca3_verts[i][j] = peca3_verts[i][j] + self.ref_ponto2 
            
            #movento o braço 1 em relação ao ponto fixo [0,65,280]
            for i in range(len(peca4_verts)):
                for j in range(len(peca4_verts[i])):
                    peca4_verts[i][j] = peca4_verts[i][j] - self.ref_ponto2 
                    peca4_verts[i][j] = self.rotacionando(peca4_verts[i][j], self.delta2)
                    peca4_verts[i][j] = peca4_verts[i][j] + self.ref_ponto2 
                    
#######################################################################################
        #movimento do braço 3
        if movimento3 == 1:
            #movento o braço 1 em relação ao ponto fixo [0,65,280]
            for i in range(len(peca4_verts)):
                for j in range(len(peca4_verts[i])):
                    peca4_verts[i][j] = peca4_verts[i][j] - [0, 0, self.delta3]

        
        #imprimindo os vertices na tela
        self.ax.add_collection3d(Poly3DCollection(peca4_verts, 
         facecolors='orange', linewidths=1, edgecolors='k', alpha=.2)) 
        
        self.ax.add_collection3d(Poly3DCollection(peca3_verts, 
         facecolors='blue', linewidths=1, edgecolors='k', alpha=.9))

        self.ax.add_collection3d(Poly3DCollection(peca2_verts, 
         facecolors='yellow', linewidths=1, edgecolors='k', alpha=.9))

        self.ax.add_collection3d(Poly3DCollection(peca1_verts, 
         facecolors='green', linewidths=1, edgecolors='k', alpha=.9))
        
        
    #######################
    def rotacionando(self, ponto_rot, new_angulo):        
        ang = new_angulo
        
        #matriz de rotação, quando for mudar tem que generalizar para o robô.
        matriz_rot = np.array([[np.cos(ang*(np.pi/180)) , -np.sin(ang*(np.pi/180)) ,0   , 0],
                               [np.sin(ang*(np.pi/180)) , np.cos(ang*(np.pi/180))  ,0   , 0],
                               [0                       , 0                        ,1   , 0],
                               [0                       , 0                        ,0   , 1]])
            
        new_ponto = np.zeros((8,4))
        
        #multiplicando o ponto pela matriz de rotação
        new_ponto = self.multi_matriz(ponto_rot, matriz_rot)
            
        return new_ponto[0:3]
    
    #multiplica um vetor por uma matriz 3x3
    def multi_matriz(self, vetor, matriz):
        new_vetor = np.zeros(4)
        
        #multiplicação de matriz, fiz com só um loop para se precisar mudar em um único índice
        for i in [0,1,2,3]:
            new_vetor[i] = vetor[0]*matriz[i][0] +vetor[1]*matriz[i][1] + vetor[2]*matriz[i][2] +1*matriz[i][3]
        
        return new_vetor
            
    ###################################3##############################################

    def InterpretaInit(self):
        
        #Função move
        if self.lista_instrucoes[0][0] == 1 :
            #uso angulo direto
            self.teta1_novo = self.lista_instrucoes[0][1]
            self.teta2_novo = self.lista_instrucoes[0][2]
            self.altura3_novo = self.lista_instrucoes[0][3]
        
        #função pmove
        if self.lista_instrucoes[0][0] == 2:
            #funcao que transforma a posição em teta para o robo
            self.Cinematica_inversa()
            #a altura não muda nessa posição
            self.altura3_novo = self.lista_instrucoes[0][3]
            
        #função up
        if self.lista_instrucoes[0][0] == 3:
            self.teta1_novo = self.teta1_atual
            self.teta2_novo = self.teta2_atual
            self.altura3_novo =  0 #altura máxima
            
            
        #função down
        if self.lista_instrucoes[0][0] == 4:
            #ponto mais baixo do 
            self.teta1_novo = self.teta1_atual
            self.teta2_novo = self.teta2_atual
            self.altura3_novo =  160 #altura máxima
            
        #função delay
        if self.lista_instrucoes[0][0] == 5:
            print('delay')
            
        #função home
        if self.lista_instrucoes[0][0] == 6:
            #volta para o estado inicial, chamar no final do programa.
            self.teta1_novo = 0
            self.teta2_novo = 0
            self.altura3_novo =  0
            
        if self.lista_instrucoes[0][0] == 7:
            print('lmove')
            
        #função zmove
        if self.lista_instrucoes[0][0] == 8:
            self.teta1_novo = self.teta1_atual
            self.teta2_novo = self.teta2_atual
            self.altura3_novo =  self.lista_instrucoes[0][1] #altura máxima
                        
    
    def Cinematica_inversa(self):
        x = self.lista_instrucoes[0][1]
        y = self.lista_instrucoes[0][2]
        
        #consertando para origem
        x = x-65
    
        #assumindo compilação correta e o ponto esta na área de trabalho
        #primeiro o segundo angulo
        t2n = np.arccos((pow(x,2)+ pow(y,2) - pow(174,2) - pow(140,2)) / (2*140*174))
        
        #k = 0
        
        if y<0:
            t2n = abs(t2n)
            #k = 1
            y = abs(y)
        
        #calculo um valor possível para teta1 e testo para saber se é válido
        num = y*(174+140*np.cos(t2n) )  - x*140*np.sin(t2n)
        den = x*(174+140*np.cos(t2n) )  + y*140*np.sin(t2n)
        
        #soma de offset para evitar divisão por zero. A resposta sai correta mas é bom evitar.
        t1n = np.arctan(num/(den+0.0001))
            
        self.teta1_novo = round(t1n*(180/np.pi), 0)
        self.teta2_novo = round(t2n*(180/np.pi), 0)
        
peca1_verts = VisualData.Peca1_dados.peca1()
peca2_verts = VisualData.Peca2_dados.peca2()
peca3_verts = VisualData.Peca3_dados.peca3()
peca4_verts = VisualData.Peca4_dados.peca4()