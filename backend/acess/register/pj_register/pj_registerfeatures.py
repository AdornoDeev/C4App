# Solicitação do nome estabelecimento.
import backend.modular_functionsinlore as mo
import backend.acess.register.pj_register.pj_registerclass as classpj

# Solicitação de nome.
def execute_name_pj_register():
    while True:
        pj_nome_register = input("Digite o nome do estabelecimento: ").title().strip()
        if pj_nome_register:
            return pj_nome_register
        print('\033[31mUm nome deve ser informado, tente novamente.\033[m')

# Solicitação de Senha.
def execute_password_pj_register():
# Solicitação de senha:
    while True:
        pj_password_register = mo.validate_password(input('Digite a senha que deseja cadastrar: '))
        if pj_password_register:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pj_password_register

# Solicitação de CNPJ.
def execute_cnpj_pj_register():
    while True:
        pj_cnpj_register = input('Digite os números do CNPJ seguindo modelo (XX.XXX.XXX/XXXX-XX): ')
        pj_resultado_register = mo.validate_cnpj(pj_cnpj_register)
        if pj_resultado_register:
            print('\033[36mCNPJ válido!\033[m')
            return pj_cnpj_register
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
            return pj_mail_register.lower()
        else:
            print('E-mail inválido!')
            print("""\033[31mRegras de digitação:
- É proibído pontos no inicio, final e antes do @;
- Antes do arroba deve haver um identificador;
- Após o arroba deve haver um provedor;
- Após o provedor deve haver um domínio;\033[m
\033[36mModelo padrão:
(identificafor/nome)@(provedor)(domínios/subdomínios)\033[m""")

# Confirmação de valores informados (Decisão do usuário):
def pj_confirm_register(name,password,cnpj,mail):
    while True:
        print(f"""Os dados informados correspondentes são:
    [Nome]: {name}
    [Senha]: {password}
    [CNPJ]: {cnpj}
    [E-mail]: {mail}""")
        pj_resultado_register = input('Confirme os dados. Você deseja alterar algo (S/N)? ').strip().lower()
        if pj_resultado_register == 's':
            pj_resultado_register = input("""Digite o que deseja alterar: | 1:Nome | 2:Senha | 3:CNPJ | 4:E-mail |
        ---> """)
            if pj_resultado_register not in ['1','2','3','4']:
                print('\033[31mÉ obrigatório informar uma das opções disponibilizadas. Tente novamente!\033[m')
            else:
                if pj_resultado_register == '1':
                    name = execute_name_pj_register()
                elif pj_resultado_register == '2':
                    password = execute_password_pj_register()
                elif pj_resultado_register == '3':
                    cnpj = execute_cnpj_pj_register()
                elif pj_resultado_register == '4':
                    mail = execute_mail_pj_register()
        elif pj_resultado_register  == 'n':
            return classpj.pj(name,password,cnpj,mail)
        else:
            print('\033[31mÉ obrigatório informar uma das opções disponibilizadas. Tente novamente!\033[m')
        mo.clean()

# Executa a função de coordenadas:

# Função que executa todas outras funções de coleta de dados.
def create_pj_user():
    pf_nome_register = execute_name_pj_register()
    pf_password_register = execute_password_pj_register()
    pj_cnpj_register = execute_cnpj_pj_register()
    pf_mail_register = execute_mail_pj_register()
    return [pf_nome_register,pf_password_register,pj_cnpj_register,pf_mail_register]
