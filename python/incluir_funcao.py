import mysql.connector
from mysql.connector import Error


def conectar_banco():
    """Tenta conectar ao banco de dados e devolve a conexão."""
    try:
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="clube2026_2"
        )
        if conexao.is_connected():
            print("\n Conexão realizada com sucesso ao banco 'clube2026_2'!")
            return conexao
    except Error as e:
        print(f"\n Erro ao conectar ao banco de dados: {e}")
        return None


def incluir_aeroporto(con):
    """Insere dados na tabela aeroporto."""
    cursor = con.cursor()
    print("\n--- INCLUIR NOVO AEROPORTO ---")

    codigo = int(input("Digite o código do aeroporto (número): "))
    descricao = input("Digite a descrição/nome: ")
    telefone = input("Digite o telefone (10 dígitos): ")
    endereco = input("Digite o endereço: ")

    comando_sql = "INSERT INTO aeroporto (codigo, descricao, telefone, endereco) VALUES (%s, %s, %s, %s)"
    dados = (codigo, descricao, telefone, endereco)

    try:
        cursor.execute(comando_sql, dados)
        con.commit()
        print("\n Aeroporto cadastrado com sucesso!")
    except Error as erro:
        print(f"\n Erro ao inserir no banco: {erro}")
    finally:
        cursor.close()


def incluir_cia(con):
    """Insere dados na tabela cia."""
    cursor = con.cursor()
    print("\n--- INCLUIR NOVA COMPANHIA (CIA) ---")

    codigo = int(input("Digite o código da CIA (número): "))
    nome = input("Digite o nome da companhia (ex: Gol, Azul): ")
    status = input("Digite o status (A - Ativo / I - Inativo): ")

    comando_sql = "INSERT INTO cia (codigo, nome, status) VALUES (%s, %s, %s)"
    dados = (codigo, nome, status)

    try:
        cursor.execute(comando_sql, dados)
        con.commit()
        print("\n Companhia cadastrada com sucesso!")
    except Error as erro:
        print(f"\n Erro ao inserir no banco: {erro}")
    finally:
        cursor.close()


def incluir_tipo_aeronave(con):
    """Insere dados na tabela tipo_aeronave."""
    cursor = con.cursor()
    print("\n--- INCLUIR TIPO DE AERONAVE ---")

    codigo = int(input("Digite o código do tipo (número): "))
    descricao = input("Digite a descrição (ex: Boeing 737): ")
    peso = int(input("Digite o peso (número inteiro): "))
    qtd_pass = int(input("Digite a quantidade de passageiros: "))

    comando_sql = "INSERT INTO tipo_aeronave (codigo, descricao, peso, qtd_pass) VALUES (%s, %s, %s, %s)"
    dados = (codigo, descricao, peso, qtd_pass)

    try:
        cursor.execute(comando_sql, dados)
        con.commit()
        print("\n Tipo de aeronave cadastrado com sucesso!")
    except Error as erro:
        print(f"\n Erro ao inserir no banco: {erro}")
    finally:
        cursor.close()


def incluir_cia_aeroporto(con):
    """Insere dados na tabela de vínculo cia_aeroporto."""
    cursor = con.cursor()
    print("\n--- VINCULAR COMPANHIA A AEROPORTO ---")

    codigo_cia = int(input("Digite o código da CIA existente: "))
    codigo_aeroporto = int(input("Digite o código do aeroporto existente: "))
    dt_inicio = input("Digite a data de início (Formato: AAAA-MM-DD): ")

    comando_sql = "INSERT INTO cia_aeroporto (codigo_cia, codigo_aeroporto, dt_inicio_operacao) VALUES (%s, %s, %s)"
    dados = (codigo_cia, codigo_aeroporto, dt_inicio)

    try:
        cursor.execute(comando_sql, dados)
        con.commit()
        print("\n Vínculo de operação registrado com sucesso!")
    except Error as erro:
        print(
            f"\n Erro: Verifique se os códigos digitados existem nas tabelas originais. ({erro})"
        )
    finally:
        cursor.close()


def incluir_cia_tipo_aeronave(con):
    """Insere dados na tabela de vínculo cia_tipo_aeronave."""
    cursor = con.cursor()
    print("\n--- VINCULAR AERONAVE A UMA COMPANHIA ---")

    codigo_cia = int(input("Digite o código da CIA existente: "))
    codigo_tipo_aer = int(input("Digite o código do tipo de aeronave existente: "))
    dt_aquisicao = input("Digite a data de aquisição (Formato: AAAA-MM-DD): ")
    status = input("Digite o status da aeronave (A - Ativo / I - Inativo): ")

    comando_sql = "INSERT INTO cia_tipo_aeronave (codigo_cia, codigo_tipo_aer, Data_aquisicao, status) VALUES (%s, %s, %s, %s)"
    dados = (codigo_cia, codigo_tipo_aer, dt_aquisicao, status)

    try:
        cursor.execute(comando_sql, dados)
        con.commit()
        print("\n Aeronave vinculada à companhia com sucesso!")
    except Error as erro:
        print(
            f"\n Erro: Verifique se os códigos digitados existem nas tabelas originais. ({erro})"
        )
    finally:
        cursor.close()
