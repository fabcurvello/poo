'''
Relação de Composição -> A classe principal (t odo)
cria uma instância da outra classe (parte),
que se torna parte dela. Quando a classe principal for destruída,
sua instância da outra classe também será.
'''

class Usuario: #t odo
    def __init__(self, nome):
        self.nome = nome
        self.telefones = []

    def cadastrar_telefone(self, ddd, numero, categorizacao):
        telefone = Telefone(ddd, numero, categorizacao)
        self.telefones.append(telefone)

    def listar_telefones(self):
        if (len(self.telefones) != 0):
            print(f"\nUsuário(a) {self.nome} - Relação de Telefones:")
            for telefone in self.telefones:
                print(telefone)
        else:
            print(f"\nUsuário(a) {self.nome} - Não possui telefone cadastrado.")

    #def __del__(self):
    #    print(f"Usuário(a) {self.nome} removido!")


class Telefone: #parte
    def __init__(self, ddd, numero, categorizacao):
        self.ddd = ddd
        self.numero = numero
        self.categorizacao = categorizacao

    def __str__(self):
        return f"- Telefone {self.categorizacao}: ({self.ddd}) {self.numero}"

    #def __del__(self):
    #    print(f"Telefone {self.categorizacao} removido!")


usuario1 = Usuario("Matheus")
usuario1.cadastrar_telefone(21, 987654321, "celular")
usuario1.cadastrar_telefone(21, 32324545, "comercial")
usuario1.cadastrar_telefone(21, 35359898, "residencial")

usuario2 = Usuario("Maria Alice")
usuario2.cadastrar_telefone(21, 92221717, "celular")

usuario3 = Usuario("Jéssica")

usuario1.listar_telefones()
usuario2.listar_telefones()
usuario3.listar_telefones()




