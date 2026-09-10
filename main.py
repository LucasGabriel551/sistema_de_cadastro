import os

import cadastro

banco_dados = []

def menu():
    while True:
        print("1 - Cadastro cliente")
        print("2 - Listar clientes")
        print("3 - atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Sair do sistema")
        print("-" * 50)

        opcao = input("escolha uma opção: ")

        os.system("cls")
        if opcao == "1":
            print("Cadastro")
            cadastro.cadastro_cliente(banco_dados)
        elif opcao == "2":
            print(banco_dados)
        elif opcao == "3":
            print("Atualizar")
        elif opcao == "4":
            print("Excluir")
        elif opcao == "5":
        
            print("Sistema encerrado.")
            break
        else:
            print("ERRO: Opção inválida.")

menu()
