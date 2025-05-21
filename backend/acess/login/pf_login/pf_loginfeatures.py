import regex

# Validação de sintaxe de CPF.
def exclusive_validate_cpf_login(cpf):
    pattern = regex.compile(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}')
    resultado = regex.fullmatch(pattern,cpf)
    if not resultado:
        return False
    else:
        return True