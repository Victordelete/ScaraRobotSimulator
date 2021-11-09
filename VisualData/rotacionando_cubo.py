import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

#função para animar
def animate(i):
    global Z
    global angulo

    #rotação lenta de 1 grau de acrescimo por vez. A velocidade é a velocidade de recalculo
    angulo = angulo + 1
    
    #ponto de referencia para rotação
    Z = Z - a
    
    #chamando função de rotação para o novo posicionamento do cubo
    Z = rotacionando(angulo)
    
    #ponto de referencia para rotação
    Z = Z + a
    
    #
    if angulo == 5:
        angulo = 0
        
    Zt = Z[0:8 , 0:3]
    
    
    #pego somente os vertices necessários para construção da imagem    
    verts = [[Zt[0],Zt[1],Zt[2],Zt[3]],
             [Zt[4],Zt[5],Zt[6],Zt[7]], 
             [Zt[0],Zt[1],Zt[5],Zt[4]], 
             [Zt[2],Zt[3],Zt[7],Zt[6]], 
             [Zt[1],Zt[2],Zt[6],Zt[5]],
             [Zt[4],Zt[7],Zt[3],Zt[0]]]


    # limpa a tela
    ax.clear()
    
    #limitando limites de plotagem
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.set_zlim(-4,4)
    
    #imprimindo os vertices na tela
    ax.add_collection3d(Poly3DCollection(verts, 
     facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    #nomeando os eixos do gráfico
    plt.title('ROTACIONANDO CUBO')
    plt.ylabel('Ylabel')
    plt.xlabel('Xlabel')
    
#######################3
def rotacionando(new_angulo):
    global Z
    global angulo
    global a
    
    #matriz de rotação, quando for mudar tem que generalizar para o robô.
    matriz_rot = np.array([[np.cos(angulo*(np.pi/180)) , -np.sin(angulo*(np.pi/180)),0    , 0],
                           [np.sin(angulo*(np.pi/180)) , np.cos(angulo*(np.pi/180)),  0   , 0],
                           [0                          , 0                         , 1    , 0                           ],
                           [0                          , 0                         , 0    , 1                           ]])
        
    new_Z = np.zeros((8,4))
    
    #multiplicando todos os pontos do desenho, se aumentar tem que trocar o 8 por length de Z
    for i in range(8):
        new_Z[i] = multi_matriz(Z[i], matriz_rot)
    return new_Z

#multiplica um vetor por uma matriz 3x3
def multi_matriz(vetor, matriz):
    new_vetor = np.zeros(4)
    
    #multiplicação de matriz, fiz com só um loop para se precisar mudar em um único índice
    for i in [0,1,2,3]:
        new_vetor[i] = vetor[0]*matriz[i][0] +vetor[1]*matriz[i][1] + vetor[2]*matriz[i][2] +1*matriz[i][3]
    
    return new_vetor    

#variaveis globais para serem trabalhadas no programa 
angulo = 0
a = 2
        
Z = np.array([[-1+a, -1+a,-1+a, 1],
              [1+a, -1+a, -1+a, 1 ],
              [1+a, 1+a, -1+a , 1],
              [-1+a, 1+a, -1+a, 1],
              [-1+a, -1+a, 1+a, 1],
              [1+a, -1+a, 1+a , 1],
              [1+a, 1+a, 1+a  , 1],
              [-1+a, 1+a, 1+a , 1]])


#definindo a figura e a imagem para apresentar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# altere o valor do interval para que que o frame seja atualizado de maneira mais rápida ou não
ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()