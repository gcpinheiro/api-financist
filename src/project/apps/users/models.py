from django.db import models


class UserModel(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
      managed = False
      db_table = 'users'