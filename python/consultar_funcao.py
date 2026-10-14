def consultar_cia(con):
    cursor = con.cursor()
    print("\n--- CONSULTAR COMPANHIA AÉREA (CIA) ---")
    print("1 - Consultar todas as companhias")
    print("2 - Consultar por código")
    opcao = input("Escolha uma opção: ")

    comando_sql = ""
    parametros = None  # Alterado de () para None para melhor controle

    if opcao == "1":
        comando_sql = "SELECT * FROM cia"

    elif opcao == "2":
        try:
            # Convertido para int para bater com o tipo de dado do banco
            codigo = int(input("Digite o código da companhia (número): "))
            comando_sql = "SELECT * FROM cia WHERE codigo = %s"
            parametros = [codigo]  # Alterado de tupla (codigo,) para lista [codigo]
        except ValueError:
            print("Erro: O código deve ser um número inteiro.")
            cursor.close()
            return

    else:
        print("Opção inválida.")
        cursor.close()
        return

    try:
        # Se parametros for None, passamos apenas o comando_sql
        if parametros:
            cursor.execute(comando_sql, parametros)
        else:
            cursor.execute(comando_sql)

        resultados = cursor.fetchall()

        if resultados:
            for row in resultados:
                print(row)
        else:
            print("Nenhum resultado encontrado.")

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

    finally:
        cursor.close()


def consultar_aeroporto(con):
    print("\n--- CONSULTAR AEROPORTO ---")
    cursor = con.cursor()
    print("1 - Consultar todos os aeroportos")
    print("2 - Consultar por código")
    opcao = input("Escolha uma opção: ")

    comando_sql = ""
    parametros = ()

    if opcao == "1":
        comando_sql = "SELECT * FROM aeroporto"

    elif opcao == "2":
        codigo = input("Digite o código do aeroporto: ")

        comando_sql = "SELECT * FROM aeroporto WHERE codigo = %s"
        parametros = (codigo,)

    else:
        print("Opção inválida.")
        return

    try:
        cursor.execute(comando_sql, parametros)
        resultados = cursor.fetchall()

        if resultados:
            for row in resultados:
                print(row)
        else:
            print("Nenhum resultado encontrado.")

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

    finally:
        cursor.close()


def consultar_tipo_aeronave(con):
    print("\n--- CONSULTAR TIPO DE AERONAVE ---")
    cursor = con.cursor()
    print("1 - Consultar todos os tipos de aeronave")
    print("2 - Consultar por código")
    opcao = input("Escolha uma opção: ")

    comando_sql = ""
    parametros = ()

    if opcao == "1":
        comando_sql = "SELECT * FROM tipo_aeronave"

    elif opcao == "2":
        codigo = input("Digite o código do tipo de aeronave: ")

        comando_sql = "SELECT * FROM tipo_aeronave WHERE codigo = %s"
        parametros = (codigo,)

    else:
        print("Opção inválida.")
        return

    try:
        cursor.execute(comando_sql, parametros)
        resultados = cursor.fetchall()

        if resultados:
            for row in resultados:
                print(row)
        else:
            print("Nenhum resultado encontrado.")

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

    finally:
        cursor.close()


def consultar_Cia_aeroporto(con):
    print("\n--- CONSULTAR CIA EM AEROPORTO (OPERAÇÃO) ---")
    cursor = con.cursor()
    print("1 - Consultar todas as operações")
    print("2 - Consultar por código da companhia")
    opcao = input("Escolha uma opção: ")

    comando_sql = ""
    parametros = ()

    if opcao == "1":
        comando_sql = "SELECT * FROM cia_aeroporto"

    elif opcao == "2":
        codigo_cia = input("Digite o código da companhia: ")

        comando_sql = "SELECT * FROM cia_aeroporto WHERE codigo_cia = %s"
        parametros = (codigo_cia,)

    else:
        print("Opção inválida.")
        return

    try:
        cursor.execute(comando_sql, parametros)
        resultados = cursor.fetchall()

        if resultados:
            for row in resultados:
                print(row)
        else:
            print("Nenhum resultado encontrado.")

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

    finally:
        cursor.close()


def consultar_Cia_tipo_aeronave(con):
    print("\n--- CONSULTAR CIA EM TIPO DE AERONAVE (AQUISIÇÃO) ---")
    cursor = con.cursor()
    print("1 - Consultar todas as aquisições")
    print("2 - Consultar por código da companhia")
    opcao = input("Escolha uma opção: ")

    comando_sql = ""
    parametros = ()

    if opcao == "1":
        comando_sql = "SELECT * FROM cia_tipo_aeronave"

    elif opcao == "2":
        codigo_cia = input("Digite o código da companhia: ")

        comando_sql = "SELECT * FROM cia_tipo_aeronave WHERE codigo_cia = %s"
        parametros = (codigo_cia,)

    else:
        print("Opção inválida.")
        return

    try:
        cursor.execute(comando_sql, parametros)
        resultados = cursor.fetchall()

        if resultados:
            for row in resultados:
                print(row)
        else:
            print("Nenhum resultado encontrado.")

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

    finally:
        cursor.close()
