from eight_puzzle.busca_largura_eight_puzzle import BuscaLarguraEightPuzzle
from eight_puzzle.busca_estrela_eight_puzzle import BuscaAEstrelaEightPuzzle
from canibais_missionarios.busca_estrela_canibal_missionario import BuscaEstrelaCanibalMissionario
from canibais_missionarios.busca_largura_canibal_missionario import BuscaLarguraCanibalMissionario
from busca_minmax.busca_minmax_damas import *
import sys

class Menu:
    """
    Classe de menu com metódos estáticos
    """

    @classmethod
    def menu(self) -> None:
        """
        Menu inicial que irá começar
        """
        while True:
            opcao = int(input("Escolha um problema\n" +
                    "1 - Missionários e Canibais\n" +
                    "2 - 8 Puzzle\n" +
                    "3 - Damas\n" +
                    "9 - Sair\n"))
            match opcao:
                case 1: Menu.menu_canibal_missionario()
                case 2: Menu.menu_eight_puzzle()
                case 3: Menu.menu_damas()
                case 9: sys.exit()
                case _:
                    print(str(opcao)+" é inválido. Tente novamente\n")
                    Menu.menu()


    @classmethod
    def menu_canibal_missionario(self) -> None:
        """
        Menu para solucionar busca para solucionar problema do canibal e missionário
        """
        while True:
            opcao = int(input("Escolha uma técnica de busca \n" +
                    "1 - Busca por Largura\n" +
                    "2 - A Estrela\n" +
                    "8 - Voltar\n"+ 
                    "9 - Sair\n"))
            match opcao:
                case 1: BuscaLarguraCanibalMissionario.new().iniciar()
                case 2: BuscaEstrelaCanibalMissionario.new().iniciar()
                case 8: break
                case 9: sys.exit()
                case _: print(str(opcao)+" é inválido. Tente novamente\n"); Menu.menu_canibal_missionario()

                  

    @classmethod
    def menu_eight_puzzle(self) -> None:
        """
        Menu para solucionar busca para solucionar problema de 8 puzzle
        """
        while True:
            opcao = int(input("Escolha a técnica de busca que deseja usar \n" +
                    "1 - Busca por Largura\n" +
                    "2 - A Estrela\n" +
                    "8 - Voltar\n" +
                    "9 - Sair\n"))
            
            match opcao:
                case 1 | 2:
                    while True:
                        lista_str = input("Informe como deseja que se inicie o 8 puzzle \n" +
                                "exemplo: 3,4,1,2,5,6,9,0,7,8\n").split(',')
                        lista = tuple(int(num) for num in lista_str)

                        if opcao == 1:
                            BuscaLarguraEightPuzzle.new(lista).iniciar()
                        elif opcao == 2:
                            BuscaAEstrelaEightPuzzle.new(lista).iniciar()
                case 8: break
                case 9: sys.exit()
                case _:
                    print(str(opcao) + " é inválido. Tente novamente\n")
                    Menu.menu()
                    
    @classmethod
    def menu_damas(self) -> None:
        """
        Menu para chamar o xadrez
        """
        while True:
            opcao = int(input("Escolha uma técnica de busca \n" +
                    "1 - Iniciar uma partida\n"+
                    "8 - Voltar\n"+
                    "9 - Sair\n"))
            match opcao:
                case 1: print("xadrez"); jogo_damas()
                case 8: break
                case 9: sys.exit()
                case _: print(str(opcao)+" é inválido. Tente novamente\n"); Menu.menu_damas

                    

Menu.menu()