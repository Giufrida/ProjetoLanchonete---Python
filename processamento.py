from pilha import Pilha
from fila import Fila

class Restaurante:
    def __init__(self):
        self.cardapio = []
        self.fila = Fila()
        self.historico = Pilha()

    def buscar(self, id):
        return next((i for i in self.cardapio if i['id'] == id), None)

    def cadastrar_item(self, id, nome, preco):
        if not nome:
            raise ValueError('Informe o nome do item.')
        if self.buscar(id):
            raise ValueError('ID já cadastrado.')
        item = {'id': id, 'nome': nome, 'preco': preco}
        self.cardapio.append(item)
        self.historico.push(('Cadastrar Item', item))

    def remover_item(self, id):
        item = self.buscar(id)
        if not item:
            raise ValueError('ID não encontrado.')
        self.cardapio.remove(item)
        self.historico.push(('Remover Item', item))

    def lancar_pedido(self, cliente, ids):
        if not cliente:
            raise ValueError('Informe o nome do cliente.')
        if not ids:
            raise ValueError('Pedido vazio.')
        itens = [self.buscar(i) for i in ids]
        if None in itens:
            raise ValueError('Pedido contém item removido do cardápio.')
        pedido = {'cliente': cliente, 'itens': itens}
        self.fila.enqueue(pedido)
        self.historico.push(('Lançar Pedido', pedido))

    def atender_pedido(self):
        if self.fila.isEmpty():
            raise ValueError('Fila da cozinha vazia.')
        pedido = self.fila.dequeue()
        self.historico.push(('Atender Pedido', pedido))
        return pedido

    def itens_fila(self):
        return list(self.fila.showQueue())

    def desfazer(self):
        if self.historico.isEmpty():
            raise ValueError('Nada para desfazer.')
        acao, dado = self.historico.pop()
        if acao == 'Cadastrar Item':
            self.cardapio.remove(dado)
        elif acao == 'Remover Item':
            self.cardapio.append(dado)
        elif acao == 'Atender Pedido':
            self.fila.enqueue(dado)
        elif acao == 'Lançar Pedido':
            pedidos = []
            while not self.fila.isEmpty():
                pedidos.append(self.fila.dequeue())
            pedidos.pop()
            for p in pedidos:
                self.fila.enqueue(p)
        return acao

    def historico_acoes(self):
        aux = []
        while not self.historico.isEmpty():
            aux.append(self.historico.pop())
        for x in reversed(aux):
            self.historico.push(x)
        return [a for a, _ in aux]
