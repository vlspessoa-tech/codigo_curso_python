lista_compras = []
valor_produto = []

while True:
    cadastro_produto = input(
        "\nO que deseja fazer? Digite:\n"
        "1 = inserir\n"
        "2 = apagar\n"
        "3 = listar valores dos produtos\n"
        "0 = sair\n").strip()

    if cadastro_produto == "1":
        produto = input("Digite novo produto: ").strip()#strip tira espaçoes extras
        if produto in lista_compras:
            print('Este produto já está na sua lista de compras')
            continue

        try:
            valor = float(input("Digite valor do produto: ").replace(",", "."))
        except ValueError:
            print("Valor inválido: digite um número (ex: 2.50).")
            continue

        lista_compras.append(produto)
        valor_produto.append(valor)
        print("Você incluiu o produto e seu valor na sua lista de compras.")
        
    elif cadastro_produto == "2":
        produto = input("Qual produto deseja remover? ").strip()

        if produto in lista_compras:
            idx = lista_compras.index(produto)
            lista_compras.pop(idx)
            valor_produto.pop(idx)
            print("Produto removido.")
        else:
            print("Produto não encontrado.")

    elif cadastro_produto == "3":
        if not lista_compras:
            print("Lista vazia.")
        else:
            for i, (prod, val) in enumerate(zip(lista_compras, valor_produto), start=1):
                print(f"{i}. {prod} - €{val:.2f}")

    elif cadastro_produto == "0":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida. Digite apenas 1, 2, 3 ou 0.")

