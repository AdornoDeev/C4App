import backend.modular_functionsinlore as mo

# Solicitação do nome do usuário:
nome = input("Digite seu nome: ").title().replace(' ','')

# Solicitação de senha:
senha = None
while not senha:
    senha = mo.validate_password(input('Digite a senha que deseja cadastrar: '))

# Solicitação de E-mail.
while True:
    mail = input('Digite seu e-mail para cadastro: ')
    resultado = mo.validate_mailsyntaxe(mail)
    if resultado:
        print('\033[36mE-mail válido!\033[m')
        mo.clean()
        break
    else:
        print('\033[31mE-mail inválido!\033[m')
        print("""\033[31mRegras de digitação:
É proibído ponto no inicio, final e antes do @;
É proibido antes do arroba não haver um identificador;
É proibido após o arroba não haver um provedor;
É proibído após o provedor não haver um domínio;\033[m
\033[36mModelo padrão:
(identificafor/nome)@(provedor)(domínios/subdomínios)\033[m""")

# Solicitação de CPF:
while True:
    cpf = input('Digite o CPF a ser cadastrado seguindo o modelo (XXX.XXX.XXX-XX): ')
    resultado = mo.validate_cpf(cpf=cpf)
    if resultado:
        print('\033[36mCPF Cadastrado com sucesso!\033[m')
        break
    else:
        print('\033[31mCPF inválido!\033[m')
        print("""\033[31mRegras de digitação:
O CPF deve seguir o modelo: XXX.XXX.XXX-XX;
O CPF deve possuir 11 dígitos;
O CPF deve possuir digitos verificadores válidos.\033[m""")
        
# Instanciar um usuáriopf:
user = mo.create_pfuser(nome,senha,mail,cpf)
print(user)

# Enviar usuário para o banco de dados: