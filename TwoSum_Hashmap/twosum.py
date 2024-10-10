"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # hashmap utiliza os valores do array como índices e retorna os índices (basicamente um vetor inverso)
        for i, num in enumerate(nums):  # i = índices e num = números dentro da lista nums (função do enumerate)
            complement = target - num  # calcula o complemento da soma necessária para chegar no target
            if complement in hashmap:  # se o complemento já se encontra no hashmap, já temos a resposta
                return [hashmap[complement], i]  # retorna o índice do complemento hashmap[complement] e o índice do outro número
            hashmap[num] = i  # adiciona o índice do vetor nums no hashmap
        return []  # retorna uma lista vazia caso não encontre os complementos para a soma

# Função principal para testar o código
def main():
    # Exemplo de teste
    solution = Solution()  # Cria uma instância da classe Solution
    nums = [2, 7, 11, 15]  # Lista de números
    target = 9  # Valor alvo para a soma
    result = solution.twoSum(nums, target)  # Chama a função twoSum com os parâmetros
    print(f"Indices: {result}")  # Exibe o resultado esperado: [0, 1]

# Verifica se este script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função main para rodar o teste

    def twoSum(self, nums: List[int], target: int) -> List[int]: # parametros da funcao
        hashmap = {} # hashmap utiliza os valores do array como indices e retorna os indices (basicamente um vetor inverso)
        for i, num in enumerate(nums): # i = indices e num = numeros dentro da lista nums (funcao do enumerate)
            complement = target - num # calcula o complemento da soma necessaria para chegar no target
            if complement in hashmap: # se o complemento ja se encontra no hashmap ja temos a resposta
                return [hashmap[complement], i] # retorna o indice do complemento hashmap[complement] e o indice do outro numero
            hashmap[num] = i # adiciona o indice do vetor nums no hashmap
        return []  # retorna uma lista vazia caso nao encontre os complementos para a soma