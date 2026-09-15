
def listar_clientes(banco_dados):

    if len(banco_dados) == 0:
        print("Nenhum cliente cadastrado.")
        return None

    print(
          f"{'ID':<5}"
          f"{'NOME':<20}"
          f"{'IDADE':<10}"
          f"{'TEL.:':<15}"
          f"{'E-MAIL'}"
    )
    print("-" * 60)

    for cliente in banco_dados:
        print(f"{cliente['id']:<5}"
              f"{cliente['nome']:<20}"
              f"{cliente['idade']:<10}"
              f"{cliente['telefone']:<15}"
              f"{cliente['email']}"
        )
    print("-" * 60)
    print()
