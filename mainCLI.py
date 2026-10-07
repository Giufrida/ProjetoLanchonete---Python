from pilha import Pilha
from fila import Fila

cardapio = list()
fila = Fila()
sistema = Pilha()

def menu():
    print('======================================================')
    print('             RESTAURANTE FASTBITE - CLI')
    print('======================================================')
    print('--- CARDÁPIO ---')
    print('1. Cadastrar Item no Cardápio')
    print('2. Remover Item do Cardápio')
    print('3. Listar Cardápio\n')
    print('--- COZINHA & PEDIDOS ---')
    print('4. Lançar Novo Pedido')
    print('5. Atender Próximo Pedido')
    print('6. Visualizar Fila da Cozinha\n')
    print('--- SISTEMA ---')
    print('7. Desfazer Última Ação')
    print('8. Visualizar Histórico de Ações')
    print('0. Sair')
    print('======================================================')

    opcao = int(input('Escolha uma opção: '))
    print()


    return opcao

while True:
    opcao = menu()

    match opcao:
        case 1:
            listaIDs = [] 
            while True:
                id = int(input('Digite o ID do item que deseja adicionar(sem repetir): '))
                if id not in listaIDs:
                    listaIDs.append(id)
                    break 
            
            
            nome = input('Digite o nome do item que deseja adicionar: ')
            preco = float(input('Digite o preço do item que deseja adicionar: '))

            item = {
                'id': id,
                'nome': nome,
                'preco': preco
            }

            cardapio.append(item)
            print('Item adicionado!')
        case 2:
            id = int(input('Digite o ID do item que deseja remover: '))
            for i in cardapio:
                if i['id'] == id:
                    cardapio.remove(i)
                    print(f'Produto {i['nome']} removido!')
                    break
        case 3:
            print('Nome  | Preço  | ID')
            for i in cardapio:
                print(f'{i['nome']} | {i['preco']} | {i['id']}')

        
        case 4:
            pedido = list()
            nomeCliente = input('Digite o nome do cliente: ')
            compra = ''
            print('Digite 0 para sair.')
            while compra != '0':   
                while True:
                    compra = int(input('Digite o ID do produto que deseja comprar: '))
                    if compra == 0:
                        break
                    elif compra in listaIDs:
                        pedido.append(compra)
                    else:
                        print('ID inválido. Digite outro.')


                if not fila.isEmpty():
                    fila.enqueue(pedido)
                    sistema.push('Lançar Pedido')
                    print('Produtos adicionados à fila!')
                    print('Produtos no seu pedido:')
                    for i in cardapio:
                        if i['id'] in pedido:
                            print(i['nome'])
                    break
                else:
                    print('Pedido vazio. Não adicionado.')
        case 5:
            atendimento = fila.dequeue()
            sistema.push('Atender Pedido')
            print('Pedido atendido! IDs dos itens são:') 
            for i in atendimento:
                print(i)

        case 6:
            print('Fila:')
            for i in fila.showQueue():
                print(i)


        case 7:
            if sistema.top() == 'Atender Pedido':
                fila.enqueue(atendimento)
                print('Pedido enviado para o final da fila!')
            elif sistema.top() == 'Lançar Pedido':
                ultimoPedido = fila.showQueue().pop()
                print(f'Pedido {ultimoPedido} removido da fila!')

        case 8:
            print('Histórico de ações:')
            for i in sistema.showQueue():
                print(i)

        case 0:
            print('Programa encerrado.')
            break

        case _:
            print('Opção Inválida.')