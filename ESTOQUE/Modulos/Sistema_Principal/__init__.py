def menu():
    from Modulos import Produtos, Login_Usuário, Analisar_dados, Linhas
    import time
    # IMPORTAÇÕES - PRONTO
    Login_Usuário.prgt_usuário()
    Linhas.linha_verde()
    p = "\033[32mACESSO LIBERADO\033[0m"
    print(f"{p:^100}")
    Linhas.linha_verde()
    # LOGIN - PRONTO
    while True:
        Linhas.linha_azul()
        p = "MENU"
        print(f"\033[36m{p:^100}\033[0m")
        Linhas.linha_azul()
        # CABEÇALHO - PRONTO
        opções = ["Ver Produtos", "Cadastra Produto", "Analisar Estoque", "Sair do Sistema"]
        cont = 0
        for i in opções:
            cont += 1
            print(f"\033[33m{cont}º - {i}\033[0m")
        Linhas.linha_azul()
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
            Linhas.linha_azul()
            p = "\033[36mVer Produtos\033[0m"
            print(f"{p:^100}")
            Linhas.linha_azul()
            Produtos.ver_arquivos()
            Linhas.linha_azul()
        # OPÇÃO 1 - PRONTO
        if usuario == 2:
            Linhas.linha_azul()
            p = "\033[36mCadastra Produto\033[0m"
            print(f"{p:^100}")
            Linhas.linha_azul()
            Produtos.cdst_produto()
        # OPÇÃO 2 - PRONTO
        if usuario == 3:
            Linhas.linha_azul()
            p = "\033[36mAnalisando Estoque\033[0m"
            print(f"{p:^100}")
            Linhas.linha_azul()
            Analisar_dados.grafico()
        # OPÇÃO 3 - PRONTO
        if usuario == 4:
            time.sleep(1)
            Linhas.linha_verde()
            p = "\033[32mSAINDO DO SISTEMA\033[0m"
            print(f"{p:^100}")
            Linhas.linha_verde()
            time.sleep(2)
            print("\033[31mPROGRAMA FINALIZADO...\033[0m")
            break
        if usuario == 4:
            break
