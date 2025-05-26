import regex
import backend.modular_functionsinlore as mo
import os
import json

# Validação de sintaxe de CNPJ.
def exclusive_validate_cnpj_login(cnpj):
    """Realiza avalidação de um cnpj em sintaxe e dígitos verificadores.
    <cnpj> -> str: É o CNPJ a ser validado (Deve conter 14 digitos no formato XX.XXX.XXX/XXXX-XX)."""

    # CNPJ Exemplo: XX.XXX.XXX.XXX/0001-XX
    pattern = regex.compile(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}") # Definindo um padrão para validação.
    resultado = regex.fullmatch(pattern,cnpj)
    if not resultado:
        return False
    else:
        return True
    
# Solicitação de CNPJ:
def execute_cnpj_pj_login():
    while True:
        pj_cnpj_login = input('Digite os números do CNPJ seguindo modelo (XX.XXX.XXX/XXXX-XX): ')
        pj_resultado_login = exclusive_validate_cnpj_login(pj_cnpj_login)
        if pj_resultado_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pj_cnpj_login
        else:
            print('\033[31mCNPJ Inválido!\033[m')
            print("""\033[31mRegras de digitação:
- É proibido não seguir o modelo de digitação: XX.XXX.XXX/XXXX-XX com todos os pontos, barra e traço.
- O CNPJ deve possuir 14 dígitos.\033[m""")

# Solicitando a password do usuário:
def execute_password_pj_login():
    while True:
        pf_password_login = mo.validate_password(input('Digite a senha atribuida ao CNPJ: '))
        if pf_password_login:
            print('\033[36mFormato validado com sucesso!\033[m')
            return pf_password_login
        
# Excução das funções:
def log_in_pj_user():
    pj_cnpj_login = execute_cnpj_pj_login()
    pj_password_login = execute_password_pj_login()
    return [pj_cnpj_login,pj_password_login]

