class ContaCorrente:
    def __init__(self, titular, agencia, conta, saldo):
        self._titular = titular
        self._agencia = agencia
        self._conta = conta
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
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @property
    def saldo(self):
        return self._saldo

    @titular.setter
    def titular(self, saldo):
        self._saldo = saldo

    def __str__(self):
        # Converte conta de int p str e formata c 7 dígitos (inclui zeros à esq se necessário)
        conta = str(self._conta).zfill(7)
        # Formato máscara 123456-7
        conta_formatada = "{}-{}".format(conta[:6], conta[6:])

        return f"---BANCO BIT---\n" \
               f"Titular: {self._titular}\n" \
               f"Agência: {self._agencia}\n" \
               f"Conta: {conta_formatada}\n" \
               f"Saldo: R$ {self._saldo:,.2f}\n"

    def calcularSaldo(self):
        return self._saldo



class ContaEspecial(ContaCorrente):
    def __init__(self, titular, agencia, conta, saldo, limite):
        super().__init__(titular, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def __str__(self):
        return f"{super().__str__()}Limite: R$ {self._limite:,.2f}\n"

    def calcularSaldo(self):
        return super().calcularSaldo() + self._limite


conta1 = ContaCorrente("Camilla Vieira", 3112, 9123456, 2500.00)
conta2 = ContaEspecial("Luana Barbosa", 5110, 812345, 450.00, 1000.00)

print(conta1)
print(conta2)

print(f"Conta 1 -> Saldo disponível: R$ {conta1.calcularSaldo():,.2f}")
print(f"Conta 2 -> Saldo disponível: R$ {conta2.calcularSaldo():,.2f}")