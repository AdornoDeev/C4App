import regex

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