'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Ordena o array para facilitar a busca de tripletos e a eliminação de duplicatas
        nums.sort()
        
        # Conjunto para armazenar tripletos únicos
        triplets = set()
        
        # Percorre cada número do array, tratando-o como o primeiro número do triplete
        for i in range(len(nums) - 2):
            # Se o número atual é igual ao número anterior, pula para evitar duplicação
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Define dois ponteiros: um após o número atual e outro no final do array
            left, right = i + 1, len(nums) - 1
            
            # Enquanto os ponteiros não se cruzam
            while left < right:
                # Calcula a soma dos três números
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Se a soma é zero, adiciona o triplete ao conjunto
                    triplets.add((nums[i], nums[left], nums[right]))
                    
                    # Move o ponteiro da esquerda para a direita, ignorando duplicatas
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Move o ponteiro da direita para a esquerda, ignorando duplicatas
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif current_sum < 0:
                    # Se a soma é menor que zero, move o ponteiro da esquerda para a direita
                    left += 1
                
                else:
                    # Se a soma é maior que zero, move o ponteiro da direita para a esquerda
                    right -= 1
        
        # Converte o conjunto de tripletos para uma lista e retorna
        return list(triplets)
        