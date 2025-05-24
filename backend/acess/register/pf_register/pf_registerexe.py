import backend.databases.pf_db.pf_db as pf_db
import backend.acess.register.pf_register.pf_registerfeatures as pf_features_
from backend.modular_functionsinlore import clean
import subprocess

# Executando as funções de coleta de dados essenciais do usuário:
user_pf_register = pf_features_.create_pf_user() # Os dados são splitados em uma lista como sequência de NOME, SENHA, CPF E EMAIL.

# Limpeza de terminal.
clean()

# Confirmação de valores informados (Decisão do usuário):
user_pf_register = pf_features_.pj_confirm_register(name=user_pf_register[0],password=user_pf_register[1],cpf=user_pf_register[2],mail=user_pf_register[3])

# Validando se o CPF já existe como um identificador.
while user_pf_register.cpf in pf_db.data_base_pf:
    print('\033[31mO CPF informado já está cadastrado, redefina o CPF para continuar.\033[m')
    user_pf_register.cpf = pf_features_.execute_cpf_pf_register()

# Coletando todos os e-mails cadastrados no banco de dados.
list_mails_pf_register = list()
for chaves in pf_db.data_base_pf:
    list_mails_pf_register.append(pf_db.data_base_pf[chaves]['mail_pf_db'])

# Validando a existência de um usuário cadastrado no sistema.
while user_pf_register.mail in list_mails_pf_register:
    print('\033[31mO e-mail informado já está cadastrado, redefina o e-mail para continuar.\033[m')
    user_pf_register.mail = pf_features_.execute_mail_pf_register()

# Enviar usuário para o "banco de dados":
pf_db.data_base_pf[user_pf_register.cpf] = {'nome_pf_db':user_pf_register.name,'password_pf_db':user_pf_register.password,'mail_pf_db':user_pf_register.mail,'cpf_pf_db':user_pf_register.cpf}

# Executando a página main de PFísica:
subprocess.run(["python", "backend/mainpages/mainpage_pf/main_pf.py"])