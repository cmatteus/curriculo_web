# Generated by Django 5.2.3 on 2025-06-26 11:41

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformacaoPessoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotos_perfil/', verbose_name='Foto de Perfil')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('titulo_principal', models.CharField(help_text='Ex: Estudante de Sistemas de Informação', max_length=255, verbose_name='Título Principal')),
                ('cargo_atual', models.CharField(blank=True, help_text='Seu cargo na empresa em que trabalha atualmente.', max_length=255, null=True, verbose_name='Cargo Atual')),
                ('biografia', models.TextField(verbose_name='Biografia / Sobre Mim')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail de Contato')),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='BR', verbose_name='Número de Telefone')),
                ('telefone_e_whatsapp', models.BooleanField(blank=True, default=True, null=True, verbose_name='O número também é WhatsApp?')),
                ('rua', models.CharField(max_length=255, verbose_name='Rua')),
                ('numero', models.CharField(max_length=20, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('pais', models.CharField(default='Brasil', max_length=100, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Informação Pessoal',
                'verbose_name_plural': 'Informações Pessoais',
            },
        ),
    ]
