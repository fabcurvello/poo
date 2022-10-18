class ContaCorrente:
    def __init__(self, titular, agencia, numero_conta, saldo):
        self._titular = titular
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def get_agencia(self):
        return self._agencia

    def set_agencia(self, agencia):
        self._agencia = agencia

    def get_numero_conta(self):
        self._numero_conta

    def set_numero_conta(self, numero_conta):
        self._numero_conta = numero_conta

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
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
print(f"Titular: {conta1.get_titular()}, Saldo: R${conta1.get_saldo()}")

conta1.depositar(500)
conta1.sacar(2000)