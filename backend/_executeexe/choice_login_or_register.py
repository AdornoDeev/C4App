import subprocess
import sys
# Arquivo executável que é responsável por chamar as opções.

while True:
    print('''Escolha como deseja acessar o de acesso:
[1] Cadastrar-se
[2] Log-in''')
    decision_choice_login_register = input('--> ').strip().lower()
    if decision_choice_login_register == '1':
        decision_choice_login_register= input('Escolha o cadastro como (PJ ou PF): ').strip().lower()
        if decision_choice_login_register == 'pf':
            subprocess.run([sys.executable, "-m", "backend.acess.register.pf_register.pf_registerexe"])
            break
        elif decision_choice_login_register == 'pj':
            subprocess.run([sys.executable, "-m", "backend.acess.register.pj_register.pj_registerexe"])
            break
    elif decision_choice_login_register == '2':
        decision_choice_login_register= input('Escolha o login como (PJ ou PF ou SH): ').strip().lower()
        if decision_choice_login_register == 'pj':
            subprocess.run([sys.executable, "-m", "backend.acess.login.pj_login.pj_loginexe"])
            break
        elif decision_choice_login_register == 'pf':
            subprocess.run([sys.executable, "-m", "backend.acess.login.pf_login.pf_loginexe"])
            break
        elif decision_choice_login_register == 'sh':
            subprocess.run([sys.executable, "-m", "backend.acess.login.sh_login.sh_loginexe"])
            break
    print('\033[31mAo menos uma das opções devem ser digitadas, tente novamente.\033[m')