class Usuario:

    #Método construtor
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrarUsuario(self):
        print("CADASTRO DE USUÁRIO")
        nome = input("Informe o nome do usuário:")
        email = input("Informe o e-mail")
        senha = input("Informe a senha")

        #self.usuario = Usuario(nome, email, senha)
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        print(f"Usuário {self.nome} cadastrado com sucesso")
        #return self.usuario

    def efetuarLogin(self):
        print("EFETUAR LOGIN")
        email = input("Informe o email para realizar login")
        senha = input("Informe a senha para realizar login")
        if ( email == usuario.email and senha == usuario.senha ):
            print(f"Usuário {usuario.nome} logado com sucesso!!!")
        else:
            print("Não foi possível efetuar login.")

    def simularTela(self):
        print("---SISTEMA XPTO---")
        print("\nRealize o cadastro de usuário!\n")
        self.cadastrarUsuario()
        print("\nAgora efetue login para poder entrar no Sistema XPTO\n")
        self.efetuarLogin()


usuario = Usuario("Fulano", "fulano@email.com", "fulano123")
usuario.simularTela()