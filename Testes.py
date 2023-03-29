# testes com comentários para agilizar o entendimento dos resultados

from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# teste completo para Conta Corrente

contacorrenteA = ContaCorrente(12345, 2543.50, 10000.00)
contacorrenteA.id
contacorrenteA.saldo
contacorrenteA.limite
contacorrenteA.depositar(1500.90) 
contacorrenteA.saldo # o saldo agora tem que ser R$4044.40
contacorrenteA.sacar(2000) # é possivel realizar sem a utilização do limite
contacorrenteA.saldo # o saldo agora tem que ser R$2044.40
contacorrenteA.sacar(9000.00) # é possivel sacar apenas com a utilização do limite
contacorrenteA.limite # o limite agora tem que ser R$3044.40
contacorrenteA.saldo #o saldo agora tem que ser R$0.00
contacorrenteA.sacar(5000.00) #o saldo não é suficiente, portanto a ação será negada

print("\n#################################################################################\n")

#teste completo para Conta Poupanca

contapoupancaB = ContaPoupanca(56789, 14590.98, 0.5) # 0.5% de rendimento ao mes 
contapoupancaB.id
contapoupancaB.saldo
contapoupancaB.verificar_rendimento_ao_ano() # o rendimento anual agora é R$899,94
contapoupancaB.depositar(2700.30)
contapoupancaB.saldo # o saldo agora é R$17291,28
contapoupancaB.verificar_rendimento_ao_ano() # o rendimento anual agora é R$1.066,49
contapoupancaB.sacar(10000.00)
contapoupancaB.saldo # o saldo agora é R$7291,28
contapoupancaB.verificar_rendimento_ao_ano() # o rendimento anual agora é R$449,71
contapoupancaB.sacar(15000.00) # o saldo não é suficiente, portanto a ação será negada
