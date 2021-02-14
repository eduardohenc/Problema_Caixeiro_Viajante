# Matriz quadrada com 11 cidades e as distâncias entre elas
distancias = [
  [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18],
  [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12],
  [20, 15, 0, 15, 14, 25, 81, 9, 23, 27, 13],
  [21, 29, 15, 0, 4, 12, 92, 12, 25, 13, 25],
  [16, 28, 14, 4, 0, 16, 94, 9, 20, 16, 22],
  [31, 40, 25, 12, 16, 0, 95, 24, 36, 3, 37],
  [100, 72, 81, 92, 94, 95, 0, 90, 101, 99, 84],
  [12, 21, 9, 12, 9, 24, 90, 0, 15, 25, 13],
  [4, 29, 23, 25, 20, 36, 101, 15, 0, 35, 18],
  [31, 41, 27, 13, 16, 3, 99, 25, 35, 0, 38],
  [18, 12, 13, 25, 22, 37, 84, 13, 18, 38, 0]
]


##### Inserção do vizinho mais distante #####
def vizinho_mais_distante(distancias, inicial = 0):
  
    # Inicializa a rota com a cidade inicial e a distancia total com zero
    atual = inicial
    rota = [atual]
    distancia_total = 0

    # Repita para o número de cidades - 1
    # A primeira cidade já foi adicionada na rota
    for _ in range(len(distancias)-1):

        # Pega a linha da matriz que representa os vizinhos da cidade atual (current)
        vizinhos = distancias[atual]

        # Inicializa a maior distância com zero
        melhor_vizinho = 0
        melhor_distancia = 0

        # Para cada cidade vizinha da cidade corrente
        for vizinho in range(len(vizinhos)):

            # Pega a distância da cidade atual para a cidade vizinha
            distancia = vizinhos[vizinho]

            #  Se a cidade ainda não foi visitada e
            #  sua distância for maior que zero e
            #  sua distância for maior que a maior distância até o momento
            #  então atualiza a cidade mais distante da atual
            if vizinho not in rota and distancia > 0 and distancia > melhor_distancia:
                melhor_vizinho = vizinho
                melhor_distancia = distancia
            
        # Atualiza a cidade atual para o vizinho mais distante
        # Adiciona o vizinho na rota e incrementa a distância total
        atual = melhor_vizinho
        rota.append(atual)
        distancia_total += melhor_distancia
    
    # Ao final, foi conectado a última cidade na primeira cidade
    rota.append(inicial)
    distancia_total += distancias[atual][inicial]

    return (distancia_total, rota)


print(vizinho_mais_distante(distancias))
   
  
  

##### Inserção do vizinho com distância média #####
def vizinho_distancia_media(distancias, inicial = 0):
    
    # Inicializa a rota com a cidade inicial e a distancia total com zero
    atual = inicial
    rota = [atual]
    distancia_total = 0

    # Repita para o número de cidades - 1
    # A primeira cidade já foi adicionada na rota
    for _ in range(len(distancias)-1):

        # Pega a linha da matriz que representa os vizinhos da cidade atual (current)
        vizinhos = distancias[atual]

        # Inicializa a maior distância com zero
        melhor_vizinho = 0
        melhor_distancia = 0

        # Para cada cidade vizinha da cidade corrente
        for vizinho in range(len(vizinhos)):

            # Pega a distância da cidade atual para a cidade vizinha
            distancia = vizinhos[vizinho]

            #  Se a cidade ainda não foi visitada e
            #  sua distância for maior que zero e
            #  sua distância for maior que a maior distância até o momento
            #  então atualiza a cidade mais distante da atual

            # sum() e len()

            if vizinho not in rota and distancia > 0 and distancia > melhor_distancia:
                melhor_vizinho = vizinho
                melhor_distancia = distancia
            
        # Atualiza a cidade atual para o vizinho mais distante
        # Adiciona o vizinho na rota e incrementa a distância total
        atual = melhor_vizinho
        rota.append(atual)
        distancia_total += melhor_distancia
    
    # Ao final, foi conectado a última cidade na primeira cidade
    rota.append(inicial)
    distancia_total += distancias[atual][inicial]

    return (distancia_total, rota)


print(vizinho_distancia_media(distancias)) 
