import re
from typing import List
from validate_docbr import CPF


def validate_cpf(cpf: str, errors: List) -> None:
    validator = CPF(True)
    if not validator.validate(cpf):
        errors.append({'cpf': 'O CPF informado não é válido.'})


def validate_nome(nome: str, errors: List) -> None:
    if not re.fullmatch('[a-zA-Z\s]+', nome):
        errors.append({'nome': 'O campo Nome deve possuir somente caracteres alfabéticos.'})


def validate_rg(rg: str, errors: List) -> None:  # pylint: disable=invalid-name
    if len(rg) != 10:
        errors.append({'rg': 'O campo RG deve possuir exatamente 10 dígitos.'})

    if not re.fullmatch(r'[\d]+', rg):
        errors.append({'rg': 'O campo RG deve possuir somente caracteres numéricos.'})


def validate_celular(celular: str, errors: List) -> None:
    if not re.fullmatch('[a-zA-Z\s]+', celular):
        errors.append({'celular': 'O campo Celular digitado não é válido.'})
