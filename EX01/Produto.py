class Produto:

    def __init__(self, nome, preco, quantidade,id_produto):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.id_produto = id_produto

    def get_nome(self):
        return self.nome
    def get_preco(self):
        return self.preco
    def get_quantidade(self):
        return self.quantidade
    def get_id_produto(self):
        return self.id_produto

    def set_nome(self, nome):
        self.nome = nome
    def set_preco(self, preco):
        self.preco = preco
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
    def set_id_produto(self, id_produto):
        self.id_produto = id_produto


    def mostrar_produto(self):
        print("N° do produto: {} ".format(self.id_produto))
        print("Nome: {}".format(self.nome))
        print("R$:{}".format(self.preco))
        print("Quantidade: {}".format(self.quantidade))

    def adicionar_estoque(self,aumento):
        self.quantidade += aumento

