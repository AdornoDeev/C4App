import backend.modular_functionsinlore as mo

# Solicitação de id de usuário:
def execute_id_sh_login():
    while True:
        sh_identf_login = input("Digite o (ID) de usuário cadastrado: ").strip()
        sh_resultado_login = mo.validate_sh_id(sh_identf_login)
        if sh_resultado_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return sh_identf_login
        print('\033[31mApenas digitos numéricos inteiros são válidos para (ID)s.\033[m')

# Solicitando a password do usuário:
def execute_password_sh_login():
    while True:
        sh_password_login = mo.validate_password(input('Digite a senha atribuida ao usuário: '))
        if sh_password_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return sh_password_login


# Execução de funções:
def log_in_sh_user():
    sh_identf_login = execute_id_sh_login()
    sh_password_login = execute_password_sh_login()
    return [sh_identf_login,sh_password_login]