from banco import Banco

class SistemaBancario:
    def __init__(self):
        self.banco = Banco()

    def menu_principal(self):
        while True:
            print("\n1. Cadastrar cliente")
            print("2. Login")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu_cadastro()
            elif opcao == '2':
                self.menu_login()
            elif opcao == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def menu_cadastro(self):
        nome = input("Nome: ")
        conta = input("Número da conta: ")
        senha = input("Senha: ")
        saldo = float(input("Saldo inicial: "))

        if self.banco.cadastrar_cliente(nome, conta, senha, saldo):
            print("Cliente cadastrado com sucesso!")
        else:
            print("Erro: conta já existe!")

    def menu_login(self):
        conta = input("Número da conta: ")
        senha = input("Senha: ")

        cliente = self.banco.login(conta, senha)

        if cliente:
            print(f"Bem-vindo(a), {cliente.nome}!")
            self.menu_operacoes(cliente)
        else:
            print("Conta ou senha incorretas!")

    def menu_operacoes(self, cliente):
        while True:
            print("\n1. Saldo")
            print("2. Saque")
            print("3. Depósito")
            print("4. Transferência")
            print("5. Sair")
            op = input("Escolha: ")

            if op == '1':
                print(f"Saldo atual: R${cliente.saldo:.2f}")

            elif op == '2':
                valor = float(input("Valor do saque: "))
                if cliente.saque(valor):
                    print("Saque realizado!")
                else:
                    print("Saldo insuficiente!")

            elif op == '3':
                valor = float(input("Valor do depósito: "))
                cliente.deposito(valor)
                print("Depósito realizado!")

            elif op == '4':
                destino = input("Conta destino: ")
                valor = float(input("Valor: "))
                if self.banco.transferencia(cliente, destino, valor):
                    print("Transferência feita!")
                else:
                    print("Erro na transferência.")

            elif op == '5':
                break
            else:
                print("Opção inválida!")
                