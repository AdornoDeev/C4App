import backend.databases.pj_db.pj_db as pj_db
import backend.acess.register.pj_register.pj_registerfeatures as pj_features_
import backend.databases.products_db.products_db as productsdb
import backend.modular_functionsinlore as mo
import subprocess
import sys

print('[CADASTRO]')

# Utilização da função que realiza a execução de outras funções de coletas de dados.
user_pj_register = pj_features_.create_pj_user() # Os dados são splitados em uma lista como sequência de NOME, SENHA, CNPJ E EMAIL.

# Limpeza de terminal.
mo.clean()

# Confirmação de seguimento do usuário e instânciação em uma class.
user_pj_register = pj_features_.pj_confirm_register(user_pj_register[0],user_pj_register[1],user_pj_register[2],user_pj_register[3])

# Validação de CNPJ como identificador já cadastrado no sistema:
while user_pj_register.cnpj in pj_db.data_base_pj:
    print('\033[31mO CNPJ informado ja está relacionado a outro usuário, você deve cadastrar outro CNPJ.\033[m')
    user_pj_register.cnpj = pj_features_.execute_cnpj_pj_register()

# Coletando todos os e-mails cadastrados no banco de dados.
list_mails_pj_register = list()
for chaves in pj_db.data_base_pj:
    list_mails_pj_register.append(pj_db.data_base_pj[chaves]['mail_pj_db'])

# Validando a existência de um usuário cadastrado no sistema.
while user_pj_register.mail in list_mails_pj_register:
    print('\033[31mO e-mail informado já está cadastrado, redefina o e-mail para continuar.\033[m')
    user_pj_register.mail = pj_features_.execute_mail_pj_register()

# Função de coleta:
def execute_coordenate_pj():
    while True:
        coordenates = mo.parse_coordinates(input('Digite as coordenadas geográficas de sua localização: '))
        if coordenates:
            print('Coordenadas cadastradas com sucesso!')
            return coordenates
        if not coordenates:
            print('O formato a ser seguido é: "12.3456, -78.9012")')

# Coletando as cordenadas
coordenates = execute_coordenate_pj()
# Enviar usuário para o banco de dados:
pj_db.data_base_pj[user_pj_register.cnpj] = {'name_pj_db':user_pj_register.name,'password_pj_db':user_pj_register.password,'cnpj_pj_db':user_pj_register.cnpj,'mail_pj_db':user_pj_register.mail,'coordenates':coordenates}

# Criando uma partição do usuário no banco de produtos:
productsdb.data_base_products.update({user_pj_register.cnpj: {}})

# Salvar usuário para o banco de dados:
pj_db.save_db_pj()
productsdb.save_db_products()

# Limpeza de terminal.
mo.clean()

# Executando a página main de PJrídica:
subprocess.run([sys.executable,'-m', "backend.acess.login.pj_login.pj_loginexe"])