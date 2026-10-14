from incluir_funcao import (
    conectar_banco,
    incluir_aeroporto,
    incluir_cia,
    incluir_tipo_aeronave,
    incluir_cia_aeroporto,
    incluir_cia_tipo_aeronave,
)
from consultar_funcao import (
    consultar_aeroporto,
    consultar_cia,
    consultar_tipo_aeronave,
    consultar_Cia_aeroporto,
    consultar_Cia_tipo_aeronave,
)

# Variável para armazenar a conexão ativa
conexao = None


while True:
    print("===============================")
    print("==           menu            ==")
    print("===============================")
    print("==           menu            ==")
    print("===============================")
    print()
    print("1 - Conectar")
    print("2 - Consultar")
    print("3 - Alterar")
    print("4 - Incluir")
    print("5 - Excluir")
    print("6 - Sair")
    print()

    resposta = input("Digite a opção desejada: ")

    match resposta:
        case "1":
            if conexao is None or not conexao.is_connected():
                conexao = conectar_banco()
            else:
                print("\n O banco de dados já está conectado!")

        case "2":
            if conexao and conexao.is_connected():
                print("\nQual tabela você deseja consultar?")
                print("1 - Aeroporto")
                print("2 - Companhia Aérea (CIA)")
                print("3 - Tipo de Aeronave")
                print("4 - CIA em Aeroporto (Operação)")
                print("5 - CIA em Tipo de Aeronave (Aquisição)")
                cosulta_opcao = input("Escolha uma opção de consulta: ")
                match cosulta_opcao:
                    case "1":
                        consultar_aeroporto(conexao)
                    case "2":
                        consultar_cia(conexao)
                    case "3":
                        consultar_tipo_aeronave(conexao)
                    case "4":
                        consultar_Cia_aeroporto(conexao)
                    case "5":
                        consultar_Cia_tipo_aeronave(conexao)
                    case _:
                        print("\n Opção de consulta inválida!")

            else:
                print("\n Por favor, conecte-se ao banco primeiro (Opção 1).")

        case "3":
            if conexao and conexao.is_connected():
                print("\n[Alterar] Aqui entrará a lógica do UPDATE...")
            else:
                print("\n Por favor, conecte-se ao banco primeiro (Opção 1).")

        case "4":
            if conexao and conexao.is_connected():
                print("\n--- O QUE VOCÊ DESEJA INCLUIR? ---")
                print("1 - Aeroporto")
                print("2 - Companhia Aérea (CIA)")
                print("3 - Tipo de Aeronave")
                print("4 - Operação (CIA em Aeroporto)")
                print("5 - Aquisição (Aeronave de uma CIA)")
                print()

                opcao_incluir = input("Escolha uma opção de inclusão: ")

                match opcao_incluir:
                    case "1":
                        incluir_aeroporto(conexao)
                    case "2":
                        incluir_cia(conexao)
                    case "3":
                        incluir_tipo_aeronave(conexao)
                    case "4":
                        incluir_cia_aeroporto(conexao)
                    case "5":
                        incluir_cia_tipo_aeronave(conexao)
                    case _:
                        print("\n Opção de inclusão inválida!")
            else:
                print("\n Por favor, conecte-se ao banco primeiro (Opção 1).")
        case "5":
            if conexao and conexao.is_connected():
                print("\n[Excluir] Aqui entrará a lógica do DELETE...")
            else:
                print("\n Por favor, conecte-se ao banco primeiro (Opção 1).")

        case "6":
            print("\n Encerrando o sistema...")
            if conexao and conexao.is_connected():
                conexao.close()
                print("Conexão com o banco fechada com segurança.")
            break

        case _:
            print("\n Opção inválida! Escolha um número de 1 a 6.")
