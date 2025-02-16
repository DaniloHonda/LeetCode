
lista = [1,2,3,4,5,6,7,8,9,10]

def binarysearch(l, num):
  inicio, fim = 0, len(l) - 1
  
  while inicio <= fim:
    meio = (inicio + fim) // 2
    
    if l[meio] == num:
      return meio
    elif l[meio] < num:
      inicio = meio+1
    else:
      fim = meio-1
  
  return -1

num = binarysearch(lista, 5)

print(num)
