import numpy as np

def peca1():
    peca1_points =      np.array(([[0,0,0],
                                   [ 25,  50, 210],
                                   [ 25,  50, 255],
                                   [-25,  50, 255],
                                   [-25,  50, 210],
                                   [-25, 100, 255],
                                   [ 25, 100, 255],
                                   [-25, 100, 210],
                                   [ 25, 100, 210],
                                   [ 25, 100, 257],
                                   [-25, 100, 257],
                                   [-25,  25, 257],
                                   [ 25,  25, 257],
                                   [ 25,  25, 255],
                                   [-25,  25, 255],
                                   [-25,   0, 255],
                                   [ 25,   0, 255],
                                   [ 25,   0, -25],
                                   [-25,   0, -25],
                                   [-25,  50, -25],
                                   [ 25,  50, -25],
                                   [ 25,  50, 208],
                                   [-25,  50, 208],
                                   [-25, 100, 208],
                                   [ 25, 100, 208]]))
        
    peca1_linhas = [ [0, 0],
                     [1, 2],
                     [2, 3],
                     [4, 3],
                     [4, 1],
                     [3, 5],
                     [6, 5],
                     [2, 6],
                     [4, 7],
                     [8, 7],
                     [1, 8],
                     [6, 9],
                     [9, 10],
                     [5, 10],
                     [12, 11],
                     [11, 10],
                     [12, 9],
                     [13, 12],
                     [14, 11],
                     [13, 14],
                     [15, 14],
                     [16, 13],
                     [16, 15],
                     [17, 16],
                     [18, 15],
                     [17, 18],
                     [18, 19],
                     [20, 19],
                     [17, 20],
                     [20, 21],
                     [22, 21],
                     [19, 22],
                     [22, 23],
                     [24, 23],
                     [21, 24],
                     [24, 8],
                     [23, 7]]
    
    peca1_lineloop = [[1, 2, -3, 4],
                         [5, -6, -7, 2],
                         [8, -9, -10, -4],
                         [11, 12, -13, -6],
                         [14, 15, -12, -16],
                         [17, 14, -18, -19],
                         [20, -19, -21, 22],
                         [23, 22, -24, -25],
                         [25, 26, -27, -28],
                         [29, -30, -31, -27],
                         [32, -33, -34, -30],
                         [35, 9, -36, -33],
                         [29, 34, 35, -10, 1, 7, 11, -16, -17, -21, -23, 28],
                         [31, 32, 36, -8, 3, 5, 13, -15, -18, -20, -24, 26],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    
    peca1_verts_ind = [[]] #lista vazia
    peca1_verts = [[]]#lista vazia
    
    for i in range(np.size(peca1_lineloop)): #percorro todo o vetor de sequencia de linhas
        
    
        for j in range(np.size(peca1_lineloop[i])): #percorre a linha do lineloop
            
            if(j == 0): #se estou na primeira linha      
                peca1_verts_ind [i].append( peca1_linhas[ peca1_lineloop[i][j]  ][0])
                peca1_verts_ind [i].append( peca1_linhas[ peca1_lineloop[i][j]  ][1]) #se é o primeiro termo do vertica acrescento ambos os pontos
            
            elif(j != 0):
                if(peca1_lineloop[i][j] < 0):
                    peca1_verts_ind [i].append( peca1_linhas[ abs (peca1_lineloop[i][j] )  ][0]) #se indice negativo pego somente o segundo
                    
                if(peca1_lineloop[i][j] > 0):
                    peca1_verts_ind [i].append( peca1_linhas[      peca1_lineloop[i][j]    ][1]) #se indice positivo pego somento o primeiro termo
            
            peca1_verts[i].append( peca1_points[ peca1_verts_ind[i][j] ]) #acrescento o valor do ponto de indice calculado anteriormente
            
        peca1_verts_ind.append([])
        peca1_verts.append([])
        
    return peca1_verts