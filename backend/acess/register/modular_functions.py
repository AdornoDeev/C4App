from backend.acess.register.pj_register import pj_registerclass
import re
# Função de validação de nome:
def validate_name(name):
    """ """
    
    # Validating name with only alphabetic
    while True:
        if not name.replace(' ','').isalpha():
            print('\033[31mDigite apenas letras, nenhum tipo de número ou símbolo é permitido. Tente novamente!\033[m')
            name = input('Digite o nome do estabelecimento: ')
        else:
            return name.title()
    
# Função de validação de senha:
def validate_password(password):
    """ """
    # Condições de validação de senha: Ao mínimo 1 minuscula, 1 maiúscula, ao mínimo 6 Números e ao mínimo 1 caracteres especial.
    while True:
        password = password.replace(' ','')
        # Contadores do laço:
        qtnd_numeros = 0
        qtdn_lower = 0
        qtdn_upper = 0
        qtdn_char = 0

        # Validação letra a letra.
        for letra in password:
            if letra.isnumeric():
                qtnd_numeros += 1
            if letra.isupper():
                qtdn_upper += 1
            if letra.islower():
                qtdn_lower += 1
        if not password.isalnum():
            qtdn_char += 1
        
        # Condições de validação final:
        if qtnd_numeros < 6:
            print('\033[31mSão necessários ao mínimo 6 números, tente novamente!\033[m')