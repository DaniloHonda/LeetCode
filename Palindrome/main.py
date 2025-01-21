'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = list(str(x)) # transforma o numero em str e ja separa ele, 123 = '1', '2', '3'
        left, right = 0, len(x_str) - 1
        
        while left <= right:
            if x_str[left] == x_str[right]: # se inicio igual final aumenta esquerda e diminui direita ate o final da str
                left += 1
                right -= 1
            else:
                return False # nao e palindromo
            
        return True # se finalizou sem retornar False == True
        
        
class Solution: # solucao 2, "ideal"
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # nao existe palindromo negativo
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10 # pega resto da divisao, consequentemente um digito 
            reversed_num = reversed_num * 10 + digit # calculo para inverter
            temp //= 10 # divide por 10, porem sem sem virgula, 122//10 = 12, uma vez que temp = 0 fim do loop

        return reversed_num == x
        
    