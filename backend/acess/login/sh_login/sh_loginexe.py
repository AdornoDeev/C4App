import backend.modular_functionsinlore as mo

# Solicitação de id de usuário:
def execute_id_sh_login():
    while True:
        sh_identf_login = input("Digite o (ID) de usuário cadastrado: ").strip()
        sh_identf_login = mo.validate_sh_id(sh_identf_login)
        if sh_identf_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return sh_identf_login
        print('\033[31mApenas digitos númericos inteiros são válidos para (ID)s.\033[m')

# Solicitando a password do usuário:
def execute_password_sh_login():
    while True:
        sh_password_login = mo.validate_password(input('Digite a senha atribuida ao usuário: '))
        if sh_password_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return sh_password_login

# Limpeza de terminal.
mo.clean()

# Execução de funções:
sh_identf_login = execute_id_sh_login()
sh_password_login = execute_password_sh_login()

# Validação dos dados no banco de dados:
