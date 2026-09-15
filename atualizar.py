
def atualizar_cliente(banco_dados):

    if len(banco_dados) == 0:
        print("Nenhum cliente cadastrado.")
        return None

    id_cliente = int(input("Digite o ID do cliente: "))

    cliente_atualizado = None
    for cliente in banco_dados:
        if cliente["id"] == id_cliente:
            cliente_atualizado = cliente
            break

    nome = input("Nome: ").strip()
    idade= input("Idade: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    if nome == "" or idade == "" or telefone == "" or email == "":
        print("ERRO: Todos os campos são obrigatórios.")
        return None
    cliente_atualizado["nome"] = nome
    cliente_atualizado["idade"] = idade
    cliente_atualizado["telefone"] = telefone
    cliente_atualizado["email"] = email

    print("Cliente atualizado com sucesso!")
