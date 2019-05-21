from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class GestaoUsuario(BaseUserManager):
    def create_user(self, nome, email, username, password=None):

        if not nome:
            raise ValueError('Usuários precisam de um nome!')

        if not email:
            raise ValueError('Usuários precisam de um endereço de e-mail!')

        if not username:
            raise ValueError('Usuários precisam de um nome de usuário!')

        user = self.model(
            nome=nome,
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, username, password):

        user = self.create_user(
            nome=nome,
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nome = models.TextField(
        verbose_name='nome',
        max_length=15,
        unique=False
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=20,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = GestaoUsuario()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nome', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
