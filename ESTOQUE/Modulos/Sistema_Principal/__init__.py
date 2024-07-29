def menu():
    from Modulos import Produtos, Login_Usuário, Gráfico_de_dados, Funcionários
    import time
    # IMPORTAÇÕES - PRONTO
    Login_Usuário.prgt_usuário()
    linha_verde()
    p = "\033[32mACESSO LIBERADO\033[0m"
    print(f"{p:^100}")
    linha_verde()
    # LOGIN - PRONTO
    while True:
        linha_azul()
        p = "MENU"
        print(f"\033[36m{p:^100}\033[0m")
        linha_azul()
        # CABEÇALHO - PRONTO
        opções = ["Ver Produtos", "Cadastra Produto", "Analisar Estoque", "Ver Funcionários", "Sair do Sistema"]
        cont = 0
        for i in opções:
            cont += 1
            print(f"\033[33m{cont}º - {i}\033[0m")
        linha_azul()
        # OPÇÕES - PRONTO
        while True:
            try:
                usuario = int(input("Escolha Uma Opção: "))
                if usuario == 1 or usuario == 2 or usuario == 3 or usuario == 4 or usuario == 5:
                    break
            except ValueError:
                print("\033[31mErro: Escolha uma opção valida!\033[0m")
            else:
                print("\033[31mErro: Escolha um número valido!\033[0m")
        # OPÇÕES ESCOLHIDAS - PRONTO
        if usuario == 1:
            linha_azul()
            p = "\033[36mVer Produtos\033[0m"
            print(f"{p:^100}")
            linha_azul()
            Produtos.ver_arquivos()
            linha_azul()
        # OPÇÃO 1 - PRONTO
        if usuario == 2:
            linha_azul()
            p = "\033[36mCadastra Produto\033[0m"
            print(f"{p:^100}")
            linha_azul()
            Produtos.cdst_produto()
        # OPÇÃO 2 - PRONTO
        if usuario == 3:
            linha_azul()
            p = "\033[36mAnalisando Estoque\033[0m"
            print(f"{p:^100}")
            linha_azul()
            Gráfico_de_dados.grafico()
        # OPÇÃO 3 - PRONTO
        if usuario == 4:
            linha_azul()
            p = "\033[36mVer Funcionários\033[0m"
            print(f"{p:^100}")
            linha_azul()
            Funcionários.ver_funcionários()
        # OPÇÃO 4 - PRONTO
        if usuario == 5:
            time.sleep(1)
            linha_vermelha()
            p = "\033[31mSAINDO DO SISTEMA\033[0m"
            print(f"{p:^100}")
            linha_vermelha()
            time.sleep(2)
            print("\033[31mPROGRAMA FINALIZADO...\033[0m")
            break
        if usuario == 5:
            break
        # OPÇÃO 5 - PRONTO
    # MENU - PRONTO




#==========================================================================
#                        LINHAS PERSONALIZADAS
#==========================================================================
def linha_vermelha():
    print("\033[31m=\033[0m" * 100)


def linha_verde():
    print("\033[32m=\033[0m" * 100)


def linha_azul():
    print("\033[36m=\033[0m" * 100)


def linha_amarela():
    print("\033[33m=\033[0m" * 100) 
#==========================================================================