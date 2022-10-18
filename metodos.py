class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def efetuarLogin(self):
        if ( self.email == "user@email.com" and self.senha == "senha123"):
            print(f"e-mail: {self.email} --> Usuário logado com sucesso!")
        else:
            print(f"e-mail: {self.email} --> Não foi possível efetuar login.")


user1 = Usuario("user@email.com", "senha123")
user2 = Usuario("rivonelson@email.com", "carro")

user1.efetuarLogin()
user2.efetuarLogin()