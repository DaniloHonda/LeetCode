/*
3. (PERCURSO DO CAVALO) Dado um tabuleiro com n × n posições, o cavalo
movimenta-se segundo as regras do xadrez. A partir de uma posição inicial (x0, y0), o
problema consiste em fazer o cavalo “visitar” todas as casas do tabuleiro, sem
repetições.
Escreva um programa que selecione uma determinada posição do tabuleiro e verifique se é
possível realizar o percurso do cavalo no tabuleiro de xadrez.
*/

#include <stdio.h>

#define N 8  // Tamanho do tabuleiro N x N

// Movimentos possíveis do cavalo (x, y)
int movimentosX[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int movimentosY[8] = {1, 2, 2, 1, -1, -2, -2, -1};

// Função para verificar se a posição (x, y) é válida no tabuleiro
int ehPosicaoValida(int x, int y, int tabuleiro[N][N]) {
    return (x >= 0 && x < N && y >= 0 && y < N && tabuleiro[x][y] == -1);
}

// Função que imprime o tabuleiro
void imprimeTabuleiro(int tabuleiro[N][N]) {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            printf("%2d ", tabuleiro[x][y]);
        }
        printf("\n");
    }
}

// Função recursiva para resolver o passeio do cavalo usando backtracking
int resolvePasseio(int x, int y, int movimentoCount, int tabuleiro[N][N], int movX[8], int movY[8]) {
    int proximoX, proximoY;
    if (movimentoCount == N * N)
        return 1;

    // Tenta todos os movimentos possíveis do cavalo a partir da posição atual
    for (int i = 0; i < 8; i++) {
        proximoX = x + movX[i];
        proximoY = y + movY[i];
        if (ehPosicaoValida(proximoX, proximoY, tabuleiro)) {
            tabuleiro[proximoX][proximoY] = movimentoCount;
            if (resolvePasseio(proximoX, proximoY, movimentoCount + 1, tabuleiro, movX, movY))
                return 1;
            else
                tabuleiro[proximoX][proximoY] = -1;  // Backtracking
        }
    }

    return 0;
}

// Função para iniciar o processo de solução do passeio do cavalo
int iniciarPasseio(int xInicial, int yInicial) {
    int tabuleiro[N][N];

    // Inicializa o tabuleiro com -1 (indica casas não visitadas)
    for (int x = 0; x < N; x++)
        for (int y = 0; y < N; y++)
            tabuleiro[x][y] = -1;

    // Coloca o cavalo na posição inicial
    tabuleiro[xInicial][yInicial] = 0;

    // Tenta resolver o passeio
    if (!resolvePasseio(xInicial, yInicial, 1, tabuleiro, movimentosX, movimentosY)) {
        printf("Não há solução para o passeio do cavalo a partir da posição (%d, %d).\n", xInicial, yInicial);
        return 0;
    } else
        imprimeTabuleiro(tabuleiro);

    return 1;
}

int main() {
    int xInicial, yInicial;

    // Recebe a posição inicial do usuário
    printf("Insira a posição inicial do cavalo (x, y): ");
    scanf("%d %d", &xInicial, &yInicial);

    // Verifica se a posição inicial é válida e tenta resolver o passeio
    if (xInicial >= 0 && xInicial < N && yInicial >= 0 && yInicial < N) {
        iniciarPasseio(xInicial, yInicial);
    } else {
        printf("Posição inválida!\n");
    }

    return 0;
}
