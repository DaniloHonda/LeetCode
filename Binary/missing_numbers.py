from typing import List  # Importa List do módulo typing

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Inicializa x como 0
        x = 0
        print(f"Início: x = 0")
        
        # Primeiro loop: XOR com os números do array
        print("\nPrimeira etapa - XOR com números do array:")
        for num in nums:
            antes = x
            x ^= num
            print(f"x = {antes} ^ {num} = {x}")
        
        # Segundo loop: XOR com a sequência completa
        print("\nSegunda etapa - XOR com sequência de 0 a n:")
        for i in range(len(nums) + 1):
            antes = x
            x ^= i
            print(f"x = {antes} ^ {i} = {x}")
            
        print(f"\nResultado final: Número faltante = {x}")
        return x

# Função principal para testar o código
def main():
    # Exemplo de entrada
    nums = [3, 0, 1]  # Falta o 2 na sequência [0, 1, 2, 3]
    print(f"Array de entrada: {nums}")
    
    # Cria instância da classe e executa
    solution = Solution()
    resultado = solution.missingNumber(nums)
    print(f"Verificação: O número retornado é {resultado}")

# Executa o programa
if __name__ == "__main__":
    main()