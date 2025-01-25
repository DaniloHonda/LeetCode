'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321
'''

class Solution:
    def reverse(self, x: int) -> int:
        # Verifica se o número é negativo
        is_negative = x < 0
        # Converte para positivo se for negativo
        x = abs(x)
        # Inicializa o número invertido
        reverse_num = 0
        
        # Inverte o número usando operações matemáticas
        while x != 0:
            digit = x % 10  # Obtém o último dígito
            reverse_num = reverse_num * 10 + digit  # Constrói o número invertido
            x //= 10  # Remove o último dígito de x

        # Se o número invertido está fora dos limites de um inteiro de 32 bits, retorna 0
        if reverse_num < -2**31 or reverse_num > 2**31 - 1:
            return 0
        
        # Retorna o número invertido com o sinal original
        return -reverse_num if is_negative else reverse_num
