import numpy
from random import random
from random import randint
populacao = []
cromossomo = []


##GERANDO CIDADE##
nCity = int(input('Informe quantas cidades: '))
nPopulacao = int(input('Informe o tamanho da populacao: '))
x = numpy.zeros([nCity, nCity]) #Tamanho da matriz quadrada de distância
distancias = []
#A baixo está adicionando as distâncias aleatórias para depois alocar na matriz de simetrica
for i in range(len(x[numpy.triu_indices(nCity, 1)])):
   distancias.append(round(random() * 100)+1) #Aqui é alocado na lista as distancias aleatoria de uma cidade para outra.
x[numpy.triu_indices(nCity, 1)]  = distancias
x += x.T



##GERANDO CROMOSSOMO E POPULACAO##
for i in range(nPopulacao):
    #fazendo com que seja criado o cromossomo do tamanho do numero de cidades
    while len(cromossomo) < nCity:
        cidade = randint(0, (nCity-1))
        if cidade not in cromossomo: 
            cromossomo.append(cidade)
    populacao.append(cromossomo)
    cromossomo = []
    
   
    
##LER O CROMOSSOMO E FAZER O CALCULO DAS DISTÂNCIAS, ATRIBUINDO O CUSTO DE CADA CROMOSSOMO (AVALIACAO DO FITNESS)##
fitness = ()
aux2 = []
for l1 in populacao:
    custo = 0
    indice2 = 0
    #for para calcular a distância de uma cidade para outra. 
    #Para isso é consultado a matriz simétrica, da qual a representação distância[2][3] retorna a distância entre a cidade 2 para 3.
    for indice in range(len(l1)-1): #-1 porque se percorrer o tamanho total, estoura o indice da matriz.
        indice2 = indice2+1      
        custo += x[l1[indice]][l1[indice2]]  #Calcula a distância de uma cidade à outra, controlando sempre o indice anterior com o próximo.
        indice = indice+1
    fitness += (custo,l1)    
    aux2.append(fitness)
    fitness = ()



## ORDENAR A POPULACAO ##
ordena = []
ordena = sorted(aux2, key = lambda aux2: aux2[0], reverse = False)
print(ordena)

##SELECIONA OS PAIS ATRAVÉS DE ROLETA##
aux = 0
soma_total = 0
for i in aux2:#FOR responsável por fazer a soma de todos os individuos.
    soma_total = soma_total + int(aux2[aux][0]) #Verifica o individuo na posicao do indice e soma na variavel
    aux += 1

sorteio = round(random() * soma_total)#Realiza o sorteio de onde vai parar a roleta.
#---------------------------------------
print('Soma total: ' + str(soma_total))
print('Sorteio: ' + str(sorteio))
#---------------------------------------
posicaoEscolhida = -1
while (posicaoEscolhida < len(populacao)) and (sorteio > 0):#Responsavel para o funcionamento da roleta, diminui o valor do sorteio até chegar a 0, verificando a posicao   
    posicaoEscolhida += 1 
    sorteio -= ordena[posicaoEscolhida][0]

##REALIZA RECOMBINAÇÃO(UNIFORME)##
#Dois pais gera dois filhos.
pai1 = [1,2,5,4,3]
pai2 = [2,1,4,3,5]
filho1 = []
filho2 = []
bitsfilho = []
#print(nCity)

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

print(filho1)
print(bitsfilho)

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
    
    

##MUTAÇÃO

##REPRODUZIR ATÉ O TAMANHO DA POPULAÇÃO, E PASSAR PARA OUTRA GERAÇÃO.