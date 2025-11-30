from cliente import Cliente

class Banco:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self, nome, numero_conta, senha, saldo):
        if numero_conta in self.clientes:
            return False

        self.clientes[numero_conta] = Cliente(nome, numero_conta, senha, saldo)
        return True

    def login(self, numero_conta, senha):
        cliente = self.clientes.get(numero_conta)
        if cliente and cliente.senha == senha:
            return cliente
        return None

    def transferencia(self, origem, destino_conta, valor):
        destino = self.clientes.get(destino_conta)
        if not destino:
            return False

        if not origem.saque(valor):
            return False

        destino.deposito(valor)
        return True
    