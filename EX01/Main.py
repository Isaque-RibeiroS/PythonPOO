from Produto import Produto

sair = False
espacamento = "-" * 60
catalogo_produtos = [0]
id_produto = 0

print(espacamento)
print("SISTEMA DE ESTOQUE")
print(espacamento)

while sair == False:
    print("Digite: \n [0]-SAIR \n [1]-NOVO PRODUTO \n [2]-OLHAR CATÁLOGO \n [3]-ADICIONAR ESTOQUE \n [4]-MODIFICAR PRODUTO")
    acao = str(input("R: "))
    print(espacamento)

# Em caso de OPÇÃO INVÁLIDA

    if acao != "0" and acao != "1" and acao != "2" and acao != "3" and acao != "4":
        print('\033[31mOpção inválida, tente novamente\033[0m')
        continue

# Opção para SAIR

    if int(acao) == 0:
        sair = True
        print('\033[31mSistema encerrado\033[0m')

# Opção de NOVO PRODUTO

    if int(acao) == 1:

        nome = str(input("Nome do produto: "))
        preco = str(input("Preço: "))
        quantidade = str(input("Quantidade: "))

        try:
            float(preco)
            int(quantidade)
        except ValueError:
            print("\033[31mDados inválidos, produto não registrado\033[0m")
            print(espacamento)
            continue

        catalogo_produtos.append(id_produto)
        id_produto += 1
        catalogo_produtos[id_produto-1] = Produto(nome, float(preco), int(quantidade),id_produto)
        print(espacamento)

# Opção de OLHAR CATÁLOGO

    if int(acao) == 2:

        if(id_produto == 0):
            print("\033[31mNenhum produto encontrado\033[0m")
            print(espacamento)
            continue

        for i in range(id_produto):

            if catalogo_produtos[i] == None:
                continue
            catalogo_produtos[i].mostrar_produto()
            print(espacamento)

# Opção de ADICIONAR ESTOQUE

    if int(acao) == 3:
        pesquisar_produto = str(input("Digite o N° do produto: "))

        try:
            int(pesquisar_produto)
        except ValueError:
            print("\033[31mDados inválidos, operação cancelada\033[0m")
            print(espacamento)
            continue
        if int(pesquisar_produto) == 0:
            print("\033[31mNenhum produto encontrado\033[0m")
            print(espacamento)
            continue
        contador = 0
        for i in range(len(catalogo_produtos)):
            contador += 1
            if i == int(pesquisar_produto):
                print(espacamento)
                catalogo_produtos[i-1].mostrar_produto()
                print(espacamento)
                adicao = str(input("Digite a quantidade a ser adicionada ao estoque: "))

                try:
                    int(adicao)
                except ValueError:
                    print("\033[31mDados inválidos, operação cancelada\033[0m")
                    print(espacamento)
                    break

                catalogo_produtos[i-1].adicionar_estoque(int(adicao))
                print("Operação realizada com sucesso")
                print(espacamento)
                break
            if contador == len(catalogo_produtos):
                print("\033[31mNenhum produto encontrado\033[0m")
                print(espacamento)

# Opção de MODIFICAR PRODUTO

    if int(acao) == 4:
        pesquisar_produto = str(input("Digite o N° do produto: "))

        try:
            int(pesquisar_produto)
        except ValueError:
            print("\033[31mDados inválidos, operação cancelada\033[0m")
            print(espacamento)
            continue
        if len(catalogo_produtos) == 1 or int(pesquisar_produto) == 0:
            print("\033[31mNenhum produto encontrado\033[0m")
            print(espacamento)
            continue
        contador = 0
        for i in range(len(catalogo_produtos)):
            contador += 1
            if i == int(pesquisar_produto):
                print(espacamento)
                catalogo_produtos[i - 1].mostrar_produto()
                print(espacamento)

                nome = str(input("Novo nome: "))
                preco = str(input("Novo preço: "))
                quantidade = str(input("Nova quantidade: "))

                try:
                    float(preco)
                    int(quantidade)
                except ValueError:
                    print("\033[31mDados inválidos, produto não registrado\033[0m")
                    print(espacamento)
                    break

                catalogo_produtos[i-1].set_nome(nome)
                catalogo_produtos[i-1].set_preco(preco)
                catalogo_produtos[i-1].set_quantidade(quantidade)
                print("Operação realizada com sucesso")
                print(espacamento)
                break
            if contador == len(catalogo_produtos):
                print("\033[31mNenhum produto encontrado\033[0m")
                print(espacamento)

