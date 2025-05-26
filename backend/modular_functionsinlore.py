import regex,os,time
import math

# Validação de um número inteiro.
def validate_intenger(num,tyquest):
    """Retorna um número inteiro válido.
    <num> -> Iterável a ser validado;
    <tyquest> -> Sobre a questão. Ex: true_cnpj print("Type the {tyquest} again:
    OBS: A tyquest é utilizada apenas por programadores.")"""
    while True:
        try:
            num = int(num)
        except ValueError as e:
            print(f"""\033[31mError Code: {e}.
                  O valor informado não é um número inteiro, tente novamente\03[m""")
            num = input(f"Digite o {tyquest} novamente: ")
        else:
            return num

# Limpeza de terminal:
def clean(sleep = 3):
    time.sleep(sleep)
    os.system('cls' if os.name == 'nt' else 'clear')

# Validação de e-mail (sintaxe).
def validate_mailsyntaxe(mail):
    """Realiza a verificação de um email, retornando verdadeiro ou falso.
    <:email:> -> E-mail a ser validado.
    Condições: Ao mínimo um identificador, ao mínimo um @, ao mínimo 1 provedor e ao mínimo 1 domínio."""
    pattern = regex.compile(r"([a-zA-Z0-9]+\.?)+[a-zA-Z0-9]+@([a-zA-Z0-9]+\.)+[a-zA-Z0-9]+")
    resultado = regex.fullmatch(pattern,mail) # Realiza um fullmatch (Verificação total) com e e-mail informado a partir do padrão.
    # Condições.
    if resultado:
        return True
    else:
        return False
    
# Validação de CNPJ (sintaxe e dígitos verificadores).
def validate_cnpj(cnpj):
    """Realiza avalidação de um cnpj em sintaxe e dígitos verificadores.
    <cnpj> -> str: É o CNPJ a ser validado (Deve conter 14 digitos no formato XX.XXX.XXX/XXXX-XX)."""

    # CNPJ Exemplo: XX.XXX.XXX.XXX/0001-XX
    pattern = regex.compile(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}") # Definindo um padrão para validação.
    resultado = regex.fullmatch(pattern,cnpj)
    if not resultado:
        return False
    else:
        # Variables:
        tempcnpj = regex.sub(r"\D",'',cnpj) # CNPJ Formatado com apenas números.
        true_cnpj = tempcnpj[0:12:] # Recolhendo a primeira parte do CNPJ para verificação e validação.
        # A função aninhada é responsávwel por calcular os dígitos válidos.
        def calculate(multiplicador,true_cnpj):
            multiplied_digits = list()
            for nums in true_cnpj:
                multiplied_digits.append(int(nums) * multiplicador)
                multiplicador -= 1
                if multiplicador == 1:
                    multiplicador = 9
            # Adcionando a soma dos numeros a lista:
            resultado = sum(multiplied_digits)
            # Dividindo o número por 11 e coletando o resultadoado:
            resultado = resultado % 11
            # Condicionais sobre o valor:
            if resultado < 2:
                resultado = 0
            else:
                resultado = 11 - resultado
            
            # Mundanças em variáveis:
            true_cnpj += str(resultado)
            return true_cnpj
        
        # Iterando duas vezes a função de validação passando o parâmetro pelo C.
        for c in range(5,7):
            true_cnpj = calculate(true_cnpj = true_cnpj, multiplicador=c)
    
    if true_cnpj == tempcnpj:
        return True
    else:
        return False

# Validação de senha (sintaxe).
def validate_password(password):
    """Obrigatóriamente valida uma senha sob condições.
    <password> -> Valor string Itrável.
    Condições:
    Ao mínimo 1 minúscula, Ao mínimo um maiúscula, Ao mínimo 6 números e ao mínimo 6 caracteres especiais desconsiderando espaços."""
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
        return password

# Validação de CPF (sintaxe e dígitos verificadores).
def validate_cpf(cpf):
    pattern = regex.compile(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}')
    resultado = regex.fullmatch(pattern,cpf)
    if not resultado:
        return False
    else:
        # Variables:
        tempcpf = regex.sub(r"\D",'',cpf) # cpf Formatado com apenas números.
        true_cpf= tempcpf[0:9:] # Recolhendo a primeira parte do cpf para verificação e validação.
        # A função aninhada é responsável por calcular os dígitos válidos.
        def calculate(multiplicador,true_cpf):
            multiplied_digits = list()
            for nums in true_cpf:
                multiplied_digits.append(int(nums) * multiplicador)
                multiplicador -= 1
            # Adicionando a soma dos numeros a lista:
            resultado = sum(multiplied_digits)
            # Dividindo o número por 11 e coletando o resultado:
            resultado = resultado % 11
            # Condicionais sobre o valor:
            if resultado < 2:
                resultado = 0
            else:
                resultado = 11 - resultado

            # Mundanças em variáveis:
            true_cpf += str(resultado)
            return true_cpf
        
        # Iterando duas vezes a função de validação passando o parâmetro pelo C.
        for c in range(10,12):
            true_cpf = calculate(true_cpf = true_cpf, multiplicador=c)
    
    if true_cpf == tempcpf:
        return True
    else:
        return False

# Validação de usuário SH (sintaxe):
def validate_sh_id(id):
   pattern = regex.compile('[0-9]+')
   resultado = regex.fullmatch(pattern, id)
   if resultado:
       return True
   else:
       return False

# Função que recebe coordenadas geofráficas
def parse_coordinates(coord_str):
    """
    Recebe uma string com coordenadas e retorna uma tupla (latitude, longitude) como floats.
    Exemplo de string: '12.3456, -78.9012'
    """
    pattern = r'(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)'
    match = regex.match(pattern, coord_str.strip())
    if not match:
        return False
    lat, lon = map(float, match.groups())
    return lat, lon

import math

import math

def calculate_distance_from_dicts(dict1, dict2):
    """
    Recebe dois dicionários com a chave 'coordenates' contendo [longitude, latitude].
    Retorna a distância entre eles em quilômetros.
    """
    lon1, lat1 = dict1["coordenates"]
    lon2, lat2 = dict2["coordenates"]
    name = dict2['name_pf_db']

    # Converter para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Fórmula de Haversine
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371  # Raio da Terra em km
    return [name, R * c]

def filtrar_cnpjs_por_distancia(lista_de_dados, limite=5):
    """
    Recebe uma lista de sublistas no formato [nome, distancia, cnpj]
    e retorna uma lista com os CNPJs cuja distância seja <= limite (padrão: 35).
    """
    cnpjs_filtrados = []

    for item in lista_de_dados:
        if len(item) != 3:
            continue  # ignora se o item não tiver exatamente 3 elementos
        
        nome, distancia, cnpj = item
        
        try:
            if float(distancia) <= limite:
                cnpjs_filtrados.append(cnpj)
        except (ValueError, TypeError):
            continue  # ignora se a distância não for numérica

    return cnpjs_filtrados
