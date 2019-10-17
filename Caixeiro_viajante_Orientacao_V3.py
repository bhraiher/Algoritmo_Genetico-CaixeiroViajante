''' 
TRABALHO DESENVOLVIDO PELOS ALUNOS
    Bruno Henrique Raiher - RA: 1619044
    Nereu Neto - RA: 176499

'''
import numpy
from random import random
from random import randint
import matplotlib.pyplot as plt


class geraCidades():
    def __init__(self, nCity, nPopulacao):
        self.nCity = nCity
        self.nPopulacao = nPopulacao
        
    def geraDistancia(self):
        x = numpy.zeros([self.nCity, self.nCity]) #Tamanho da matriz quadrada de distância
        distancias = []
        #A baixo está adicionando as distâncias aleatórias para depois alocar na matriz de simetrica
        for i in range(len(x[numpy.triu_indices(self.nCity, 1)])):
           distancias.append(round(random() * 100)+1) #Aqui é alocado na lista as distancias aleatoria de uma cidade para outra.
        x[numpy.triu_indices(self.nCity, 1)]  = distancias
        x += x.T
        
        return x
 
class Individuo():
    def __init__(self, nCity, nPopulacao, populacao, matriz):
        self.nCity = nCity
        self.nPopulacao = nPopulacao
        self.populacao = populacao
        self.matriz = matriz
        
        
    #avaliação    
    def avaliacao(self):
        fitness = ()
        aux2 = []
        
        for l1 in self.populacao:
            custo = 0
            indice2 = 0
            #for para calcular a distância de uma cidade para outra. 
            #Para isso é consultado a matriz simétrica, da qual a representação distância[2][3] retorna a distância entre a cidade 2 para 3.
            for indice in range(len(l1)-1): #-1 porque se percorrer o tamanho total, estoura o indice da matriz.
                indice2 = indice2+1      
                custo += self.matriz[l1[indice]][l1[indice2]]  #Calcula a distância de uma cidade à outra, controlando sempre o indice anterior com o próximo.
                indice = indice+1
            fitness += (custo,l1)    
            aux2.append(fitness)
            fitness = ()

##REALIZA RECOMBINAÇÃO(UNIFORME)##   
        return aux2
    
    
    def reproducao(self, paiEscolhido):       
        #Dois pais gera dois filhos.
        paiEscolhido1 = paiEscolhido[0]
        paiEscolhido2 = paiEscolhido[1]
        pai1 = self.populacao[paiEscolhido2]
        pai2 = self.populacao[paiEscolhido1]


        filho1 = []
        filho2 = []
        bitsfilho = []
        filhos = []
        
        for i in range(nCity): 
            if random() < 0.5: #random responsável por criar os bits do individuo para fazer recombinação.
              bitsfilho.append('0')
            else:
              bitsfilho.append('1')
        
        #Primeiro filho 
        for i in range(nCity):#Substitui a cidade na posição do '1'
           if bitsfilho[i] == '1':
             filho1.append(pai1[i])
           else:
             filho1.append('0')
        
        for i in range(nCity):
            
            posic_pai2 = 0
            if filho1[i] == '0': 
                while (posic_pai2 != nCity):
                    if pai2[posic_pai2] not in filho1: 
                        filho1[i] = pai2[posic_pai2]
                        posic_pai2 = nCity
                        #print(posic_pai2)
                    else:
                        posic_pai2 += 1
  
        
        #Segundo filho
        for i in range(nCity):#Substitui a cidade na posição do '1'
           if bitsfilho[i] == '1':
             filho2.append(pai2[i])
           else:
             filho2.append('0')
        
        for i in range(nCity):
            posic_pai1 = 0
            if filho2[i] == '0': 
                while (posic_pai1 != nCity):
                    if pai1[posic_pai1] not in filho2: 
                        filho2[i] = pai1[posic_pai1]
                        posic_pai1 = nCity
                    else:
                        posic_pai1 += 1
        #print(filho2)
        filhos.append(filho1)
        filhos.append(filho2)
        return filhos
        

    

class algoritmoGenetico():
    def __init__(self, nCity, nPopulacao, nGeracao):
        self.nCity = nCity
        self.nPopulacao = nPopulacao
        self.nGeracao = nGeracao
        self.populacao = []
#[] - Definir uma lista com os melhores por cada geração.
        
        
        
    def inicializa_populacao(self):
        cromossomo = []
        for i in range(self.nPopulacao):
            #fazendo com que seja criado o cromossomo do tamanho do numero de cidades
            while len(cromossomo) < self.nCity:
                cidade = randint(0, (self.nCity-1))
                if cidade not in cromossomo: 
                    cromossomo.append(cidade)
            self.populacao.append(cromossomo)
            cromossomo = []
            
        return self.populacao  
    
    
    def ordena_populacao(self, nota_cromossomo): 
        self.nota_cromossomo = nota_cromossomo
        
        
        aux2 = nota_cromossomo
        ## ORDENAR A POPULACAO ##
        ordena = []
        ordena = sorted(aux2, key = lambda aux2: aux2[0], reverse = False)
    
        return ordena
    
    def soma_avaliacoes(self, nota_cromossomo):
        aux = 0
        soma_total = 0
        for i in nota_cromossomo:#FOR responsável por fazer a soma de todos os individuos.
            soma_total = soma_total + int(nota_cromossomo[aux][0]) #Verifica o individuo na posicao do indice e soma na variavel
            aux += 1  
        
        return soma_total

    def seleciona_pai(self, nota_cromossomo):
        
        pais = []
        for i in range(2):
            sorteio = round(random() * self.soma_avaliacoes(nota_cromossomo))#Realiza o sorteio de onde vai parar a roleta.
            posicaoEscolhida = -1
            while (posicaoEscolhida < len(self.populacao)) and (sorteio > 0):#Responsavel para o funcionamento da roleta, diminui o valor do sorteio até chegar a 0, verificando a posicao   
                posicaoEscolhida += 1 
                sorteio -= self.ordena_populacao(nota_cromossomo)[posicaoEscolhida][0]
            i +=1
            
            pais.append(posicaoEscolhida)  
        
        return pais
        
            

    
    
    
    
    def resolver(self):    
        ##GERANDO CIDADE##
        matriz = geraCidades(self.nCity, self.nPopulacao).geraDistancia()
        
        ##GERANDO CROMOSSOMO E POPULACAO INICIAL##
        self.populacao = self.inicializa_populacao()
        nova_populacao = []
        melhores = []
##FOR DAQUI PRA BAIXO
        for i in range(nGeracao):

            new_populacao = nPopulacao/2   
            ##LER O CROMOSSOMO E FAZER O CALCULO DAS DISTÂNCIAS, ATRIBUINDO O CUSTO DE CADA CROMOSSOMO (AVALIACAO DO FITNESS)##        
            avaliar_individuo = Individuo(self.nCity,self.nPopulacao,  self.populacao ,matriz).avaliacao()
            #print(avaliar_individuo)
            ## ORDENAR A POPULACAO ##
            ordenar = self.ordena_populacao(avaliar_individuo)
            melhores.append(ordenar[0][0])

           
            ##SELECIONA OS PAIS ATRAVÉS DE ROLETA##
            soma_total = self.soma_avaliacoes(avaliar_individuo)
            
            for i2 in range(int(new_populacao)):# tem que popular a nova populacao               
                pai_selecionado = self.seleciona_pai(avaliar_individuo)                
                
                ##FAZ A REPRODUCAO##
                reproducao = Individuo(self.nCity, self.nPopulacao,  self.populacao , matriz ).reproducao(pai_selecionado)                

                nova_populacao.append(reproducao[0])
                nova_populacao.append(reproducao[1])

                i2+=1

            self.populacao = []
            self.populacao = nova_populacao
            nova_populacao = []
            
        print('Melhor individuo da ultima geracao: ', self.populacao[0])
        print('Nota do melhor: ',ordenar[0][0])
        return melhores
    
    
        
        
    
    
if __name__ == '__main__':
     ##GERANDO CIDADE##
    nCity = int(input('Informe quantas cidades: '))
    nPopulacao = int(input('Informe o tamanho da populacao: '))
    nGeracao = int(input('Informe quantas gerações deve ter: '))
    chama = algoritmoGenetico(nCity, nPopulacao, nGeracao).resolver()
    

    plt.plot(chama)
    plt.title("Acompanhamento dos valores")
    plt.show() 
