from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from stdimage import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9, null=False, blank=False)
    score = models.IntegerField('Score')
    imagem = StdImageField(
        'Imagem', upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}},
        default=''
    )

    def __str__(self):
        return self.nome


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é OBRIGATÓRIO')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Precisar ser SUPER USUÁRIO')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Precisa ser usuário padrão')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('Repita o Email', unique=True)
    nome = models.CharField('Nome', max_length=300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
