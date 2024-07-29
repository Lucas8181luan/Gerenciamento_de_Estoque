def relata():
    import csv
    from Modulos import Sistema_Principal
    # IMPORTAÇÕES - PRONTO
    relato_usuário = str(input("\033[31mRelate o Problema Que Está Tendo: \033[0m"))
    linha = f"{"=" * 100}"
    relatos = [relato_usuário]
    nome_arquivo = "ESTOQUE/Modulos/Banco de Dados/Relatos ao Suporte.csv"
    with open(nome_arquivo, mode='a', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(relatos)
        arquivo.write(linha)
    Sistema_Principal.linha_verde()
    print("\033[32mSEU RELATO FOI ENVIADO AO GERENTE! EM BREVE ENTRAREMOS EM CONTATO\033[0m")
    Sistema_Principal.linha_verde()
