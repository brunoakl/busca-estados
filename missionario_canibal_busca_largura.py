import time
import psutil
from busca_largura import BuscaEmLargura
from missionario_canibal_base import Estado, ProblemaMissionariosCanibais

class MissionarioCanibalBuscaLargura(BuscaEmLargura):
    def aplicar_acao(self, estado: Estado, acao):
        missionario, canibal = acao
        if estado.barco:
            novo_estado = Estado(estado.missionarios - missionario, estado.canibais - canibal, False)
        else:
            novo_estado = Estado(estado.missionarios + missionario, estado.canibais + canibal, True)
        return novo_estado

# Exemplo de uso:
estado_inicial = Estado(3, 3, True)
estado_final = Estado(0, 0, False)
problema = ProblemaMissionariosCanibais(estado_inicial, estado_final)
busca = MissionarioCanibalBuscaLargura(problema)
caminho = busca.buscar()

if caminho:
    print("Caminho para a solução:")
    for estado in caminho:
        print(f"Missionários: {estado.missionarios}, Canibais: {estado.canibais}, Barco no lado {'Esquerdo' if estado.barco else 'Direito'}")
else:
    print("Não foi encontrada uma solução.")
