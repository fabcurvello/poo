nomes = ["Carlos", "Matheus", "Maria", "Jéssica", "Ana"]

try: #tentar
    numero = int(input("Informe um número para que seja exibido o nome correspondente na lista:"))
    print(f"Nome encontrado na posição {numero} da lista: {nomes[numero]}")

except IndexError as erro: #exceto
    print("Este número não corresponde a um item da lista de nomes...")
    print(erro)

except ValueError as erro:
    print("Você deve digitar um NÚMERO!")

else: # OPCIONAL -> Só é executado se não acontecer nenhum erro
    print("Execução concluída sem erros!!!")

finally: # OPCIONAL -> Será executado sempre, com ou sem erros
    print("Fim do programa!")

'''
OBS1: Pode usar simplesmente Exception, ao invés de especificar a classe de exceção
OBS2: Não é necessário utilizar o termo as erro para capturar a mensagem de erro. pode ser somente except:
OBS3: É possível agrupar tipos de exceções. except (ValueError, IndexError) as erro:
'''
