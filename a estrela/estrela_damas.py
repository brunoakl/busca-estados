import numpy as np
import random

# Constantes para o jogo
VAZIO = 0
JOGADOR = 1
PC = 2
TAMANHO_TABULEIRO = 8

# Direções de movimento
DIRECOES = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def inicializar_tabuleiro():
    tabuleiro = np.zeros((TAMANHO_TABULEIRO, TAMANHO_TABULEIRO), dtype=int)
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            if (i + j) % 2 == 1:
                if i < 3:
                    tabuleiro[i][j] = JOGADOR
                elif i > 4:
                    tabuleiro[i][j] = PC
    return tabuleiro

def print_tabuleiro(tabuleiro):
    for row in tabuleiro:
        print(' '.join(str(cell) for cell in row))
    print()

def movimentos_validos(tabuleiro, jogador):
    movimentos = []
    oponente = JOGADOR if jogador == PC else PC
    direcao = 1 if jogador == JOGADOR else -1

    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            if tabuleiro[i][j] == jogador:
                for dx, dy in DIRECOES:
                    x, y = i + dx * direcao, j + dy
                    # Verificar movimentos normais
                    if 0 <= x < TAMANHO_TABULEIRO and 0 <= y < TAMANHO_TABULEIRO and tabuleiro[x][y] == VAZIO:
                        movimentos.append(((i, j), (x, y)))
                    # Verificar capturas
                    x2, y2 = i + 2 * dx * direcao, j + 2 * dy
                    if 0 <= x2 < TAMANHO_TABULEIRO and 0 <= y2 < TAMANHO_TABULEIRO and tabuleiro[x][y] == oponente and tabuleiro[x2][y2] == VAZIO:
                        movimentos.append(((i, j), (x2, y2)))

    return movimentos


def mover_peca(tabuleiro, inicio, fim):
    tabuleiro[fim[0], fim[1]] = tabuleiro[inicio[0], inicio[1]]
    tabuleiro[inicio[0], inicio[1]] = VAZIO
    # Remover peça capturada
    if abs(fim[0] - inicio[0]) == 2:
        x_captura, y_captura = (inicio[0] + fim[0]) // 2, (inicio[1] + fim[1]) // 2
        tabuleiro[x_captura, y_captura] = VAZIO
    return tabuleiro

def escolher_movimento_pc(tabuleiro):
    movimentos = movimentos_validos(tabuleiro, PC)
    movimentos_normais = [m for m in movimentos if abs(m[0][0] - m[1][0]) == 1]
    movimentos_captura = [m for m in movimentos if abs(m[0][0] - m[1][0]) == 2]

    if movimentos_captura:
        return random.choice(movimentos_captura)
    elif movimentos_normais:
        return random.choice(movimentos_normais)
    else:
        return None


def ha_pecas(tabuleiro, jogador):
    return any(jogador in linha for linha in tabuleiro)

def jogo_damas():
    tabuleiro = inicializar_tabuleiro()
    turno_jogador = True

    while True:
        print_tabuleiro(tabuleiro)

        if not ha_pecas(tabuleiro, PC):
            print("Jogador venceu!")
            break
        elif not ha_pecas(tabuleiro, JOGADOR):
            print("PC venceu!")
            break

        if turno_jogador:
            movimentos = movimentos_validos(tabuleiro, JOGADOR)
            if not movimentos:
                print("Sem movimentos válidos. PC venceu!")
                break
            inicio, fim = eval(input("Digite seu movimento (inicio, fim): "))
            tabuleiro = mover_peca(tabuleiro, inicio, fim)
        else:
            movimento_pc = escolher_movimento_pc(tabuleiro)
            if movimento_pc:
                print(f"PC move de {movimento_pc[0]} para {movimento_pc[1]}")
                tabuleiro = mover_peca(tabuleiro, movimento_pc[0], movimento_pc[1])
            else:
                print("PC sem movimentos válidos. Jogador venceu!")
                break

        turno_jogador = not turno_jogador

jogo_damas()
