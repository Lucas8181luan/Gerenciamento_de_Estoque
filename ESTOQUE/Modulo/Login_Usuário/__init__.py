def prgt_usuário():
    while True:
        import pandas as pd
        # IMPORTAÇÕES - PRONTO
        arquivo = "ESTOQUE/Modulo/Login_Usuário/Cadastro de Usuário.csv"
        df = pd.read_csv(arquivo)
        numeros_linhas = len(df)
        pgnt_usuário = str(input("Você Possui Cadastro Na Plataforma (SIM/NÃO): ")).strip().upper()
        if pgnt_usuário == "SIM":
            while True:
                print("-" * 40)
                numero_acesso = str(input("Seu Número de Acesso: "))
                nome = str(input("Seu Nome de Usuário: "))
                email = str(input("Digite Seu E-mail: "))
                senha = str(input("Digite Sua Senha: "))
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
    print("=" * 40)
    p = "CADASTRAMENTO DE USUÁRIO"
    print(f"{p:^40}")
    print("=" * 40)
    # CABEÇALHO - PRONTO
    import pandas as pd
    # IMPORTAÇÕES - PRONTO
    arquivo = "ESTOQUE/Modulo/Login_Usuário/Cadastro de Usuário.csv"
    df = pd.read_csv(arquivo)
    numeros_linhas = len(df)
    gerando_id = numeros_linhas + 1
    id_adicionar = gerando_id
    print("-" * 40)
    print(f"Guarde seu número de acesso = ",end="")
    print(f"\033[92m{id_adicionar}\033[0m")
    print("-" * 40)
    # ID - PRONTO
    print("-" * 40)
    p = "NOME USUÁRIO"
    print(f"{p:^40}")
    print("-" * 40)
    nome_usuário = str(input("Seu Nome: "))
    nome_adicionar = nome_usuário
    # NOME - PRONTO
    print("-" * 40)
    p = "CADASTRA E-MAIL"
    print(f"{p:^40}")
    print("-" * 40)
    while True:
        email = str(input("Digite um E-mail: "))
        email_dn = str(input("Digite o E-mail novamente: "))
        if email == email_dn:
            email_adicionar = email
            break
        else:
            print("\033[31mErro: Os E-mail Estão Diferentes!\033[0m")
    # E-MAIL - PRONTO
    print("-" * 40)
    p = "CADASTRA SENHA"
    print(f"{p:^40}")
    print("-" * 40)
    while True:
        senha = str(input('Digite uma Senha: '))
        senha_dn = str(input("Digite a Senha novamente: "))
        if senha == senha_dn:
            senha_adicionar = senha
            break
        else:
            print("\033[31mErro: As Senhas Estão Diferentes!\033[0m")
    # SENHA - PRONTO
    adicionar_dados = f"{id_adicionar},{nome_adicionar},{email_adicionar},{senha_adicionar}\n"
    nome_arquivo = "ESTOQUE/Modulo/Login_Usuário/Cadastro de Usuário.csv"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar_dados)
    # ADICIONAR DADOS - PRONTO
    linha = "=" * 80
    adicionar = f'{linha}'
    nome_arquivo = "ESTOQUE/Modulo/Login_Usuário/Cadastro de Usuário.csv"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar)
    # LINHA - PRONTO


def verificar_login(login):
    import pandas as pd
    arquivo_excel = "ESTOQUE/Modulo/Login_Usuário/Cadastro de Usuário.csv"
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
