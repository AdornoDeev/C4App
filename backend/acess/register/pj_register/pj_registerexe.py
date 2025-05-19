from backend import modular_functionsinlore as mo

''''
password = None
# Solicitação do nome estabelecimento:
nome = input("Digite o nome do estabelecimento: ")

# Solicitação de senha:
while not password:
    password = mo.validate_password(input('Digite a senha que deseja cadastrar: '))

# Solicitação de E-mail.
while True:
    mail = input('Digite o e-mail de cadastro do estabelecimento: ')
    resultado = mo.validate_mailsyntaxe(mail)
    if resultado:
        print('\033[36mE-mail válido!\033[m')
        mo.clean()
        break
    else:
        print('E-mail inválido!')
        print("""\033[31mRegras de digitação:
É proibído ponto no inicio, final e antes do @;
É proibido antes do arroba não haver um identificador;
É proibido após o arroba não haver um provedor;
É proibído após o provedor não haver um domínio;\033[m
\033[36mModelo padrão:
(identificafor/nome)@(provedor)(domínios/subdomínios)\033[m""")

# Solicitação de E-mail.
while True:
    cnpj = input('Digite os números do CNPJ seguindo modelo (XX.XXX.XXX/XXXX-XX):  ')
    resultado = mo.validate_cnpj(cnpj)
    if resultado:
        print('\033[36mCNPJ válido!\033[m')
        break
    else:
        print('\033[31mCNPJ Inválido!\033[m')
        print("""\033[31mRegras de digitação:
É proibido não seguir o modelo de digitação: XX.XXX.XXX/XXXX-XX com todos os pontos, barra e traço.
Um CNPJ possúi 14 dígitos,\033[m
O Dígitos verificadores deve corresponder ao cálculo.""")
'''