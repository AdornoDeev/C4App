import regex
import backend.modular_functionsinlore as mo
# Validação de sintaxe de CPF.
def exclusive_validate_cpf_login(cpf):
    pattern = regex.compile(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}')
    resultado = regex.fullmatch(pattern,cpf)
    if not resultado:
        return False
    else:
        return True

# Solicitando o CPF do usuário:
def execute_cpf_pf_login():
    while True:
        pf_cpf_login = input('Digite o CPF seguindo o modelo (XXX.XXX.XXX-XX): ')
        pf_resultado_login = exclusive_validate_cpf_login(cpf=pf_cpf_login)
        if pf_resultado_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pf_cpf_login
        else:
            print('\033[31mCPF inválido!\033[m')
            print("""\033[31mRegras de digitação:
- O CPF deve seguir o modelo: XXX.XXX.XXX-XX;
- O CPF deve possuir 11 dígitos.\033[m""")

# Solicitando a password do usuário:
def execute_password_pf_login():
    while True:
        pf_password_login = mo.validate_password(input('Digite a senha atribuida ao CPF: '))
        if pf_password_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pf_password_login

# Excução das funções:
def log_in_pf_user():
    pf_cpf_login = execute_cpf_pf_login()
    pf_password_login = execute_password_pf_login()
    return [pf_cpf_login,pf_password_login]

