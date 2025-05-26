from backend.modular_functionsinlore import clean
import backend.acess.login.pj_login.pj_loginfeatures as pj_feat
import backend.databases.pj_db.pj_db as pj_db
import subprocess,sys,json

print('[LOGIN]')

# Função de salvamento do arquivo Json:

while True:
    # Solicitando informações do usuário.
    pj_login_data_saved = pj_feat.log_in_pj_user()
    # Validação dos dados no banco de dados:
    if pj_login_data_saved[0] not in pj_db.data_base_pj:
        while True:
            option_pj_login = input('Não há registro deste CNPJ no sistema, deseja criar uma conta (S/N)? ').strip().lower()
            if option_pj_login == 's':
                clean()
                subprocess.run([sys.executable,'-m','backend.acess.register.pj_register.pj_registerexe'])
                break
            elif option_pj_login == 'n':
                clean()
                print('Obrigado por utilizar nossos sistemas, volte sempre.')
                break
            else:
                print('\033[31mUma opção deve ser informada, tente novamente.\033[m')
        break
    else:
        temp_password_pj_login = pj_db.data_base_pj[pj_login_data_saved[0]]['password_pj_db']
        if temp_password_pj_login == pj_login_data_saved[1]:
            pj_login_data_saved = {'cnpj':pj_login_data_saved[0],'password':pj_login_data_saved[1]}
            
            json_data_pj_log = json.dumps(pj_login_data_saved)
            clean()
            subprocess.run([sys.executable,'-m','backend.mainpages.mainpage_pj.main_pjexe',json_data_pj_log])
            break
        else:
            print('\033[31mA senha ou CNPJ informado estão incorretos, tente novamente.\033[m')
