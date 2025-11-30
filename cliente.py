class Cliente:
    def __init__(self, nome, numero_conta, senha, saldo_inicial=0.0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.senha = senha
        self.saldo = saldo_inicial

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True   
    
    