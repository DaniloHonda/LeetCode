"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # parametros da funcao
        hashmap = {} # hashmap utiliza os valores do array como indices e retorna os indices (basicamente um vetor inverso)
        for i, num in enumerate(nums): # i = indices e num = numeros dentro da lista nums (funcao do enumerate)
            complement = target - num # calcula o complemento da soma necessaria para chegar no target
            if complement in hashmap: # se o complemento ja se encontra no hashmap ja temos a resposta
                return [hashmap[complement], i] # retorna o indice do complemento hashmap[complement] e o indice do outro numero
            hashmap[num] = i # adiciona o indice do vetor nums no hashmap
        return []  # retorna uma lista vazia caso nao encontre os complementos para a soma