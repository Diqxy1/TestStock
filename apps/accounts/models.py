from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'Usuário',
        max_length=30,
        unique=True,
        help_text='Obrigatorio. Nó máximo 30 caracteres. Letras, e os digitos @/./+/-/_ apenas.',
        validators=[username_validator],
        error_messages={
            'unique': "Esté usuário já está sendo utilizado."
        },
    )
    name = models.CharField('Nome completo', max_length=150)
    email = models.EmailField('E-mail')
    is_staff = models.BooleanField(
        'Equipe',
        default=False,
        help_text='Define se o usuário pode acessar o painel administrativo',
    )
    is_active = models.BooleanField(
        'Status',
        default=True,
        help_text=(
            'Status do usuário'
        ),
    )
    date_joined = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'Usuários'
