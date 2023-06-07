from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from banco import Banco
from enumtipoconta import TipoConta

b1 = Banco('Itau')
cliente1 = b1.criar_conta_corrente('Jhonatan', 32, '137.856.407-30')
# cliente1.listar_contas()

cliente2 = b1.criar_conta_poupanca('Brizzida', 32, '333.415.988-47')
for i in b1._lista_clientes:
    print(i)

print(b1.sacar(cliente1, TipoConta.CORRENTE, 100))
