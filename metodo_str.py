class Usuario:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email


    def __str__(self):
        return f"DADOS DO(A) USUÁRIO(A) - Nome: {self._nome}, E-mail: {self._email}"

user1 = Usuario("Jorge", "jorge@email.com")
user2 = Usuario("Fátima", "fatima@email.com")

print(user1)
print(user2)