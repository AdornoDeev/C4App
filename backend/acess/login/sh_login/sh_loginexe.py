import backend.modular_functionsinlore as mo
import backend.acess.login.sh_login.sh_loginfeatures as sh_feat
import backend.acess.login.pj_login.pj_loginfeatures as pj_feat_log
import backend.databases.sh_db.sh_db as sh_db
import backend.databases.pj_db.pj_db as pj_db
import subprocess,sys,json

print('[LOGIN]')

contador_sh_login = 0

# Solicitando o cnpj da empresa para locailzar o funcionário:
while True:
    cnpj_acess_sh = pj_feat_log.execute_cnpj_pj_login()
    if cnpj_acess_sh not in pj_db.data_base_pj:
        print('\033[31mCNPJ não encontrado, tente novamente!\033[m')
    else:
        break


while True:
    # Solicitando informações do usuário.
    sh_login_data_saved = sh_feat.log_in_sh_user()
    # Validação dos dados no banco de dados:
    if sh_login_data_saved[0] not in sh_db.data_base_sh[cnpj_acess_sh]:
        print('\033[31mA senha ou ID informado estão incorretos, tente novamente.\033[m')
        mo.clean()
    else:
        temp_password_sh_login = sh_db.data_base_sh[cnpj_acess_sh][sh_login_data_saved[0]]['password_sh_db']
        if temp_password_sh_login == sh_login_data_saved[1]:
            
            sh_login_data_saved = {'id':sh_login_data_saved[0],'password':sh_login_data_saved[1], 'cnpj':cnpj_acess_sh}
            json_data_sh_log = json.dumps(sh_login_data_saved)
            mo.clean()
            subprocess.run([sys.executable,'-m','backend.mainpages.mainpage_sh.main_shexe',json_data_sh_log])
            break
        else:
            print('\033[31mA senha ou ID informado estão incorretos, tente novamente.\033[m')
            mo.clean()
    contador_sh_login += 1
    if contador_sh_login == 2:
        decision_sh_login = input('Digite (sair) para sair do sistema: ').strip()
        if decision_sh_login == 'sair':
            print('Obrigado por utilizar nossos sistemas, volte sempre.')
            break
# Limpeza de terminal.
