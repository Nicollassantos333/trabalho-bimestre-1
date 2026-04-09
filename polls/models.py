from django import forms
from django.db import models

# create your models here.
class pergunta(models.Model):
    nome = models.CharField(verbose_name="Insira seu nome", max_length=20)
    email = models.EmailField(verbose_name="Insira seu endereço de Email", max_length=250)
    senha = models.CharField(verbose_name="Insira sua senha", max_length=20)
    def __str__(self):
            return self.nome