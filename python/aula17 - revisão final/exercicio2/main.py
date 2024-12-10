class ItemPedido:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.calcular_total() for item in self.itens)

    def exibir_pedido(self):
        for item in self.itens:
            print(item.__dict__)
        print(f"Total do pedido: R${self.calcular_total():.2f}")

class Cardapio:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, preco):
        self.itens[nome] = preco

    def obter_preco(self, nome):
        return self.itens.get(nome, None)

cardapio = Cardapio()
cardapio.adicionar_item("Hamburguer", 15.00)
cardapio.adicionar_item("Batata Frita", 10.00)
cardapio.adicionar_item("Refrigerante", 5.00)

pedido = Pedido()
pedido.adicionar_item(ItemPedido("Hamburguer", cardapio.obter_preco("Hamburguer"), 2))
pedido.adicionar_item(ItemPedido("Batata Frita", cardapio.obter_preco("Batata Frita"), 1))
pedido.adicionar_item(ItemPedido("Refrigerante", cardapio.obter_preco("Refrigerante"), 3))

pedido.exibir_pedido()
