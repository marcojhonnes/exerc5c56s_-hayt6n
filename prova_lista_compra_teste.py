class Lista_produto:
    def __init__(self, nome_produto, quantidade_estoque, valor_unitario):
        self.nome_produto = nome_produto
        self.quantidade_estoque = quantidade_estoque
        self.valor_unitario = valor_unitario
        # self.lista_produtos = {}
        # self.valor_total = quantidade * valor_unitario
        self.lista_produtos = {}
    def adicionar_produto(self):
        produto = {}
        produto['nome'] = input('Nome produto: ')
        produto['quantidade_estoque']= int(input('Quntifdade do produto: '))
        produto['valor_unitario']= int(input('Valor do produto: '))
        self.lista_produtos[produto['nome']]= produto
        print(self.lista_produtos)

    def auterar_produto(self):
        produto = {}
        nome_produto = input('Nome do  produto que deseja alterar: ')
        if nome_produto in self.lista_produtos:
            del produto['nome_produto']
            produto['nome'] = input('Nome produto: ')
            produto['quantidade_estoque']= int(input('Quntifdade do produto: '))
            produto['valor_unitario']= int(input('Valor do produto: '))
            self.lista_produtos[produto['nome']]= produto
            print(self.lista_produtos)
        else:
            print(f'produto {nome_produto} não cadastrado!')
        
produto = Lista_produto('arroz', 1, 2)
for i in range(2):
    produto.adicionar_produto()
    produto.auterar_produto()

    


# class Lista_compra(Lista_produto):
#     def __init__(self, nome_produto, quantidade_produto):
#         self.nome_produto = nome_produto
#         self.quantidade_produto = quantidade_produto
#         self.valor_unitario = valor_unitario
#         self.valor_total = quantidade_produto * valor_unitario

    # def adicionar_produto(self):
    #     produto = input('digite o nome do produto: ')
    #     if produto in self.lista_produto:
    #         self.quantidade = int(input('digite a quantidade do produto: '))
    #         lista_Compra = 
    #     self.produtos.append(produto)

#     def visualizar_lista(self):
#         if not self.produtos:
#             print("A lista de compras está vazia.")
#             return

#         print("Lista de compras:")
#         for produto in self.produtos:
#             print(f"Produto: {produto.nome} | Quantidade: {produto.quantidade} | Valor unitário: R${produto.valor_unitario:.2f} | Valor total: R${produto.valor_total:.2f}")

#         valor_total_compras = sum(produto.valor_total for produto in self.produtos)
#         print(f"Valor total da lista: R${valor_total_compras:.2f}")

#     def atualizar_produto(self, nome, nova_quantidade, novo_valor_unitario):
#         for produto in self.produtos:
#             if produto.nome == nome:
#                 produto.quantidade = nova_quantidade
#                 produto.valor_unitario = novo_valor_unitario
#                 produto.atualizar_total()
#                 print("Informações do produto atualizadas com sucesso.")
#                 return
#         print("Produto não encontrado na lista.")

#     def remover_produto(self, nome):
#         for produto in self.produtos:
#             if produto.nome == nome:
#                 self.produtos.remove(produto)
#                 print("Produto removido da lista.")
#                 return
#         print("Produto não encontrado na lista.")


# produto = Lista_produto('arroz', 10, 25)
# produto.adicionar_produto()
# lista_compras = ListaDeCompras()
# lista_compras.adicionar_produto("Arroz", 2, 5.0)
# lista_compras.adicionar_produto("Feijão", 1, 6.5)
# lista_compras.adicionar_produto("Carne", 3, 25.0)

# lista_compras.visualizar_lista()

# lista_compras.atualizar_produto("Arroz", 3, 4.0)
# lista_compras.remover_produto("Feijão")

# lista_compras.visualizar_lista()
