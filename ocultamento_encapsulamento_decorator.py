class ContaCorrente:
    def __init__(self, titular, agencia, numero_conta, saldo):
        self._titular = titular
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def numero_conta(self):
        self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self._numero_conta = numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo = self._saldo + valor
        print(f"Novo saldo: R$ {self._saldo}")

    def sacar(self, valor):
        if (valor <= self._saldo):
            self._saldo = self._saldo - valor
            print(f"Novo saldo: R$ {self._saldo}")
        else:
            print("Não é possível sacar. Saldo indisponível para esta operação.")


conta1 = ContaCorrente("Fabricio", "0101", "7575-5", 1000)
print(f"Titular: {conta1.titular}, Saldo: R${conta1.saldo}")

conta1.titular = "Fabricio Curvello"
print(f"Titular: {conta1.titular}, Saldo: R${conta1.saldo}")

conta1.depositar(500)
conta1.sacar(2000)

