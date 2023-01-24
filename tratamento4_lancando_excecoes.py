def dividir (n1, n2):
    if (n2 == 0):
        raise ValueError("Não é possível dividir por zero.")

    print(f"{n1} / {n2} = {n1 / n2}")



try:
    dividir(10, 0)
except ValueError as erro:
    print(f"DESENVOLVEDOR: Erro encontrado -> {erro}")

'''
Neste exemplo é possível lançar o tipo de erro para ser capturado adiante.

raise lança a exceção! Permite passar adiante o erro para ser tratado posteriormente.
Isso é útil quando a chamada vem de métodos diferentes, de herança, ou de um sistema que acessa um banco de dados...
'''