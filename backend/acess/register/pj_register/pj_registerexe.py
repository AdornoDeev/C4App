from backend import modular_functionsinlore as mo

# Solicitação do nome estabelecimento:
def execute_name_pj_register():
    while True:
        pj_nome_register = input("Digite o nome do estabelecimento: ").title().replace(' ','')
        if pj_nome_register:
            break
        print('\033[31mUm nome deve ser informado, tente novamente.\033[m')

def execute_password_pj_register():
# Solicitação de senha:
    while True:
        pj_password_register = mo.validate_password(input('Digite a senha que deseja cadastrar: '))
        if pj_password_register:
            print('\033[36mFormato validado com sucesso!\033[m')
            break

# Solicitação de CNPJ.
def execute_cnpj_pj_register():
    while True:
        pj_cnpj_register = input('Digite os números do CNPJ seguindo modelo (XX.XXX.XXX/XXXX-XX): ')
        pj_resultado_register = mo.validate_cnpj(pj_cnpj_register)
        if pj_resultado_register:
            print('\033[36mCNPJ válido!\033[m')
            break
        else:
            print('\033[31mCNPJ Inválido!\033[m')
            print("""\033[31mRegras de digitação:
- É proibido não seguir o modelo de digitação: XX.XXX.XXX/XXXX-XX com todos os pontos, barra e traço.
- O CNPJ deve possur 14 dígitos;
- Os dígitos verificadores devem corresponder ao cálculo.\033[m""")


# Solicitação de E-mail.
def execute_mail_pj_register():
    while True:
        pj_mail_register = input('Digite o e-mail de cadastro do estabelecimento: ')
        pj_resultado_register = mo.validate_mailsyntaxe(pj_mail_register)
        if pj_resultado_register:
            print('\033[36mE-mail válido!\033[m')
            mo.clean()
            break
        else:
            print('E-mail inválido!')
            print("""\033[31mRegras de digitação:
- É proibído pontos no inicio, final e antes do @;
- Antes do arroba deve haver um identificador;
- Após o arroba deve haver um provedor;
- Após o provedor deve haver um domínio;\033[m
\033[36mModelo padrão:
(identificafor/nome)@(provedor)(domínios/subdomínios)\033[m""")
            
# Executando as funções:
pj_nome_register = execute_name_pj_register()
pj_password_register = execute_password_pj_register()
pj_cnpj_register = execute_cnpj_pj_register()
pj_mail_register = execute_mail_pj_register()

# Instanciar um usuáriopj:
user = mo.create_pjuser(pj_nome_register,pj_password_register,pj_mail_register,pj_cnpj_register)

# Confirmação de valores informados (Decisão do usuário):

# Enviar usuário para o banco de dados: