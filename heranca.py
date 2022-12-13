class Pessoa:
    def __init__(self, matricula, nome, email):
        self._matricula = matricula
        self._nome = nome
        self._email = email

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


    def _fazer_login(self):
        print("-- FAÇA O LOGIN PARA ENTRAR NO SISTEMA --")
        email = input("E-mail: ")
        if(email == self._email):
            print(f"Olá {self._nome}! Login realizado com sucesso!")
            return True
        else:
            print("Falha na tentativa de fazer login...")
            return False

# Aluno é subclasse de Pessoa
class Aluno(Pessoa):
    def __init__(self, matricula, nome, email, curso, turma):
        super().__init__(matricula, nome, email)
        self._curso = curso
        self._turma = turma

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    @property
    def turma(self):
        return self._turma

    @turma.setter
    def turma(self, turma):
        self._turma = turma


# Professor é subclasse de Pessoa
class Professor(Pessoa):
    def __init__(self, matricula, nome, email, formacao):
        super().__init__(matricula, nome, email)
        self._formacao = formacao

    @property
    def formacao(self):
        return self._formacao

    @formacao.setter
    def formacao(self, formacao):
        self._formacao = formacao



alu1 = Aluno(301, "Carla Moreira", "carla@email.com", "Inglês", "N102")
prof1 = Professor(27, "Maria Cristina", "cristina@email.com", "Letras")

print(f"\nDADOS DO(A) ALUNO(A) {alu1.matricula}:")
print(f"Nome: {alu1.nome}")
print(f"E-mail: {alu1.email}")
print(f"Curso: {alu1.curso}")
print(f"Turma: {alu1.turma}")

print(f"\nDADOS DO(A) PROFESSOR(A) {prof1.matricula}:")
print(f"Nome: {prof1.nome}")
print(f"E-mail: {prof1.email}")
print(f"Formação: {prof1.formacao}")



'''
Experimento para identificar um usuário cadastrado
'''

#Dicionário onde a chave é a matrícula e o valor é o objeto inteiro
usuarios = {alu1.matricula : alu1, prof1.matricula : prof1}
def identificar_usuario(dic_usuarios):
    print("\n-- IDENTIFICAÇÃO DO USUÁRIO --")
    matricula = int(input("Informe o número de sua matrícula:"))
    if (matricula in dic_usuarios):
        usuario_identificado = dic_usuarios[matricula]
        print(f"Usuário localizado: {usuario_identificado.nome}")
        #pelo usuário identificado, chamar método fazer_login() que está na classe Pessoa. Este método retorna um boolean
        logado = usuario_identificado._fazer_login()
        print(logado)
    else:
        print("Matrícula não existe!")



identificar_usuario(usuarios)