def two_sum(nums, target):
    d = {}  # Dicionário para armazenar {valor: índice}

    for i, num in enumerate(nums):  # Percorre a lista com índice e valor
        complement = target - num  # Calcula o número necessário para atingir o target
        if complement in d:  # Se esse número já foi visto antes
            return [d[complement], i]  # Retorna os índices dos dois números encontrados
        d[num] = i  # Armazena o índice do número atual no dicionário

    return []  # Nunca chegará aqui, pois a entrada sempre tem uma solução garantida
