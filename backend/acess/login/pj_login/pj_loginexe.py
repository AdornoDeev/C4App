import backend.modular_functionsinlore as mo
import backend.acess.login.pj_login.pj_loginfeatures as mofeatpj

# Solicitação de CNPJ:
def execute_cnpj_pj_login():
    while True:
        pj_cnpj_login = input('Digite os números do CNPJ seguindo modelo (XX.XXX.XXX/XXXX-XX): ')
        pj_resultado_login = mofeatpj.exclusive_validate_cnpj_login(pj_cnpj_login)
        if pj_resultado_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pj_cnpj_login
        else:
            print('\033[31mCNPJ Inválido!\033[m')
            print("""\033[31mRegras de digitação:
- É proibido não seguir o modelo de digitação: XX.XXX.XXX/XXXX-XX com todos os pontos, barra e traço.
- O CNPJ deve possuir 14 dígitos.\033[m""")

# Solicitando a password do usuário:
def execute_password_pj_login():
    while True:
        pf_password_login = mo.validate_password(input('Digite a senha atribuida ao CNPJ: '))
        if pf_password_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pf_password_login

# Limpeza de terminal.
mo.clean()

# Execução de funções:
pj_cnpj_login = execute_cnpj_pj_login()
pf_password_login = execute_password_pj_login()

# Validação dos dados no banco de dados:
