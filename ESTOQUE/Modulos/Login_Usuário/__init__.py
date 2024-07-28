import pandas as pd
from Modulos import Linhas
# IMPORTAÇÕES - PRONTO

def prgt_usuário():
    import pandas as pd
    from Modulos import Linhas
    # IMPORTAÇÕES - PRONTO
    while True:
        arquivo = "ESTOQUE/Modulos/Banco de Dados/Cadastro de Usuário.csv"
        df = pd.read_csv(arquivo)
        numeros_linhas = len(df)
        pgnt_usuário = str(input("Você Possui Cadastro Na Plataforma (SIM/NÃO): ")).strip().upper()[0]
        if pgnt_usuário == "S":
            if numeros_linhas < 1:
                print("\033[31mErro: Você não possui cadastro\033[0m")
                continue
            else:
                while True:
                    Linhas.linha_azul()
                    numero_acesso = str(input("\033[36mSeu Número de Acesso: \033[0m"))
                    Linhas.linha_azul()
                    nome = str(input("\033[36mSeu Nome de Usuário: \033[0m"))
                    Linhas.linha_azul()
                    email = str(input("\033[36mDigite Seu E-mail: \033[0m"))
                    Linhas.linha_azul()
                    senha = str(input("\033[36mDigite Sua Senha: \033[0m"))
                    Linhas.linha_azul()
                    junta = numero_acesso + nome + email + senha
                    verificando_login = verificar_login(junta)
                    if verificando_login == True:
                        break
                    else:
                        print("\033[31mErro: Numero de Acesso, Nome de Usuário, E-mail ou Senha incorreto!\033[0m")
            break
        else:
            if numeros_linhas > 1:
                print("\033[31mErro: Você ja possui cadastro\033[0m")
            else:
                cdst_usuário()
            

def cdst_usuário():
    Linhas.linha_verde()
    p = "\033[32mCADASTRAMENTO DE USUÁRIO\033[0m"
    print(f"{p:^100}")
    Linhas.linha_verde()
    # CABEÇALHO - PRONTO
    import pandas as pd
    # IMPORTAÇÕES - PRONTO
    arquivo = "ESTOQUE/Modulos/Banco de Dados/Cadastro de Usuário.csv"
    df = pd.read_csv(arquivo)
    numeros_linhas = len(df)
    gerando_id = numeros_linhas + 1
    id_adicionar = gerando_id
    Linhas.linha_amarela()
    print(f"\033[33mGuarde seu número de acesso = \033[0m",end="")
    print(f"\033[92m{id_adicionar}\033[0m")
    Linhas.linha_amarela()
    # ID - PRONTO
    Linhas.linha_amarela()
    p = "\033[33mNOME USUÁRIO\033[0m"
    print(f"{p:^100}")
    Linhas.linha_amarela()
    nome_usuário = str(input("\033[33mSeu Nome: \033[0m"))
    nome_adicionar = nome_usuário
    # NOME - PRONTO
    Linhas.linha_amarela()
    p = "\033[33mCADASTRA E-MAIL\033[0m"
    print(f"{p:^100}")
    Linhas.linha_amarela()
    while True:
        email = str(input("\033[33mDigite um E-mail: \033[0m"))
        email_dn = str(input("\033[33mDigite o E-mail novamente: \033[0m"))
        if email == email_dn:
            email_adicionar = email
            break
        else:
            print("\033[31mErro: Os E-mail Estão Diferentes!\033[0m")
            Linhas.linha_amarela()
    # E-MAIL - PRONTO
    Linhas.linha_amarela()
    p = "\033[33mCADASTRA SENHA\033[0m"
    print(f"{p:^100}")
    Linhas.linha_amarela()
    while True:
        senha = str(input("\033[33mDigite uma Senha: \033[0m"))
        senha_dn = str(input("\033[33mDigite a Senha novamente: \033[0m"))
        if senha == senha_dn:
            senha_adicionar = senha
            break
        else:
            print("\033[31mErro: As Senhas Estão Diferentes!\033[0m")
            Linhas.linha_amarela()
    # SENHA - PRONTO
    adicionar_dados = f"{id_adicionar},{nome_adicionar},{email_adicionar},{senha_adicionar}\n"
    nome_arquivo = "ESTOQUE/Modulos/Banco de Dados/Cadastro de Usuário.csv"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar_dados)
    # ADICIONAR DADOS - PRONTO
    linha = "=" * 80
    adicionar = f'{linha}'
    nome_arquivo = "ESTOQUE/Modulos/Banco de Dados/Cadastro de Usuário.csv"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar)
    # LINHA - PRONTO
    Linhas.linha_verde()
    p = "\033[32mCADASTRAMENTO REALIZADO COM SUCESSO!\033[0m"
    print(f"{p:^100}")
    Linhas.linha_verde()


def verificar_login(login):
    import pandas as pd
    arquivo_excel = "ESTOQUE/Modulos/Banco de Dados/Cadastro de Usuário.csv"
    df = pd.read_csv(arquivo_excel)
    # ACHAR ARQUIVO - PRONTO
    valor_celula_numero_acesso = df.at[0, "ID"]
    valor_celula_nome = df.at[0, "Nome"]
    valor_celula_email = df.at[0, "E-mail"]
    valor_celula_senha = df.at[0, "Senha"]
    login_cdst = valor_celula_numero_acesso + valor_celula_nome + valor_celula_email + valor_celula_senha
    if login == login_cdst:
        return True
    else:
        return False
    # PUXAR DADOS - PRONTO
