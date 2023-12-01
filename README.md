# Busca em Espaço de Estados
- Projeto desenvolvido para aplicar técnicas de busca em espaço de estados em diferentes problemas, como o jogo de damas, o problema dos missionários e canibais, e o quebra-cabeça de oito peças.
- (Insira aqui o link do vídeo com o funcionamento)

## Autores e Distribuição de Tarefas
- Bruno Machado Ferreira `Troubleshooting e Documentação do Projeto`

 
- Ernani Mendes da Fonseca Neto `Implementação da lógica do problema de Damas`


- Fábio Gomes de Souza `Pesquisa e implementação do algoritmo A-Star(A*)`


- Ryan Henrique Nantes `Pesquisa e implementação do algoritmo de Busca por Largura`

## Introdução 
O software que desenvolvemos é composto por bases separadas para cada um dos problemas, `busca minmax`, `canibais_missionarios`, `eight_puzzles`.


## Requisitos e bibliotecas
- Ubuntu 22.04 ou Windows 10
- Conda
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [memory_profiler 0.61.0](https://pypi.org/project/memory-profiler/0.61.0/)
- [numpy 1.26.2](https://pypi.org/project/numpy/1.26.2/)

## Preparando o ambiente
Abra um terminal na pasta do projeto e crie o ambiente, executanto o comando `conda create -n busca python==3.11 -y.` Ative-o com `conda activate busca`
Depois, instale o `memory_profiler`e o `numpy` com o comando `pip install memory_profiler==0.61.0 numpy==1.26.2`. Com isso, o ambiente está pronto.

## Uso
Rode o programa com `python main.py` para abrir o menu principal do programa. Você pode navegar por ele usando os números correspondentes as opções disponíveis.


## Missionários e canibais.
No menu dos Missionários e Canibais, o usuário pode escolher entre os métodos "Busca por Largura" e "A Estrela(A*)" para solucionar o problema.
Usar um dos métodos retornará os prompts da solução do problema dos Missionários e canibais, o uso de memória e o tempo de execução.
A navegação com valores inválidos como letras retornará o usuário ao menu. 

## 8 Puzzle
No menu do 8 Puzzle, o usuário pode escolher entre os métodos "Busca por Largura" e "A Estrela(A*)" para solucionar o problema.
Escolher uma das opções requisitará que o usuário preencha uma tupla que DEVERÁ conter ao menos 9 valores numéricos. Inserir menos valores que o necessário causará um erro que retornará o usuário ao menu de escolha de método.

### Explicação sobre os métodos
A busca por largura comça no estado inicial e explora todos os vizinhos do nível atual antes de passar para o próximo nível de nós. Devido a tendência de alto uso de memória, pode ser inadequada em grandes espaços de busca. Este método sempre encontrará a solução mais curta, se disponível.
Seu uso retornará os prompts da solução do problemas dos Missionários e canibais, o uso de memória e o tempo de execução.

O método A-Star faz uso de heurísticas - dada pela fórmula *f(n) = g(n) + h(n)* - para se locomover pelo espaço de busca, onde *g(n)* é o custo do caminho entre o estado inicial e *n*, e *h(n)* é uma estimativa heurística do menor caminho entre *n* até o objetivo final. Também faz uso intenso de recursos, mas costuma ser mais eficiente que a busca por largura pois não precisa explorar todos os caminhos. Sua performance é limitada pela heurísitca usada, podendo reduzir muito o número de nós e sendo muito mais rápida.
Seu uso retornará os prompts da solução do problemas dos Missionários e canibais, o uso de memória e o tempo de execução.

## Damas
No menu de Damas, o usuário pode executar a solução do problema de damas, iniciando uma partida de damas. O usuário é o primeiro a jogar, controlando as peças azuis com número 1.
Para mover uma peça, o usuário deve fornecer 2 pares de coordenada: a primeira sendo a de origem da peça e a segunda sendo o destino da peça.
As coordenadas devem ser inseridas na ordem Linha X Coluna. Logo após a jogada do usuário, o computador fará uma jogada.
Movimentos ilegais serão notificados no terminal. O jogo se encerra quando não houverem mais movimentos possíveis
Atenção! Os únicos jeitos de sair da partida de damas é encerrando o terminal ou terminando a partida.