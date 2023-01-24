def dividir (n1, n2):
    try:
        print(f"{n1} / {n2} = {n1 / n2}")
    except ZeroDivisionError as erro:
        #print(f"Erro na função dividir: {erro}")
        raise


try:
    dividir(10, 0)
except Exception as erro:
    print(f"DESENVOLVEDOR: Erro encontrado -> {erro}")

'''
raise lança a exceção! Permite passar adiante o erro para ser tratado posteriormente.
Isso é útil quando a chamada vem de métodos diferentes, de herança, ou de um sistema que acessa um banco de dados...
'''