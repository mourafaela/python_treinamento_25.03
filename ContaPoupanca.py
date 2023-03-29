# OBSERVAÇÃO -> Foram consideradas as mesmas regras da Poupança: taxa de rendimento dada AO MÊS e cálculo do rendimento como JUROS COMPOSTOS 

from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, id_conta = int, saldo = float, taxa_de_rendimento = float):
        super().__init__(id_conta, saldo)
        self._taxa_de_rendimento = float = taxa_de_rendimento #dada em porcentagem sem o sinal %

    #getter taxa 
    @property
    def taxaDeRendimentoPoupanca(self):
        print(f"Taxa de rendimento ao mês: {self._taxa_de_rendimento}")
        print(".........................................................................................................")

    #setter taxa
    @taxaDeRendimentoPoupanca.setter
    def limite(self, taxaDeRendimentoPoupanca):
        self._taxa_rendimento_poupanca = taxaDeRendimentoPoupanca

    def depositar(self, valor_deposito):
        self._saldo = self._saldo + valor_deposito
        print("Você efetuou um deposito no valor de " + ("R$%.2f" %valor_deposito))
        print(".........................................................................................................")

    def sacar(self,valor_saque):
        try:
            if self._saldo - valor_saque < 0:
                raise ValueError
            else:
                self._saldo -= valor_saque
                print(f"Você efetuou um saque no valor de " + ("R$%.2f" %valor_saque))
                print("Saldo atual: " + ("R$%.2f" %self._saldo))
                print(".........................................................................................................")

        except ValueError:
            print("Saldo Insuficiente! Tente sacar um valor menor.")
            print(".........................................................................................................")

    def verificar_rendimento_ao_ano(self):
        saldo_apos_rendimento = self._saldo * ((1 + self._taxa_de_rendimento/100) ** (12))
        rendimento = saldo_apos_rendimento - self._saldo
        print("Com o saldo de " + ("R$%.2f" %self._saldo) + ", o rendimento anual será de: " + ("R$%.2f" % rendimento))
        print(".........................................................................................................")