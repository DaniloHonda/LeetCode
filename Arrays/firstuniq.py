# Finding the first unique char in a string

def firstuniq(s):
    d = {}  # Dicionário para armazenar {caractere: (índice, contagem)}

    for idx, ch in enumerate(s):
        if ch not in d:
            d[ch] = [idx, 1]  # Armazena o índice e a contagem do caractere
        else:
            d[ch][1] += 1  # Incrementa a contagem do caractere

    for ch, (idx, count) in d.items():  # Percorre os itens armazenados
        if count == 1:  # Se a contagem for 1, significa que é único
            return idx  # Retorna o índice do primeiro caractere único

    return -1  # Retorna -1 se não houver caracteres únicos