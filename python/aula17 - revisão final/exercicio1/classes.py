class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.codigo} - {self.nome} - R${self.preco:.2f} - {self.quantidade} unidades"

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        self.produtos[produto.codigo] = produto

    def remover_produto(self, codigo, quantidade):
        produto = self.produtos.get(codigo)
        if produto and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            if produto.quantidade == 0:
                del self.produtos[codigo]
            return True
        return False

    def listar_produtos(self):
        for produto in self.produtos.values():
            print(produto)
