# Validate char function name:
'''def validate_name(name):
    """Return a valid name.title() with only charters.
    <name> -> Str value iterable"""
    while True:
        if not name.replace(' ','').isalpha(): # Remove Spaces
            print('\033[31mDigite apenas letras, nenhum tipo de número ou símbolo é permitido. Tente novamente!\033[m')
            name = input('Digite o nome do estabelecimento: ') # Ask the name again if wrong.
        else:
            print('\033[36mNome do estabelecimento cadastrado com sucesso.\033[m')
            return name.title() # Return the titlename'''

# Validating a intenger number:
def validate_intenger(num,tyquest):
    """Return a valid intenger number.
    <num> -> The itarable to be validate;
    <tyquest> -> What is the question. Ex: true_cnpj print("Type the {tyquest} again:
    OBS: The tyquest is only used by programmers.")"""
    while True:
        try:
            num = int(num)
        except ValueError as e:
            print(f"""\033[31mError Code: {e}.
                  O valor informado não é um número inteiro, tente novamente\03[m""")
            num = input(f"Digite o {tyquest} novamente: ")
        else:
            return num


# Validate char function password:
def validate_password(password):
    """Return valid password with conditions.
    <password> -> Str Value iterable.
    Conditions:
    At least 1 lower, At least 1 Upper, At least 6 numbers and At least 1 special char."""
    password = password.replace(' ','')
    # Contadores do laço:
    qtdn_numeros = 0
    qtdn_lower = 0
    qtdn_upper = 0
    qtdn_specchar = 0
    # Variável de controle de condições:
    control_return = 0

    # Validação letra a letra.
    for letra in password:
        if letra.isnumeric():
            qtdn_numeros += 1
        if letra.isupper():
            qtdn_upper += 1
        if letra.islower():
            qtdn_lower += 1
    if not password.isalnum():
        qtdn_specchar = 1
        
    # Errors and final conditions:
    if qtdn_numeros < 6:
        print('\033[31mÉ necessário ao mínimo 6 números, tente novamente!\033[m')
        control_return = 1
    if qtdn_lower < 1:
        print('\033[31mÉ necessário ao mínimo 1 letra minúscula, tente novamente!\033[m')
        control_return = 1
    if qtdn_upper < 1:
        print('\033[31mÉ necessário ao mínimo 1 letra maiúscula, tente novamente!\033[m')
        control_return = 1
    if qtdn_specchar != 1:
        print('\033[31mÉ necessário ao mínimo 1 caractere especial, tente novamente!\033[m')
        control_return = 1

    if control_return != 1:
        print('\033[36mSenha Válida!\033[m')
        return password

# Validate char e-mail function:
def validate_mail(mail):
    """return a valid e-mail with conditions.
    <mail> -> Str value iterable.
    Conditions:
    It must has only one [@] in the e-mail, It must has a name before the [@]
    and it must has a provisor with domain after the [@]"""
    mail = mail.replace(' ','')
        
    qtdn_arroba = mail.count('@')
    qtdn_ponto = mail.count('.')
    pos_arroba = mail.find('@')
    pos_ponto = mail.find('.')

    if not qtdn_arroba == 1:
        print("\033[31mO e-mail informado está inválido, não há ou existem mais de um (@) no e-mail informado, tente novamente!\033[m")
    elif pos_arroba == 0:
        print("\033[31mO e-mail informado está inválido, alguma frase ou nome deve estar antes do (@), tente novamente!\033[m")
    elif '.' not in mail[pos_arroba::]:
        print("\033[31mO e-mail informado está inválido, não há um (.) para identificação de domínio após o (@) no e-mail informado, tente novamente!\033[m")
    elif pos_ponto == (pos_arroba + 1):
        print("\033[31mO e-mail informado está inválido, um provedor deve ser informado entre o (@) e o (.), tente novamente!\033[m")
    elif mail[-1] == '.':
        print("\033[31mO e-mail informado está inválido, um domínio deve ser informado após o (.), tente novamente!\033[m")
    else:
        print("\033[36mE-mail válido!\033[m")
        return mail
    

# Validating a true_cnpj mathematically:
def validate_cnpj(cnpj):
    if not cnpj.isnumeric():
       print("\033[31mNão é permitido o dígito de símbolos, pontuações e letras. Tente novamente!\033[m")
       return None
    elif len (cnpj) != 14:
        print("\033[31mUm CNPJ válido possui 14 dígitos, tente novamente.\033[m")
        return None
    else:
        # Varibles:
        multiplier = 5 # Multiplicator for the first sequence.
        sequence_list = list()
        true_cnpj = cnpj[0:12:]

        # Validating the first digit:
        for nums in true_cnpj:
            sequence_list.append(int(nums) * multiplier)
            multiplier -= 1
            if multiplier == 1:
                multiplier = 9
        
        # Adding all the numbers in the list:
        result = sum(sequence_list)
        
        # Dividing the number by 11 and colecting the remainder:
        result = result % 11

        # Conditionals to the value:
        if result < 2:
            result = 0
        else:
            result = 11 - result
        
        true_cnpj += str(result)
    # Validating the second digit:
    sequence_list.clear()
    multiplier = 6
    for nums in true_cnpj:
        sequence_list.append(int(nums) * multiplier)
        multiplier -= 1
        if multiplier == 1:
            multiplier = 9
            
    # Adding all the numbers in the list:
    result = sum(sequence_list)
        
    # Dividing the number by 11 and colecting the remainder:
    result = result % 11

    # Conditionals to the value:
    if result < 2:
        result = 0
    else:
        result = 11 - result
    true_cnpj += str(result)
    
    if true_cnpj == cnpj:
        print(f"\033[36mO CNPJ é válido!\033[m")
        return cnpj
    else:
        print(f"\033[34mO CNPJ é inválido!\033[m")
        return None