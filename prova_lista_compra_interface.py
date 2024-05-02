from prova_lista_compra import * 
# lista= Lista_produto
contador = True
while contador:
    
    print('1- Adicionar produto: ')
    print('2- Fazer compra: ')
    print('3- Modificar produto: ')
    print('4- Finalizar compra: ')

    opçao = int(input('Escolha o numero da opção desejada: '))
    if opçao == 1:
        lista.adicionar_produto()
    elif opçao == 2:
        lista.lista_compra()
    elif opçao == 3:
        lista.alterar_produto()
    elif opçao == 4: 
        lista.vlaor_final()
    elif opçao == 5:
        lista.pesquisar_produtos()
    elif opçao == 0:
        print('Obrigado! Até mais!')
        contador = False


