# from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from user.validators import (validate_cpf, validate_passport,
                             validate_rg, validate_ssn)


DOCUMENT_VALIDATORS = {
    'CPF': validate_cpf,
    'PASSPORT': validate_passport,
    'RG': validate_rg,
    'SSN': validate_ssn
}


# Create your models here.
class User(AbstractUser):
    # Por enquanto da forma que esta, joaozinho pode se cadastrar multiplas
    # vezes com documentos diferentes
    # uma solucao eh colocar uma camada extra de coisas unicas
    # tipo email, telefone etc etc
    DOCUMENT_TYPE_CHOICES = [
        ('CPF', 'CPF'),
        ('RG', 'RG'),
        ('PASSAPORTE', 'Passaporte'),
        ('SSN', 'Social Security Number'),
    ]
    document_type = models.CharField(max_length=20,
                                     choices=DOCUMENT_TYPE_CHOICES,
                                     null=True, blank=True)
    document_value = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        unique_together = (('document_type', 'document_value'),)

    def clean(self):
        super().clean()
        try:
            validator = DOCUMENT_VALIDATORS.get(self.document_type)
            if validator is not None:
                validator(self.document_value)
            else:
                raise ValidationError('Unsupported document type.')

        except ValidationError as e:
            raise ValidationError(f"{e.message} \
                                  [Document Type: {self.document_type}]")




