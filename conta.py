class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print("Foi depositado R$:", quant)
            print("Saldo atual: ")
        else:
            print("Erro no depósito!")

    def consulta_saldo(self):
        return self.saldo
    
    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print("Saldo insuficiente!")
        else:
            self.saldo -= quant
            print("Foi sacado R$:  ", quant)
            print("Saldo atual:")