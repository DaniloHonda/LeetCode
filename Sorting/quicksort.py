def quick_sort(arr, inicio, fim):
    if inicio < fim:
        # Encontra a posição do pivô
        pivo = particionar(arr, inicio, fim)
        # Ordena a parte esquerda do pivô
        quick_sort(arr, inicio, pivo - 1)
        # Ordena a parte direita do pivô
        quick_sort(arr, pivo + 1, fim)

def particionar(arr, inicio, fim):
    pivo = arr[fim]  # Escolhe o último elemento como pivô
    i = inicio - 1   # Índice do menor elemento
    
    for j in range(inicio, fim):
        # Se o elemento atual for menor ou igual ao pivô
        if arr[j] <= pivo:
            i += 1  # Incrementa o índice do menor elemento
            arr[i], arr[j] = arr[j], arr[i]
    
    # Coloca o pivô na posição correta
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

# Exemplo de uso
if __name__ == "__main__":
    # Array de exemplo
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", arr)
    
    quick_sort(arr, 0, len(arr) - 1)
    print("Array ordenado:", arr)