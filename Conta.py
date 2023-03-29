# foram consideradas somente 2 casas decimais nos cálculos pois para o exercício a precisão não é muito importante

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, id_conta = int , saldo = float):
        self._id_conta = id_conta
        self._saldo = saldo

    @abstractmethod
    def depositar(self):
        pass
    
    @abstractmethod
    def sacar(self):
        pass

    @property #getter id
    def id(self):
        print(f"Id da conta: {self._id_conta}")
        print(".........................................................................................................")
    
    @id.setter #setter id
    def id(self, id_conta):
        self._id_conta = id_conta

    @property #getter saldo
    def saldo(self):
        print("Saldo atual: " + ("R$%.2f" %self._saldo))
        print(".........................................................................................................")
    
    @saldo.setter #setter saldo
    def saldo(self, saldo_conta):
        self._saldo_conta = saldo_conta
