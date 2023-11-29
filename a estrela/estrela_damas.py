import numpy as np
import random

# Constantes para o jogo
VAZIO = 0
JOGADOR = 1
PC = 2
DAMA_JOGADOR = 3
DAMA_PC = 4

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

def capturas_possiveis(tabuleiro, i, j, jogador, oponente, e_dama, capturas_previas=[]):
    capturas = []
    direcoes = DIRECOES if e_dama else [(1, -1), (1, 1)] if jogador == JOGADOR else [(-1, -1), (-1, 1)]

    for dx, dy in direcoes:
        x, y = i + dx, j + dy
        x2, y2 = i + 2 * dx, j + 2 * dy

        if 0 <= x2 < TAMANHO_TABULEIRO and 0 <= y2 < TAMANHO_TABULEIRO and tabuleiro[x][y] == oponente and tabuleiro[x2][y2] == VAZIO:
            novo_tabuleiro = np.copy(tabuleiro)
            mover_peca(novo_tabuleiro, (i, j), (x2, y2))
            sequencias_adicionais = capturas_possiveis(novo_tabuleiro, x2, y2, jogador, oponente, e_dama, capturas_previas + [((i, j), (x2, y2))])

            if sequencias_adicionais:
                capturas.extend(sequencias_adicionais)
            else:
                capturas.append(((i, j), (x2, y2)))

    return capturas

def movimentos_validos(tabuleiro, jogador):
    movimentos = []
    oponente = JOGADOR if jogador == PC else PC
    pecas = [jogador, DAMA_JOGADOR if jogador == JOGADOR else DAMA_PC]

    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            if tabuleiro[i][j] in pecas:
                e_dama = tabuleiro[i][j] in [DAMA_JOGADOR, DAMA_PC]
                movimentos.extend(capturas_possiveis(tabuleiro, i, j, jogador, oponente, e_dama))

                if not movimentos:
                    movimentos.extend(movimentos_normais(tabuleiro, i, j, jogador, e_dama))

    return movimentos

def movimentos_normais(tabuleiro, i, j, jogador, e_dama):
    movimentos = []
    direcoes = DIRECOES if e_dama else [(1, -1), (1, 1)] if jogador == JOGADOR else [(-1, -1), (-1, 1)]

    for dx, dy in direcoes:
        x, y = i + dx, j + dy
        if 0 <= x < TAMANHO_TABULEIRO and 0 <= y < TAMANHO_TABULEIRO and tabuleiro[x][y] == VAZIO:
            movimentos.append(((i, j), (x, y)))

    return movimentos


def mover_peca(tabuleiro, inicio, fim):
    # Promove a peça a dama se atingir o lado oposto do tabuleiro
    if tabuleiro[inicio[0], inicio[1]] == JOGADOR and fim[0] == 0:
        tabuleiro[fim[0], fim[1]] = DAMA_JOGADOR
    elif tabuleiro[inicio[0], inicio[1]] == PC and fim[0] == TAMANHO_TABULEIRO - 1:
        tabuleiro[fim[0], fim[1]] = DAMA_PC
    else:
        tabuleiro[fim[0], fim[1]] = tabuleiro[inicio[0], inicio[1]]
    tabuleiro[inicio[0], inicio[1]] = VAZIO

    # Remover peça capturada
    if abs(fim[0] - inicio[0]) == 2:
        x_captura, y_captura = (inicio[0] + fim[0]) // 2, (inicio[1] + fim[1]) // 2
        tabuleiro[x_captura, y_captura] = VAZIO
    return tabuleiro

def ha_pecas(tabuleiro, jogador):
    return any(jogador in linha for linha in tabuleiro)

def avaliar_tabuleiro(tabuleiro):
    # Aqui, você pode definir como o tabuleiro será avaliado.
    # Por exemplo, contando o número de peças de cada jogador.
    jogador_peca = np.sum(tabuleiro == JOGADOR)
    pc_peca = np.sum(tabuleiro == PC)
    return pc_peca - jogador_peca  # Exemplo: mais peças do PC são melhores para o PC

def minimax(tabuleiro, profundidade, maximizandoJogador):
    if profundidade == 0 or not ha_pecas(tabuleiro, JOGADOR) or not ha_pecas(tabuleiro, PC):
        return avaliar_tabuleiro(tabuleiro)

    if maximizandoJogador:
        maxEval = float('-inf')
        for movimento in movimentos_validos(tabuleiro, PC):
            tabuleiro_copia = np.copy(tabuleiro)
            mover_peca(tabuleiro_copia, movimento[0], movimento[1])
            eval = minimax(tabuleiro_copia, profundidade - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for movimento in movimentos_validos(tabuleiro, JOGADOR):
            tabuleiro_copia = np.copy(tabuleiro)
            mover_peca(tabuleiro_copia, movimento[0], movimento[1])
            eval = minimax(tabuleiro_copia, profundidade - 1, True)
            minEval = min(minEval, eval)
        return minEval

def melhor_movimento_pc(tabuleiro, profundidade):
    melhor_movimento = None
    maxEval = float('-inf')
    for movimento in movimentos_validos(tabuleiro, PC):
        tabuleiro_copia = np.copy(tabuleiro)
        mover_peca(tabuleiro_copia, movimento[0], movimento[1])
        eval = minimax(tabuleiro_copia, profundidade - 1, False)
        if eval > maxEval:
            maxEval = eval
            melhor_movimento = movimento
    return melhor_movimento

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
            movimento_pc = melhor_movimento_pc(tabuleiro, 3)  # Defina a profundidade desejada
            if movimento_pc:
                print(f"PC move de {movimento_pc[0]} para {movimento_pc[1]}")
                tabuleiro = mover_peca(tabuleiro, movimento_pc[0], movimento_pc[1])
            else:
                print("PC sem movimentos válidos. Jogador venceu!")
                break

        turno_jogador = not turno_jogador

jogo_damas()
