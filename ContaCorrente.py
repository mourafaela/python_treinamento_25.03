from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta = int, saldo = float, limite = float):
        super().__init__(id_conta, saldo)
        self._limite = float = limite

    @property #getter limite
    def limite(self):
        print("Limite atual: " + ("R$%.2f" %self._limite))
        print(".........................................................................................................")

    @limite.setter #setter limite
    def limite(self, valor_limite):
        self._limite = valor_limite

    def depositar(self, valor_deposito = float):
        self._saldo = self._saldo + valor_deposito
        print("Você efetuou um deposito no valor de " + ("R$%.2f" %valor_deposito))
        print(".........................................................................................................")

    #aqui não seria possivel aplicar o principio Single Responsibility pois para validar o saldo, é necessário saber o valor do saque
    def sacar(self,valor_saque = float): 
        try:
            if self._saldo - valor_saque < 0:
                if (self._saldo+self._limite) - valor_saque < 0:
                    raise ValueError
                else:
                    self._limite = (self._saldo + self._limite) - valor_saque
                    self._saldo = 0.00
                    print(f"Você efetuou um saque no valor de " + ("R$%.2f" %valor_saque))
                    print("Saldo atual: " + ("R$%.2f" %self._saldo))
                    print("Limite atual: " + ("R$%.2f" %self._limite))
                    print(".........................................................................................................")

            else:
                print(f"Você efetuou um saque no valor de " + ("R$%.2f" %valor_saque))
                self._saldo -= valor_saque
                print("Saldo atual: " + ("R$%.2f" %self._saldo))
                print("Limite atual: " + ("R$%.2f" %self._limite))
                print(".........................................................................................................")
        
        except ValueError:
            print("Saque negado! Seu limite não é suficiente. Tente novamente.")
            print(".........................................................................................................")