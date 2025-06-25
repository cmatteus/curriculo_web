from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name="Título"
    )
    imagem = models.ImageField(
        null=False,
        blank=False,
        upload_to='projetos/',
        verbose_name="Imagem",
        help_text="Faça o upload da imagem do projeto"
    )
    descricao = models.TextField(
        null=False,
        blank=False,
        verbose_name="Descrição"
    )
    link_online = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Link para o projeto online"
    )
    link_github = models.URLField(
        blank=True,
        null=True,
        max_length=200,
        verbose_name="Link para o GitHub"
    )