

""""
 ********************** DIO - BOOTCAMP **********************
 ********** DESAFIO 02 - BANCO - PYTHON DEVELOPER ***********
"""


LIMITE_SAQUE = 500
AGENCIA = '0001'
numero_saques = 3
extrato = []
saldo = 1500
usuarios = []
contas = []

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            print('Usuario existente')
            
            return usuario

def criar_usuario(usuarios):
    print("================ Cadastro de Usuarios ================")
    cpf = input('Informe o seu CPF (Apenas numeros): ')
    
    if filtrar_usuario(cpf,usuarios):
        return
    
    nome = input('Informe o seu nome: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o seu endecero (Logradouro, Nro - Bairro - Cidade/UF): ')

    return ({'CPF':cpf, 'Nome':nome, 'Data de Nascimento':data_nascimento, 'Endereco':endereco})


def criar_conta(usuarios, agencia, numero_conta):
    print("================ Cadastro de Contas ================")
    cpf = input('Insira o CPF do titular: ')
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            print('Contra criada com sucesso')
            return {'CPF':cpf, 'Agencia':agencia, 'Nr. Conta':numero_conta}

        
def listar_contas(contas):
    print("================ Contas ================")
    for conta in contas:
        
        print(f'Numero da Conta: {conta["Nr. Conta"]}', end="\n")
        print(f'Numero da Agencia: {conta["Agencia"]}', end="\n")
        print(f'CPF do Titular: {conta["CPF"]}', end="\n")

        print("\n")
    print("\n")
    print("=========================================")  


def listar_usarios(usuarios):
    print("================ Usuarios ================")
    for usuario in usuarios:
        
        print(f'Nome Titular: {usuario["Nome"]}', end="\n")
        print(f'CPF Titular: {usuario["CPF"]}', end="\n")
        print(f'Data Nascimento: {usuario["Data de Nascimento"]}', end="\n")
        print(f'Endereco: {usuario["Endereco"]}', end="\n")


        print("\n")
    print("\n")
    print("=========================================")  


        
def sacar(saldo, valor, extrato, limite_saque = LIMITE_SAQUE, numero_saques = numero_saques, /):
    if saldo < valor:
        print('Saldo insuficiente.')
    
    elif valor > LIMITE_SAQUE:
        print('Saque em um valor maior que o limite diario.')
    
    elif numero_saques <= 0:
        print('Numero de saques atingido.')

    elif valor < 0:
        print('Informar valor valido.')    
    
    elif valor > 0:
        extrato.append(f'Saque: R$ {valor:.2f}')
        saldo -= valor
        numero_saques -= 1
        print('Saque realizado com sucesso.', end='/n')

    else:
        print("Erro.")
    
    
    return saldo, extrato, numero_saques


def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito: R$ {valor:.2f}')
        print('Deposito realizado com sucesso', end='/n')
    
    else:
        print('Insira um valor valido.')

    return saldo, extrato

        
def emitir_extrato(saldo, /, * ,extrato):
    print("================ Extrato ================")

    for i in range(0,len(extrato)):
        print(f'{i+1}: {extrato[i]}', end="\n")

    print("\n")
    print(f'Saldo atual em conta R$ {saldo}')
    print("=========================================")


while True:
    print(f""""
================ Extrato ================
[1] - Sacar
[2] - Depositar
[3] - Extrato
[4] - Criar Usuario
[5] - Criar Conta
[6] - Listar Contas
[7] - Listar Usuarios
    
[s] - Sair
=========================================

Opção:  
    """)

    opcao = input()

    if opcao == "1":
        valor = int(input('Insira o valor que deseja sacar: '))
        saldo, extrato, numero_saques = sacar(saldo, valor, extrato, LIMITE_SAQUE, numero_saques)

    elif opcao == '2':
        valor = int(input('Insira o valor que deseja depositar: '))
        saldo, extrato = depositar(saldo, valor)

    elif opcao == "3":
        emitir_extrato(saldo, extrato = extrato)

    elif opcao == '4':
        usuario = criar_usuario(usuarios)

        if usuario:
            usuarios.append(usuario)

    elif opcao == '5':
        numero_conta = len(contas)+1

        conta = criar_conta(usuarios, agencia = AGENCIA, numero_conta = numero_conta)

        if conta:
            contas.append(conta)

        else:
            print('Usuario não existente')


    elif opcao == '6':
        listar_contas(contas)

    elif opcao == '7':
        listar_usarios(usuarios)

    elif opcao == 's':
        break


