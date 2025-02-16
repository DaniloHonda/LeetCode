def sliding(s, num):
  l, r = 0, 0  # Ponteiros da esquerda (l) e da direita (r) para a janela deslizante
  max_length = 1  # Variável para armazenar o tamanho máximo da substring válida
  counter = {}  # Dicionário que armazena as letras e a quantidade de vezes que aparecem

  counter[s[num]] = 1  # Inicializa a contagem da primeira letra na posição 'num'

  while r < len(s) - 1:  # Enquanto o ponteiro direito não atingir o fim da string
    r += 1  # Move o ponteiro direito para expandir a janela
    
    # ERRO: counter(s[r]) está errado, deve ser apenas counter
    if s[r] in counter:  # Verifica se a letra já apareceu na janela
      counter[s[r]] += 1  # Incrementa a contagem da letra
    else:
      counter[s[r]] = 1  # Se for a primeira aparição, inicializa com 1

    # Se a contagem da letra atual atingir 3, removemos caracteres da esquerda
    while counter[s[r]] == 3:
      counter[s[l]] -= 1  # Diminui a contagem da letra mais à esquerda
      l += 1  # Move o ponteiro esquerdo para a direita, reduzindo a janela
      
    # ERRO: max é o nome de uma função embutida do Python, deve ser renomeado (ex: max_length)
    max_length = max(max_length, r - l + 1)  # Atualiza o tamanho máximo da substring válida

  return max_length  # Retorna o tamanho máximo encontrado
