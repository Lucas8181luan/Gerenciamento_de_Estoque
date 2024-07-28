def menu():
    from Modulo import Produtos, Login_Usuário
    # IMPORTAÇÕES - PRONTO
    Login_Usuário.prgt_usuário()
    print("\033[92m=" * 40)
    p = "ACESSO LIBERADO"
    print(f"{p:^40}")
    print("=" * 40 + "\033[0m")
    # LOGIN - PRONTO
    while True:
        print("-" * 40)
        p = "MENU"
        print(f"{p:^40}")
        print("-" * 40)
        # CABEÇALHO - PRONTO
        opções = ["Ver Estoque", "Cadastra Produto", "Analisar Quantidade", "Sair do Sistema"]
        cont = 0
        for i in opções:
            cont += 1
            print(f"{cont}º - {i}")
        print("-" * 40)
        # OPÇÕES - PRONTO
        while True:
            try:
                usuario = int(input("Escolha Uma Opção: "))
                if usuario == 1 or usuario == 2 or usuario == 3 or usuario == 4:
                    break
            except ValueError:
                print("\033[31mErro: Escolha uma opção valida!\033[0m")
            else:
                print("\033[31mErro: Escolha um número valido!\033[0m")
        # OPÇÕES ESCOLHIDAS - PRONTO
        if usuario == 1:
            print("=" * 100)
            Produtos.ver_arquivos()
            print("=" * 100)
        # OPÇÃO 1 - PRONTO
        if usuario == 2:
            print("-" * 40)
            p = "CADASTRA PRODUTO"
            print(f"{p:^40}")
            print("-" * 40)
            Produtos.cdst_produto()
        # OPÇÃO 2 - PRONTO
