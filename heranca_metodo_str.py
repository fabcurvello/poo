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

    def __str__(self):
        return f"{self._matricula}: \nNome: {self._nome} \nE-mail: {self.email}"


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

    def __str__(self):
        return f"\nDADOS DO(A) ALUNO(A) {super().__str__()} \nCurso: {self._curso} \nTurma: {self._turma}"


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

    def __str__(self):
        return f"\nDADOS DO(A) PROFESSOR(A) {super().__str__()} \nFormação: {self.formacao}"



alu1 = Aluno(301, "Carla Moreira", "carla@email.com", "Inglês", "N102")
prof1 = Professor(27, "Maria Cristina", "cristina@email.com", "Letras")

print(alu1)
print(prof1)