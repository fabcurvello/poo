'''
Relação de Agregação -> Uma classe precisa da outra classe para executar sua ação,
ou seja, uma classe utiliza a outra como parte de si.

Ex: Classe CarrinhoDeCompras precisa da Classe Produto para funcionar.
Classe Produto independe da Classe CarrinhoDeCompra
'''

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if (len(self.produtos) != 0 ):
            print("Produtos no seu carrinho de compras:")
            for produto in self.produtos:
                print(f" - {produto.nome}: R$ {produto.preco}")
        else:
            print("Seu carrinho de compras existe, mas está vazio!")

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompras()

produto1 = Produto("Celular iPhone", 5000)
produto2 = Produto("Notebook Dell", 3800)

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

carrinho.listar_produtos()