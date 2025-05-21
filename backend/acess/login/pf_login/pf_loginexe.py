import backend.modular_functionsinlore as mo
import backend.acess.login.pf_login.pf_loginfeatures as mofeatpf
# Solicitando o CPF do usuário:
def execute_cpf_pf_login():
    while True:
        pf_cpf_login = input('Digite o CPF seguindo o modelo (XXX.XXX.XXX-XX): ')
        pf_resultado_login = mofeatpf.exclusive_validate_cpf_login(cpf=pf_cpf_login)
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
pf_cpf_login = execute_cpf_pf_login()
pf_password_login = execute_password_pf_login()

mo.clean()
# Validação dos dados no banco de dados: