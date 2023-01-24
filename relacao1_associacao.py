'''
Relação de Associação -> É uma das relações mais comuns entre dois objetos.
Acontece quando um objeto “utiliza” outro, porém, sem que eles dependam um do outro.

Ex: Objeto trem x objeto trilho, Objeto carro x objeto rua, Objeto aluno x Objeto Curso.
'''

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.exercicio = None

    def estudar(self):
        print(f"{self.nome} está estudando Python")


class Academia:
    def __init__(self, nome_academia, atividade):
        self.nome_academia = nome_academia
        self.atividade = atividade

    def praticar_atividade(self):
        return f"está fazendo {self.atividade} na academia {self.nome_academia}"

pessoa1 = Pessoa("Rafael")
pessoa2 = Pessoa("Juliana")

academia1 = Academia("Fit Total", "Musculação")
academia2 = Academia("Gym Fight", "Judô")

#Relação de Associação: A pessoa pratica exercício na academia:
pessoa1.exercicio = academia1
pessoa2.exercicio = academia2

#Pelo atributo exercicio (do obj pessoa) é possível acionar um método de Academia
print(f"{pessoa1.nome} {pessoa1.exercicio.praticar_atividade()}")
print(f"{pessoa2.nome} {pessoa2.exercicio.praticar_atividade()}")


