class Lista_produto:
    def __init__(self):
        self.produtos = {}  
        self.compras = {}
        self.valor_a_pagar = {}

    def adicionar_produto(self):
        produto = {}
        produto['nome'] = input('Nome produto: ')
        produto['quantidade_estoque'] = int(input('Quantidade do produto: '))
        produto['valor_unitario'] = float(input('Valor do produto: '))
        self.produtos[produto['nome']]= produto
        print(self.produtos)

    def alterar_produto(self):
        produto = {}
        nome_produto = input('Nome do produto que deseja alterar: ')
        if nome_produto in self.produtos:
            produto = self.produtos[nome_produto]
            produto['nome'] = input('Novo nome do produto: ')
            produto['quantidade_estoque'] = int(input('Nova quantidade do produto: '))
            produto['valor_unitario'] = float(input('Novo valor do produto: '))
            print("Produto alterado com sucesso!")
        else:
            print(f'O produto {nome_produto} não está cadastrado!')

    def lista_compra(self):
        item = {}
        nome_produto = input('Nome do produto: ')
        if nome_produto in self.produtos:
           
            item['quantidade'] = int(input('Quantidade do produto: '))
            item['valor_unitario'] = self.produtos[nome_produto]['valor_unitario']
            item['valor_total'] = item['quantidade'] * item['valor_unitario']
            # item['valor_compra'] = sum(item['valor_total'])
            self.produtos = self.produtos['quantidade_estique'] - self.compras[item['quantidade']]
            self.compras[nome_produto]= item
            # self.valor_a_pagar[item['valor_total']]= item
            # item['valor_compra'] = sum(nome_produto[item['valor_total']])
            # soma_itens[item['valor_total']]
            # self.valor_a_pagar = sum
            # self.valor_a_pagar = item['valor_total'] = item['valor_total']
            dados = self.compras

            valor_compra = 0
            for chave, valor in dados.items():
                valor = valor.get('valor_total')
                valor_compra += valor
            print(f'Os itens de sua compra são: {self.compras}')
            # print(f'Os itens que seram somados são: {soma_itens}')
            # print(f'O valor total a ser pago é: {self.compras[item["valor_compra"]]}')
            print(f'O valor total a ser pago é: {valor_compra}')
        else:
            print(f'O produto não está cadastrado')

    # def vlaor_final(self):
    #     for chave, valor in self.valor_a_pagar.items():
    #         valor.sum()
    #         # soma = sum(valores)
    #         print(f'O valor á pagar é: {valor}')
    # def valor_final(self):
    #     soma = sum(self.valor_a_pagar.values())
    #     print(f'O valor a pagar é: {soma}')
    #     # total_pagar = sum(self.valor_a_pagar[item[]])
    # def valor_final(self):
    #     soma = 0
    #     for valor in self.valor_a_pagar.values():
    #         soma += valor
    #     print(f'O valor a pagar é: {soma}')

    def pesquisar_produtos(self):
        print(self.produtos)

lista = Lista_produto()
#lista.adicionar_produto()
# # lista.alterar_produto()
# lista.lista_compra()
# # print(produtos.self['nome'])
# print(lista.compras)
# print(lista.produtos)
