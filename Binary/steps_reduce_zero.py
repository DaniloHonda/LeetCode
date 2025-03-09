class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        print(f"Inicio: num = {num}, steps = {steps}")
        
        while num > 0:
            print(f"\nAntes da operacao: num = {num}, steps = {steps}")
            if num & 1:  # Verifica se o numero é impar (bit menos significativo = 1)
                num -= 1
                print(f"impar: subtrai 1 -> num = {num}")
            else:
                num //= 2
                print(f"Par: divide por 2 -> num = {num}")
            steps += 1
            print(f"Apos operacao: steps = {steps}")
        
        print(f"\nResultado final: steps = {steps}")
        return steps

# Fucao principal para testar
def main():
    # Exemplo de entrada
    numero = 14  # Teste com 14
    print(f"Numero inicial: {numero}")
    
    # Cria instância da classe e executa
    solution = Solution()
    resultado = solution.numberOfSteps(numero)
    print(f"Verificao: Numero de passos = {resultado}")

# Executa o programa
if __name__ == "__main__":
    main()