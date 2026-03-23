import os 
import json

clientes = []
    
def cadastrar_clientes():
    nome = input("Digite seu nome para continuar o cadastro :".title()).strip()
    cpf = input("Digite seu CPF para continuar seu cadastro :".title()).strip()
    telefone = input("Digite seu Telefone para continuar seu cadastro :".title()).strip()
    email = input("Digite seu Email para concluir seu cadastro :".title()).strip()
    
    clientes.append({
        "nome":nome,
        "cpf":cpf,
        "telefone":telefone,
        "email":email
    })
    print(f"\nCliente {nome} Cadastrado com Sucesso !!".title())
    
    caminho_pasta = os.path.join("clientes_cadastrados",nome)
    os.makedirs(caminho_pasta,exist_ok=True)
    
    caminho_arquivo = os.path.join(caminho_pasta, "cliente.json")
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(clientes,arquivo,indent=4, ensure_ascii=False)
        
def Listar_Clientes():
     if not clientes:
        print("Nenhum Cliente Cadastrado")
     else:
        print("\n--- Lista de Clientes ---")
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Email: {cliente['email']}")
            print("-" * 30)
            
def Deletar_Cadastro():
     cpf_deletar = input("Digite o CPF do cliente que voce deseja remover :".title())
     for cliente in clientes[:]:
        if cliente['cpf'] == cpf_deletar:
            clientes.remove(cliente)
            print("Cliente removido com sucesso !!")
            break
     else:
            print("Cliente não Encontrado")
            
def Atualizar_Cliente():
     cpf_busca= input("Digite seu CPF do cliente que deseja atualizar :")
     for cliente in clientes:
        if cliente['cpf'] == cpf_busca:
            print("Cliente Encontrado ")
            
            novo_nome = input("Novo Nome :")
            novo_telefone = input("Novo Telefone :")
            novo_email = input("Novo Email :")
            
            if novo_nome:
                cliente['nome']= novo_nome
                
            if novo_telefone:
                cliente['telefone'] = novo_telefone
                
            if novo_email:
                cliente['email'] = novo_email
            print("Cliente Atualizado Com Sucesso !!")
            break
     else:
            print("Cliente não Encontrado.")
            
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
  
while True:
    print("\n--- Sistema de Cadastro ao Cliente ---")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Deletar Cliente")
    print("4 - Atualizar Cliente")
    print("5 - Sair")
    
    
    opcao = input("Escolha uma opção :")
    
    if opcao == "1":
<<<<<<< HEAD
        
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
        
        caminho_arquivo = os.path.join(caminho_pasta,"Clientes.txt")
        
        with open(caminho_arquivo,"w") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"CPF: {cpf}\n")
            arquivo.write(f"Telefone: {telefone}\n")
            arquivo.write(f"Email: {email}\n")
        
        print("Cliente Cadastrado com Sucesso !!")
        
=======
      limpar_tela()
      cadastrar_clientes()
      input("\n Pressione Enter Para Continuar ")
>>>>>>> 8d3e6b4 (refactor: melhoria no codigo)
    elif opcao == "2":
        Listar_Clientes()
    elif opcao == "3":
        Deletar_Cadastro()
    elif opcao == "4":
        Atualizar_Cliente()
    elif opcao == "5":
        print()
        break
<<<<<<< HEAD
    else:
        print("Opção Invalida")
=======
>>>>>>> 8d3e6b4 (refactor: melhoria no codigo)
