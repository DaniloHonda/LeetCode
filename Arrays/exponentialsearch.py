def binary_search(lista, num, inicio, fim):
  inicio, fim =0, len(lista) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2

    if lista[meio] == num:
      return meio
    elif lista[meio] < num:
      inicio = meio + 1
    else:
      fim = meio - 1
  return -1

 # Exponencial search utiliza da binary search em seu algoritmo, mas precisa que ela possua right e left como parametros
 # O(log n) e precisa de array ordenado

def exponential_search(lista, num):
  if lista[0] == num:
    return 0
  len = len(lista)
  r = 1 # uma vez que o elemento 0 não é o número buscado, o r é duplicado

  while r <= len -1 and lista[r] <= num:
    if lista[r] == num:
      return r
    r = r * 2
  return binary_search(lista, num, r//2, min(r, len-1)) # min(r, len-1) para evitar o erro de overflow 
# r//2 vai ser como o ponteiro left e min(r, len-1) vai ser como o ponteiro right