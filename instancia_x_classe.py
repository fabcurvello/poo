class TaxiRio:

    #Atributo de classe
    cor = "Amarelo"

    #O método construtor possui atributos de instância
    def __init__(self, fabricante, modelo, ano):
        self._fabricante = fabricante
        self._modelo = modelo
        self._ano = ano


    # Método de instância
    def exibir_fabricante_modelo(self):
        print(f"Você está aguardando um Táxi {self._fabricante} {self._modelo}.")


    #Método de classe
    @classmethod
    def exibir_cor(cls):
        print(f"A cor padrão dos táxis na capital do Rio de Janeiro é {cls.cor}.")


    #Método estático
    @staticmethod
    def exibir_horario_de_funcionamento():
        print("A Táxi Rio está à sua disposição 24h por dia.")


    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def fabricante(self, ano):
        self._ano = ano


    def __str__(self):
        return f"Características do Taxi Selecionado:\n" \
               f"-- Fabricante: {self._fabricante}\n" \
               f"-- Modelo: {self._modelo}\n" \
               f"-- Ano: {self._ano}\n" \
               f"-- Cor: {self.cor}\n"



taxi1 = TaxiRio("Toyota", "Corolla", 2023)
taxi2 = TaxiRio("Honda", "Civic", 2022)
taxi3 = TaxiRio("Chevrolet", "Cruze", 2021)

print(taxi1)
# TaxiRio.cor = "Azul" #Muda a cor de todos os objetos a partir deste ponto
print(taxi2)
print(taxi3)

# Chamadas de método de instância
taxi1.exibir_fabricante_modelo()
taxi2.exibir_fabricante_modelo()
taxi3.exibir_fabricante_modelo()

# Chamada do método de classe através de instância de objeto
taxi1.exibir_cor()

# Chamada do método de classe sem utilizar instância alguma
TaxiRio.exibir_cor()


# Chamadas de método estático
TaxiRio.exibir_horario_de_funcionamento()
taxi1.exibir_horario_de_funcionamento()
