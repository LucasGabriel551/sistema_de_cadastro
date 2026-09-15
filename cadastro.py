
def cadastro_cliente(banco_dados):
    nome = input("Nome: ").strip()
    idade= input("Idade: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    if nome == "" or idade == "" or telefone == "" or email == "":
        print("ERRO: Todos os campos são obrigatórios.")
        return None

    cliente = {
        "id": len(banco_dados) + 1,
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email
    }

    banco_dados.append(cliente)
