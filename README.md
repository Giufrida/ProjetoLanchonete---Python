# ProjetoLanchonete-Python

• Sistema de Gestão de Restaurante

Sistema de gerenciamento para o restaurante Great Fillet, projetado para automatizar o controle do cardápio, a fila de atendimento e preparo na cozinha, além de permitir o rastreamento e reversão de ações por meio de histórico e auditoria.

O projeto demonstra a aplicação prática de estruturas de dados fundamentais em Python (Lista nativa, Fila e Pilha), oferecendo modos de operação via Linha de Comando (CLI) e Interface Gráfica (GUI com Tkinter).

• Sumário

Estruturas de Dados Utilizadas
Funcionalidades e Módulos
Interfaces Disponíveis
Estrutura do Projeto
Pré-requisitos e Como Executar
Regras de Negócio e Validações

• Estruturas de Dados Utilizadas

A solução combina três estruturas essenciais para manter a integridade dos dados e o fluxo de operações do restaurante:

Cardápio (list nativa do Python):
Armazena os itens/pratos disponíveis (ID, Nome e Preço).
Utiliza a estrutura dinâmica de lista nativa para busca, inclusão e remoção.

Fila da Cozinha (Classe Fila - FIFO):
Gerencia a ordem dos pedidos que aguardam preparo.
Segue o princípio First In, First Out (FIFO): o primeiro pedido registrado é o primeiro a ser atendido pela cozinha.

Histórico de Operações (Classe Pilha - LIFO):
Registra as ações de lançamento e atendimento de pedidos para auditoria.
Segue o princípio Last In, First Out (LIFO), viabilizando o mecanismo de Desfazer (Undo) para reverter a última operação realizada.

• Funcionalidades e Módulos

1. Gestão do Cardápio (list)
RF-01 - Cadastrar Item: Adiciona um novo item ao cardápio com ID único, Nome e Preço.
RF-02 - Remover Item: Remove um item do cardápio através do seu ID.
RF-03 - Exibir Cardápio: Lista todos os pratos atualmente cadastrados no sistema.

2. Atendimento e Cozinha (Fila)
3. 
RF-04 - Lançar Pedido (Enfileirar): Registra um pedido associando o Nome do Cliente e os IDs dos itens do cardápio validados. O pedido vai para o final da fila da cozinha.
RF-05 - Atender Pedido (Desenfileirar): Processa e remove o próximo pedido da fila, exibindo as informações do pedido concluído.
RF-06 - Visualizar Fila: Exibe a lista ordenada de pedidos aguardando preparo na cozinha.

3. Histórico e Auditoria (Pilha)

RF-07 - Registrar Histórico: Empilha automaticamente um registro contendo a ação executada ("Lançar Pedido" ou "Atender Pedido") e seus dados.
RF-08 - Desfazer Última Ação (Desempilhar/Undo): Reverte a ação no topo da pilha:

Se a última ação foi Lançar Pedido: o pedido é cancelado/removido da fila.
Se a última ação foi Atender Pedido: o pedido retorna ao início da fila da cozinha.

🖥 Interfaces Disponíveis

Interface Gráfica (Tkinter GUI)
   
Uma interface visual moderna e intuitiva construída com a biblioteca padrão tkinter, permitindo operar o cardápio, a fila da cozinha e o histórico através de telas interativas, botões e tabelas informativas.



• Estrutura do Projeto

restaurante-great-fillet/
│
├── pilha.py          # Classe Pilha (fornecida)
├── fila.py           # Classe Fila (fornecida)
├── cardapio.py       # Lógica e manipulação do Cardápio (list)
├── main_gui.py       # Execução da interface gráfica (Tkinter)
└── README.md         # Documentação do projeto


• Pré-requisitos e Como Executar

Pré-requisitos

Python 3.8 ou superior instalado.
O módulo tkinter (incluído nativamente na instalação padrão do Python no Windows e macOS. No Linux/Ubuntu, pode ser necessário sudo apt-get install python3-tk).

Passos para Execução

Clonar ou baixar o repositório:
git clone https://github.com/seu-usuario/restaurante-great-fillet.git
cd restaurante-great-fillet

Executar a Interface Gráfica (Tkinter):
python main_gui.py


• Regras de Negócio e Validações

Validação de Cardápio: Não é possível lançar pedidos com IDs de itens inexistentes.
Tratamento de Filas Vazias: Exibição de mensagens amigáveis caso a cozinha não possua pedidos pendentes para atendimento ou visualização.
Tratamento de Pilhas Vazias: Impede a operação de "Desfazer" quando não há ações registradas no histórico.
Integridade da Reversão: Garantia de que a devolução de um pedido atendido retorne para a cabeça da fila sem perder os itens originais associados.
