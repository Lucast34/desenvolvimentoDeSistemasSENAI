from classes import Estoque
from classes import Produto

estoque = Estoque()
estoque.adicionar_produto(Produto(1, "Arroz", 20.00, 50))
estoque.adicionar_produto(Produto(2, "Feijão", 10.00, 30))

estoque.listar_produtos()

estoque.remover_produto(1, 20)
estoque.listar_produtos()
