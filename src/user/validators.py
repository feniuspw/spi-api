import re
from django.core.exceptions import ValidationError


def validate_cpf(cpf):
    cpf = re.sub("[^0-9]", "", cpf)
    if len(cpf) != 11:
        raise ValidationError("Invalid CPF: Incorrect length.")
    if cpf == cpf[0] * 11:
        raise ValidationError("Invalid CPF: All digits are the same.")

    def calculate_check_digit(digits):
        sum_of_products = sum((len(digits) + 1 - i) * int(digit)
                              for i, digit in enumerate(digits))
        check_digit = 11 - (sum_of_products % 11)
        return '0' if check_digit > 9 else str(check_digit)
    if cpf[9] != calculate_check_digit(cpf[:9]):
        raise ValidationError("Invalid CPF: First check digit is incorrect.")
    if cpf[10] != calculate_check_digit(cpf[:10]):
        raise ValidationError("Invalid CPF: Second check digit is incorrect.")
    return True


def validate_passport(value):
    if not re.match(r"^[A-Za-z0-9]{6,9}$", value):
        raise ValidationError("Invalid passport format.")


def validate_rg(value):
    return True


def validate_ssn(value):
    return True
