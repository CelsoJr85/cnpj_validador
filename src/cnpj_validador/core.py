import re


def _converter_caractere(c: str) -> int:
    """
    Regra Oficial Definitiva da Receita Federal (Nota Técnica 2025/001):
    O valor decimal corresponde ao código ASCII do caractere menos 48.
    - Dígitos '0' (ASCII 48) a '9' (ASCII 57) mantêm os valores de 0 a 9.
    - Letras 'A' (ASCII 65) a 'Z' (ASCII 90) passam a valer de 17 a 42.
    """
    return ord(c.upper()) - 48


def _calcular_digito(cnpj_base: list, pesos: list) -> int:
    soma = sum(v * p for v, p in zip(cnpj_base, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def validar_cnpj(cnpj_str: str) -> bool:
    if not isinstance(cnpj_str, str):
        return False

    cnpj_limpo = re.sub(r'[^A-Za-z0-9]', '', cnpj_str).upper()

    if len(cnpj_limpo) != 14:
        return False

    valores = [_converter_caractere(c) for c in cnpj_limpo]

    # Pesos padrão do Módulo 11 para CNPJ
    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    base = valores[:12]
    digitos_informados = valores[12:]

    digito_1 = _calcular_digito(base, pesos_1)
    digito_2 = _calcular_digito(base + [digito_1], pesos_2)

    return digitos_informados == [digito_1, digito_2]
