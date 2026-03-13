class Cliente():
    def __init__(self,nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
    
    def saida_dados(self):
        print(
            f"\n --- Dados do Cliente --- \n"
            f"Nome : {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}\n"
)