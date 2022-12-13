class ContaCorrente:
    def __init__(self, titular, agencia, saldo):
        self._titular = titular
        self._agencia = agencia
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
    def saldo(self):
        return self._saldo

    @titular.setter
    def titular(self, saldo):
        self._saldo = saldo


class ContaEspecial(ContaCorrente):
    def __init__(self, titular, agencia, saldo, limite):
        super().__init__(titular, agencia, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

