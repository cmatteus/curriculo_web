# Generated by Django 5.2.3 on 2025-06-26 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_educacao_formacao_habilidade_lingua'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educacao',
            options={'verbose_name': 'Formação Educacional', 'verbose_name_plural': 'Formações Educacionais'},
        ),
        migrations.AlterModelOptions(
            name='experiencia',
            options={'verbose_name': 'Experiência Profissional', 'verbose_name_plural': 'Experiências Profissionais'},
        ),
        migrations.AlterModelOptions(
            name='formacao',
            options={'verbose_name': 'Formação Acadêmica', 'verbose_name_plural': 'Formações Acadêmicas'},
        ),
        migrations.AlterModelOptions(
            name='habilidade',
            options={'verbose_name': 'Habilidade', 'verbose_name_plural': 'Habilidades'},
        ),
        migrations.AlterModelOptions(
            name='lingua',
            options={'verbose_name': 'Língua', 'verbose_name_plural': 'Línguas'},
        ),
        migrations.AlterModelOptions(
            name='projeto',
            options={'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
    ]
