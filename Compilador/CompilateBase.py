
#Base de funções para programação
#como são poucas coloquei em variável, mas pode-se colocar como aquivo também
BaseFuncoes =  [['move', 1], #criando arco que deverá ser definido
                ['pmove', 2],#movendo de
                ['up', 3], #movendo para cima
                ['down', 4],#movendo para baixo
                ['delay', 5],#pausa no sistema
                ['home', 6],#o pondo onde será iniciado
                ['lmove', 7],#movendo de forma linear
                ['zmove', 8],#movendo uma altura especifica, sem alterar o restante
                ['end', 100]]


class CompilateFunction:
    def __init__(self, instancia_de_Tk):
        #declaro uma lista vazia para ter acesso depois
        self.list_lines_comp = [[]]
        self.erro_ind = 0
        
    def InicioCompilacao(self, ArquivoBase):
        #abre o arquivo
        file = open(ArquivoBase,"r")
        
        #todas as linhas do arquivo do usuario
        list_lines = file.read()
        file.close()
        
        #separo em linhas a string completa
        self.list_lines_comp = list_lines.split('\n')
        
        #interpretação semantica e sintatica
        self.list_lines_comp = self.pre_process(self.list_lines_comp)
        
        #separo as linhas em palavras simples 
        for i in range(len(self.list_lines_comp)):
            self.list_lines_comp[i] = self.list_lines_comp[i].split()
        
        ################################
        #indice utilizado para indicar erro na interpretação
        ind_erro = 0
        
        #Transformando as funcoes em simbolos numericos
        for i in range(len(self.list_lines_comp)):
            ind_erro = 1
            
            for j in range(len(BaseFuncoes)):
                #comparando as funcoes do usuario com o padrao de compilacao
                if BaseFuncoes[j][0] == self.list_lines_comp[i][0]:
                    self.list_lines_comp[i][0] = BaseFuncoes[j][1]
                    ind_erro = 0
                    break
                
            #caso ind erro nao se alterou é porque há um erro na linha em questão
            if ind_erro == 1 :
                print('Erro encontrado na linhas', i+1) #corrigindo para linhas com indice inicial 1
                break
                
        #transformo todas as variaveis de texto para float
        for i in range(len(self.list_lines_comp)):
            for j in range(len(self.list_lines_comp[i])):
                self.list_lines_comp[i][j] = float(self.list_lines_comp[i][j])
                
        ################################
        #analise semântica
                
        ###############################
        #ligação posteriormente
                    #fazer uma compilaçao unica interno ao programa.
                    
        
                
    def pre_process(self, list_lines_comp):
        #eliminando linhas em branco e comentários
        i = 0
        
        #usa-se um while para percorrer a lista pois a quantidade de iterações pode variar pela quantidade de linahs em branco
        #remove todas as linhas em branco
        while(1):
            if i == len(list_lines_comp):
                break
            
            #excluir os comentários 
            for j in range(len(list_lines_comp[i])):
                #caso encontre um comentário excluo o resto da linha
                if list_lines_comp[i][j] == '#' :
                    list_lines_comp[i] = list_lines_comp[i][0:j]
                    break
            
            if len(list_lines_comp[i]) == 0 : #caso seja uma linha vazia eu elimino a mesma para facilitar
                del(list_lines_comp[i])
                i=i-1 #caso uma linha seja eliminada corrijo 
            
            i = i+1
        
        return list_lines_comp