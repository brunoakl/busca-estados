from eight_puzzle.busca_largura_eight_puzzle import BuscaLarguraEightPuzzle
from eight_puzzle.busca_estrela_eight_puzzle import BuscaAEstrelaEightPuzzle
from canibais_missionarios.busca_estrela_canibal_missionario import BuscaEstrelaCanibalMissionario
from canibais_missionarios.busca_largura_canibal_missionario import BuscaLarguraCanibalMissionario
from busca_minmax.busca_minmax_damas import jogo_damas
import sys, os, platform

class Menu:
    """
    Classe de menu com metódos estáticos
    """
    def limpar_terminal():
        sistema = platform.system()
    # Limpa o terminal com base no sistema operacional
        if sistema == 'Windows':
            os.system('cls')  # Para Windows
        else:
            os.system('clear')  # Para Unix/Linux/MacOS
    
    
    @classmethod
    def menu(self) -> None:
        """
        Menu inicial que irá começar
        """
        try:
            while True:
                opcao = int(input("Escolha um problema\n" +
                        "1 - Missionários e Canibais\n" +
                        "2 - 8 Puzzle\n" +
                        "3 - Damas\n" +
                        "9 - Sair\n"))
                match opcao:
                    case 1: Menu.limpar_terminal(); Menu.menu_canibal_missionario()
                    case 2: Menu.limpar_terminal(); Menu.menu_eight_puzzle()
                    case 3: Menu.limpar_terminal(); Menu.menu_damas()
                    case 9: sys.exit()
        except ValueError:
            print("\nInválido. Tente novamente\n")
            Menu.menu()
            

    @classmethod
    def menu_canibal_missionario(self) -> None:
        """
        Menu para solucionar busca para solucionar problema do canibal e missionário
        """
        try:
            while True:
                opcao = int(input("Escolha uma técnica de busca \n" +
                        "1 - Busca por Largura\n" +
                        "2 - A-Star(A*)\n" +
                        "8 - Voltar\n"+ 
                        "9 - Sair\n"))
                match opcao:
                    case 1: BuscaLarguraCanibalMissionario.new().iniciar()
                    case 2: BuscaEstrelaCanibalMissionario.new().iniciar()
                    case 8: Menu.limpar_terminal(); break
                    case 9: sys.exit()
        except ValueError:
            print("\nInválido. Tente novamente\n")
            Menu.menu_canibal_missionario()
                  

    @classmethod
    def menu_eight_puzzle(self) -> None:
        """
        Menu para solucionar busca para solucionar problema de 8 puzzle
        """
        try:
            while True:
                opcao = int(input("\nEscolha a técnica de busca que deseja usar \n" +
                        "1 - Busca por Largura\n" +
                        "2 - A-Star(A*)\n" +
                        "8 - Voltar\n" +
                        "9 - Sair\n"))
                
                match opcao:
                    case 1 | 2:
                        lista_str = input("Informe como deseja que se inicie o 8 puzzle \n" +
                                "exemplo:7,2,4,5,0,6,8,3,1\n").split(',')
                        lista = tuple(int(num) for num in lista_str)

                        if opcao == 1:
                            BuscaLarguraEightPuzzle.new(lista).iniciar()
                        elif opcao == 2:
                            BuscaAEstrelaEightPuzzle.new(lista).iniciar()
                    case 8: Menu.limpar_terminal(); break
                        
                    case 9: sys.exit()
        except ValueError:
            print("\nInválido. Tente novamente\n")
            Menu.limpar_terminal()
            Menu.menu_eight_puzzle()
                    
    @classmethod
    def menu_damas(self) -> None:
        """
        Menu para chamar o xadrez
        """
        try:
            while True:
                opcao = int(input("Escolha uma técnica de busca \n" +
                        "1 - Iniciar uma partida\n"+
                        "8 - Voltar\n"+
                        "9 - Sair\n"))
                match opcao:
                    case 1: jogo_damas()
                    case 8: Menu.limpar_terminal(); break
                    case 9: sys.exit()
        except ValueError:
            print("\nInválido. Tente novamente\n")
            Menu.limpar_terminal()
            Menu.menu_damas()
                    

Menu.menu()