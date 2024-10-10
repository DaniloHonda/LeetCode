'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''
from typing import List

class Solution:
    # Vetor já ordenado, solução ideal usando a abordagem de dois ponteiros
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1  # Atribui para 'left' o valor 0, e para 'right' o valor de len(numbers) - 1
        
        # Enquanto o ponteiro da esquerda não ultrapassar o da direita
        while left < right:
            sum = numbers[left] + numbers[right]  # Soma os valores dos dois ponteiros
            if sum == target:  # Se a soma for igual ao target, encontramos os dois números
                return [left + 1, right + 1]  # Retorna os índices ajustados (1-indexed)
            elif sum > target:  # Se a soma for maior que o target, movemos o ponteiro da direita para diminuir a soma
                right -= 1
            else:  # Se a soma for menor que o target, movemos o ponteiro da esquerda para aumentar a soma
                left += 1
        
        return []  # Caso não haja solução (o que não acontece, pois há uma solução garantida pelo enunciado)

# Função principal para testar o código
def main():
    # Exemplo de teste
    solution = Solution()  # Cria uma instância da classe Solution
    numbers = [2, 7, 11, 15]  # Lista de números já ordenada
    target = 9  # Valor alvo para a soma
    result = solution.twoSum(numbers, target)  # Chama a função twoSum com os parâmetros
    print(f"Indices: {result}")  # Exibe o resultado esperado: [1, 2]

# Verifica se este script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função main para rodar o teste
