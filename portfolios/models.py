# coding: utf-8
from django.db import models
from django.utils import timezone


class DadosPessoais(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Nome')
    street = models.CharField(max_length=100, verbose_name='Endereço')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    cep = models.CharField(max_length=50, verbose_name='Cep')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    moblie = models.CharField(max_length=20, verbose_name='Celular')
    about = models.TextField(max_length=255, verbose_name='Sobre')
    data_nascimento = models.DateField(default=timezone.now, verbose_name='Data Nascimento')
    email = models.EmailField(verbose_name='Email')
    conhecimentos = models.TextField(max_length=255, verbose_name='Conhecimentos')
    github = models.CharField(max_length=100, verbose_name='link')
    curse = models.CharField(max_length=100, verbose_name='Curso')
    local = models.CharField(max_length=100, verbose_name='Local')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    resumo = models.TextField(max_length=255, verbose_name='Resumo')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Dados Pessoais'
        verbose_name_plural = 'Dados Pessoais'
