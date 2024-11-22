produtos = {
    'nomes' : ['Pastel','Leite'],
    'preco' : [7.50,4.99],
    'quantidade' : [7,10]
}

nome = input('Nome do produto :')
produtos.get('nomes').append(nome)

preco = float(input('Preço do produto :'))
produtos.get('preco').append(preco)

quantidade = int(input('Quantidade de estoque :'))
produtos.get('quantidade').append(quantidade)

for produto in produtos.items():
    print(f'💳 {produto[0]}')
    print(f'{produto[1]}')
    

