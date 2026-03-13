import os
from customer import Cliente

clientes = []

while True:
    print("\n--- Sistema de Cadastro ao Cliente ---")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Deletar Cliente")
    print("4 - Atualizar Cliente")
    print("5 - Sair")
    
    opcao = input("Escolha uma Opção :").strip()
    
    if opcao == "1":
        
        nome = input("Digite seu nome para continuar o cadastro:".title()).strip()
        cpf = input("Digite seu CPF para continuar seu cadastro :".title()).strip()
        telefone = input("Digite seu Telefone para continuar seu cadastro:".title()).strip()
        email = input("Digite seu Email para concluir seu cadastro:".title()).strip()
        
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF Inválido! Digite um CPF válido ")
            continue
        
        cliente = Cliente(nome,cpf,telefone,email)
        clientes.append(cliente)
        
        caminho_pasta = os.path.join("cliente_cadastrados",nome)
        os.makedirs(caminho_pasta, exist_ok= True)
        
        caminho_arquirvo = os.path.join(caminho_pasta,"Clientes.txt")
        
        with open(caminho_arquirvo,"w") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"CPF: {cpf}\n")
            arquivo.write(f"Telefone: {telefone}\n")
            arquivo.write(f"Email: {email}\n")
        
        print("Cliente Cadastrado com Sucesso !!")
        
    elif opcao == "2":
        
        if not clientes:
            print("Nenhum Cliente Cadastrado")
        else:
            print("\n--- Lista de Clientes ---")
            for cliente in clientes:
                cliente.saida_dados()
                
    elif opcao == "3":
        
        cpf_deletar = input("Digite o CPF do cliente que voce deseja remover: ")
        for cliente in clientes:
            if cliente.cpf == cpf_deletar:
               clientes.remove(cliente)
               print("Cliente removido com sucesso !!")
               break
        else:
            print("Cliente não Encontrado")
            
    elif opcao == "4":
        cpf_busca = input("Digite o CPF do cliente que deseja atualizar: ")
        
        for cliente in clientes:
            if cliente.cpf == cpf_busca:
                print("Cliente Encontrado")
                
                novo_nome = input("Novo Nome :")
                novo_telefone = input("Novo Telefone :")
                novo_email = input("Novo Email :")
                
                if novo_nome:
                    cliente.nome = novo_nome
                if novo_telefone:
                    cliente.telefone = novo_telefone
                if novo_email:
                    cliente.email = novo_email
                print("Cliente Atualizado Com Sucesso !!")
                break
        else:
            print("Cliente não Encontrado.") 
    elif opcao == "5":
        print("Sistema Encerrado")
        break
    else:
        print("Opção Invalida")