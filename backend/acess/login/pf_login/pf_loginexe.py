from backend.modular_functionsinlore import clean
import backend.acess.login.pf_login.pf_loginfeatures as pf_feat
import backend.databases.pf_db.pf_db as pf_db
import subprocess,sys,json

print('[LOGIN]')
while True:
    # Solicitando informações do usuário.
    pf_login_data_saved = pf_feat.log_in_pf_user()
    # Validação dos dados no banco de dados:
    if pf_login_data_saved[0] not in pf_db.data_base_pf:
        while True:
            option_pf_login = input('Não há registro deste id no sistema, deseja criar uma conta (S/N)? ').strip().lower()
            if option_pf_login == 's':
                clean()
                subprocess.run([sys.executable,'-m','backend.acess.register.pf_register.pf_registerexe'])
                break
            elif option_pf_login == 'n':
                clean()
                print('Obrigado por utilizar nossos sistemas, volte sempre.')
                break
            else:
                print('\033[31mUma opção deve ser informada, tente novamente.\033[m')
        break
    else:
        temp_password_pf_login = pf_db.data_base_pf[pf_login_data_saved[0]]['password_pf_db']
        if temp_password_pf_login == pf_login_data_saved[1]:
            pf_login_data_saved = {'cpf':pf_login_data_saved[0],'password':pf_login_data_saved[1]}

            json_data_pf_log = json.dumps(pf_login_data_saved)
            clean()
            print(json_data_pf_log)
            subprocess.run([sys.executable,'-m','backend.mainpages.mainpage_pf.main_pfexe',json_data_pf_log])
            break
        else:
            print('\033[31mA senha ou id informado estão incorretos, tente novamente.\033[m')
