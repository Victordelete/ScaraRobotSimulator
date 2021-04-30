import numpy as np

def peca4():
    peca4_points = np.array([    [0   ,  0 ,   0],
                                 [-4.5, 391, 516],
                                 [-4.5, 391, 166],
                                 [-4.5, 399, 516],
                                 [-4.5, 399, 166],
                                 [3.5, 391, 166],
                                 [3.5, 391, 516],
                                 [3.5, 399, 516],
                                 [3.5, 399, 166],
                                 [0.5, 394, 166],
                                 [-1.5, 394, 166],
                                 [0.5, 396, 166],
                                 [-1.5, 396, 166],
                                 [0.5, 394, 514.75],
                                 [-1.5, 394, 514.75],
                                 [0.5, 396, 514.75],
                                 [-1.5, 396, 514.75] ])
    
    peca4_linhas = [ [0, 0],
                     [2, 1],
                     [1, 3],
                     [4, 3],
                     [2, 4],
                     [2, 5],
                     [5, 6],
                     [1, 6],
                     [3, 7],
                     [6, 7],
                     [4, 8],
                     [8, 7],
                     [5, 8],
                     [9, 10],
                     [9, 11],
                     [11, 12],
                     [10, 12],
                     [9, 13],
                     [14, 13],
                     [10, 14],
                     [13, 15],
                     [11, 15],
                     [16, 15],
                     [12, 16],
                     [14, 16]]
    
    peca4_lineloop = [[1, 2, -3, -4],
                         [5, 6, -7, -1],
                         [2, 8, -9, -7],
                         [10, 11, -8, -3],
                         [4, 10, -12, -5, 13, 16, -15, -14],
                         [6, 9, -11, -12],
                         [17, -18, -19, -13],
                         [17, 20, -21, -14],
                         [21, -22, -23, -15],
                         [19, 24, -23, -16],
                         [24, 22, -20, -18],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    
    peca4_verts_ind = [[]] #lista vazia
    peca4_verts = [[]]#lista vazia
    
    for i in range(np.size(peca4_lineloop)): #percorro todo o vetor de sequencia de linhas
        
    
        for j in range(np.size(peca4_lineloop[i])): #percorre a linha do lineloop
            
            if(j == 0): #se estou na primeira linha      
                peca4_verts_ind [i].append( peca4_linhas[ peca4_lineloop[i][j]  ][0])
                peca4_verts_ind [i].append( peca4_linhas[ peca4_lineloop[i][j]  ][1]) #se é o primeiro termo do vertica acrescento ambos os pontos
            
            elif(j != 0):
                if(peca4_lineloop[i][j] < 0):
                    peca4_verts_ind [i].append( peca4_linhas[ abs (peca4_lineloop[i][j] )  ][0]) #se indice negativo pego somente o segundo
                    
                if(peca4_lineloop[i][j] > 0):
                    peca4_verts_ind [i].append( peca4_linhas[      peca4_lineloop[i][j]    ][1]) #se indice positivo pego somento o primeiro termo
            
            peca4_verts[i].append( peca4_points[ peca4_verts_ind[i][j] ]) #acrescento o valor do ponto de indice calculado anteriormente
            
        peca4_verts_ind.append([])
        peca4_verts.append([])
        
    return peca4_verts