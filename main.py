from eight_puzzle.busca_largura_eight_puzzle import BuscaLarguraEightPuzzle
from eight_puzzle.busca_estrela_eight_puzzle import BuscaAEstrelaEightPuzzle
from canibais_missionarios.busca_estrela_canibal_missionario import BuscaEstrelaCanibalMissionario
from canibais_missionarios.busca_largura_canibal_missionario import BuscaLarguraCanibalMissionario

class Menu:
    """
    Classe de menu com metódos estáticos
    """

    @classmethod
    def menu(self) -> None:
        """
        Menu inicial que irá começar
        """
        try:
            while True:
                opcao = int(input("Escolha por favor qual problema deseja ver \n" +
                        "1 - Missionários e Canibais\n" +
                        "2 - 8 Puzzle\n" +
                        "3 - Damas\n"))
                match opcao:
                    case 1:
                        Menu.menu_canibal_missionario()
                    case 2:
                        Menu.menu_eight_puzzle()
                    case 3:
                        break
                    case _:
                        print("Opção Inválida")
        except:
            print("Valor inserido não é válido!")
            Menu.menu()

    @classmethod
    def menu_canibal_missionario(self) -> None:
        """
        Menu para solucionar busca para solucionar problema do canibal e missionário
        """
        try:
            while True:
                opcao = int(input("Escolha a técnica de busca que deseja usar \n" +
                        "1 - Busca por Largura\n" +
                        "2 - A Estrela\n" +
                        "3 - Voltar\n"))
                match opcao:
                    case 1:
                        BuscaLarguraCanibalMissionario.new().iniciar()
                    case 2:
                        BuscaEstrelaCanibalMissionario.new().iniciar()
                    case 3:
                        break
                    case _:
                        print("Opção Inválida")
        except:
            print("Valor inserido não é válido!")
            Menu.menu_canibal_missionario()       

    @classmethod
    def menu_eight_puzzle(self) -> None:
        """
        Menu para solucionar busca para solucionar problema de 8 puzzle
        """
        try:
            while True:
                opcao = int(input("Escolha a técnica de busca que deseja usar \n" +
                        "1 - Busca por Largura\n" +
                        "2 - A Estrela\n" +
                        "3 - Voltar\n"))
                lista_str = input("Informe como deseja que se inicie o 8 puzzle \n" +
                              "exemplo: 3,4,1,2,5,6,9,0,7,8\n").split(',')
                lista = (int(lista_str[0]), int(lista_str[1]), int(lista_str[2]), 
                         int(lista_str[3]), int(lista_str[4]), int(lista_str[5]), 
                         int(lista_str[6]), int(lista_str[7]), int(lista_str[8]))
                match opcao:
                    case 1:
                        BuscaLarguraEightPuzzle.new(lista).iniciar()
                    case 2:
                        BuscaAEstrelaEightPuzzle.new(lista).iniciar()
                    case 3:
                        break
                    case _:
                        print("Opção Inválida")
        except:
            print("Valor inserido não é válido!")
            Menu.menu_eight_puzzle() 

Menu.menu()