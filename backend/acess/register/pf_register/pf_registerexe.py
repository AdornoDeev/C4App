import backend.modular_functionsinlore as mo
import backend.databases.pf_db.pf_db as pf_db

# Solicitação do nome do usuário:
def execute_name_pf_register():
    while True:
        pf_nome_register = input("Digite seu nome completo: ").title().strip()
        if pf_nome_register:
            return pf_nome_register
        print('\033[31mUm nome deve ser informado, tente novamente.\033[m')
    
# Solicitação de password:
def execute_password_pf_register():
    while True:
        pf_password_register = mo.validate_password(input('Digite a senha que deseja cadastrar: '))
        if pf_password_register:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pf_password_register

# Solicitação de E-mail.
def execute_mail_pf_register():
    while True:
        pf_mail_register = input('Digite seu e-mail para cadastro: ')
        pf_resultado_register = mo.validate_mailsyntaxe(pf_mail_register)
        if pf_resultado_register:
            print('\033[36mE-mail válido!\033[m')
            return pf_mail_register
        else:
            print('\033[31mE-mail inválido!\033[m')
            print("""\033[31mRegras de digitação:
- É proibído pontos no inicio, final e antes do @;
- Antes do arroba deve haver um identificador;
- Após o arroba deve haver um provedor;
- Após o provedor deve haver um domínio.\033[m
\033[36mModelo padrão:
- (identificador/nome)@(provedor)(domínios/subdomínios)\033[m""")

# Solicitação de CPF:
def execute_cpf_pf_register():
    while True:
        pf_cpf_register = input('Digite o CPF a ser cadastrado seguindo o modelo (XXX.XXX.XXX-XX): ')
        pf_resultado_register = mo.validate_cpf(cpf=pf_cpf_register)
        if pf_resultado_register:
            print('\033[36mCPF Cadastrado com sucesso!\033[m')
            return pf_cpf_register
        else:
            print('\033[31mCPF inválido!\033[m')
            print("""\033[31mRegras de digitação:
- O CPF deve seguir o modelo: XXX.XXX.XXX-XX;
- O CPF deve possuir 11 dígitos;
- O CPF deve possuir dÍgitos verificadores válidos.\033[m""")
        
# Executando as funções:
pf_nome_register = execute_name_pf_register()
pf_password_register = execute_password_pf_register()
pf_mail_register = execute_mail_pf_register()
pf_cpf_register = execute_cpf_pf_register()


# Instanciar um usuáriopf:
user = mo.create_pfuser(pf_nome_register,pf_password_register,pf_mail_register,pf_cpf_register)

# Limpeza de terminal.
mo.clean()

# Confirmação de valores informados (Decisão do usuário):


# Enviar usuário para o banco de dados:
print(pf_db.data_base)