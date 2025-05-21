import backend.modular_functionsinlore as mo

# Solicitação de id de usuário:
while True:
    sh_identf_login = input("Digite o (ID) de usuário cadastrado: ").strip()
    sh_identf_login = mo.validate_sh_id(sh_identf_login)
    if sh_identf_login:
        break
    print('\033[31mApenas digitos númericos inteiros são válidos para (ID)s.\033[m')

# Solicitando a password do usuário:
while True:
    sh_password_login = mo.validate_password(input('Digite a senha atribuida ao usuário: '))
    if sh_password_login:
        print('\033[36mFormato validado com sucesso!\033[m')
        break

# Limpeza de terminal.
mo.clean()

# Validação dos dados no banco de dados:
