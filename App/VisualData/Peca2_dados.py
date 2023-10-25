import numpy as np

def peca2():
    peca2_points = [  [ 0 ,  0 ,   0],
                               [-25,  63, 255],
                               [-25, 178, 255],
                               [ 25, 178, 255],
                               [ 25,  63, 255],
                               [ 25,  63, 210],
                               [-25,  63, 210],
                               [ 23,  63, 253],
                               [ 23,  63, 212],
                               [-23,  63, 212],
                               [-23,  63, 253],
                               [-25, 178, 210],
                               [ 25, 178, 210],
                               [ 25, 178, 208],
                               [-25, 178, 208],
                               [-25, 253, 208],
                               [ 25, 253, 208],
                               [ 25, 253, 210],
                               [-25, 253, 210],
                               [-25, 203, 210],
                               [ 25, 203, 210],
                               [ 25, 203, 255],
                               [-25, 203, 255],
                               [ 23, 203, 253],
                               [ 23, 203, 212],
                               [-23, 203, 212],
                               [-23, 203, 253],
                               [-25, 253, 255],
                               [ 25, 253, 255],
                               [ 25, 178, 257],
                               [-25, 178, 257],
                               [ 25, 253, 257],
                               [-25, 253, 257]]
    
    peca2_linhas = [ [0, 0],
                     [1, 2],
                     [3, 2],
                     [4, 3],
                     [4, 1],
                     [5, 4],
                     [5, 6],
                     [6, 1],
                     [8, 7],
                     [8, 9],
                     [9, 10],
                     [7, 10],
                     [6, 11],
                     [12, 11],
                     [5, 12],
                     [13, 12],
                     [14, 11],
                     [13, 14],
                     [14, 15],
                     [16, 15],
                     [13, 16],
                     [16, 17],
                     [17, 18],
                     [15, 18],
                     [19, 18],
                     [20, 17],
                     [20, 19],
                     [20, 21],
                     [21, 22],
                     [19, 22],
                     [24, 23],
                     [24, 25],
                     [25, 26],
                     [23, 26],
                     [22, 27],
                     [28, 27],
                     [21, 28],
                     [8, 24],
                     [7, 23],
                     [9, 25],
                     [10, 26],
                     [3, 29],
                     [29, 30],
                     [2, 30],
                     [28, 31],
                     [31, 32],
                     [27, 32],
                     [30, 32],
                     [29, 31]]
    
    peca2_lineloop = [[1, -2, -3, 4],
                         [5, 4, -7, -6, 8, 11, -10, -9],
                         [12, -13, -14, 6],
                         [15, 13, -16, -17],
                         [17, 18, -19, -20],
                         [21, 22, -23, -19],
                         [24, -22, -25, 26],
                         [27, 28, -29, -26, 30, 33, -32, -31],
                         [34, -35, -36, 28],
                         [37, 30, -38, -8],
                         [9, 39, -31, -37],
                         [39, 32, -40, -10],
                         [11, 40, -33, -38],
                         [41, 42, -43, -2],
                         [44, 45, -46, -35],
                         [42, 47, -45, -48],
                         [14, -15, 20, 21, -25, 27, 36, 44, -48, -41, -3, -5],
                         [12, -16, 18, 23, -24, 29, 34, 46, -47, -43, -1, -7],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
    
    peca2_verts_ind = [[]] #lista vazia
    peca2_verts = [[]]#lista vazia
    
    for i in range(len(peca2_lineloop)): #percorro todo o vetor de sequencia de linhas
        
    
        for j in range(len(peca2_lineloop[i])): #percorre a linha do lineloop
            
            if(j == 0): #se estou na primeira linha      
                peca2_verts_ind [i].append( peca2_linhas[ peca2_lineloop[i][j]  ][0])
                peca2_verts_ind [i].append( peca2_linhas[ peca2_lineloop[i][j]  ][1]) #se é o primeiro termo do vertica acrescento ambos os pontos
            
            elif(j != 0):
                if(peca2_lineloop[i][j] < 0):
                    peca2_verts_ind [i].append( peca2_linhas[ abs (peca2_lineloop[i][j] )  ][0]) #se indice negativo pego somente o segundo
                    
                if(peca2_lineloop[i][j] > 0):
                    peca2_verts_ind [i].append( peca2_linhas[      peca2_lineloop[i][j]    ][1]) #se indice positivo pego somento o primeiro termo
            
            peca2_verts[i].append( peca2_points[ peca2_verts_ind[i][j] ]) #acrescento o valor do ponto de indice calculado anteriormente
            
        peca2_verts_ind.append([])
        peca2_verts.append([])
    
    del peca2_verts[-1]
    return peca2_verts
