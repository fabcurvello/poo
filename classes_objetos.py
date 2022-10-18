class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

aluno1 = Aluno(501, "Ana Carolina")
aluno2 = Aluno(502, "Carlos José")

print(f"Matrícula: {aluno1.matricula} - Nome: {aluno1.nome}")
print(f"Matrícula: {aluno2.matricula} - Nome: {aluno2.nome}")


class Carro:
    def __init__(self, fabricante, modelo, cor, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


carro1 = Carro("Fiat", "Mobi", "Preto", 2022)
carro2 = Carro("Volkswagen", "Up", "Branco", 2020)

print(f"\nCARRO 1\nFabricante: {carro1.fabricante}\nModelo: {carro1.modelo}\nCor: {carro1.cor}\nAno: {carro1.ano}\n")
print(f"\nCARRO 2\nFabricante: {carro2.fabricante}\nModelo: {carro2.modelo}\nCor: {carro2.cor}\nAno: {carro2.ano}\n")
