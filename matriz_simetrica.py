##GERANDO CIDADE E DISTÂNCIAS##
nCity = int(input('Informe quantas cidades: '))
nPopulacao = int(input('Informe o tamanho da populacao: '))
x = numpy.zeros([nCity, nCity]) # 4x4 array of zeros
distancias = []
#A baixo está adicionando as distâncias aleatórias para depos alocar na matriz de simetrica
for i in range(len(x[numpy.triu_indices(nCity, 1)])):
   distancias.append(round(random() * 100)+1)
x[numpy.triu_indices(nCity, 1)]  = distancias
x += x.T

