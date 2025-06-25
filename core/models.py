from django.db import models
from django.core.exceptions import ValidationError

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

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    cargo = models.CharField(
        blank=False,
        null=False, 
        max_length=200,
        verbose_name="Cargo")
    nome_empresa = models.CharField(
        blank=False,
        null=False, 
        max_length=200,
        verbose_name="Nome da Empresa")
    icone_empresa = models.ImageField(
        upload_to='icones_empresas/',
        blank=False,
        null=False, 
        verbose_name="Ícone da Empresa",
        help_text="Faça o upload do logo/ícone da empresa"
    )
    data_inicio = models.DateField(
        blank=False,
        null=False, 
        verbose_name="Data de Início"
    )
    emprego_atual = models.BooleanField(
        default=False,
        verbose_name="Este é o emprego atual?",
        help_text="Marque esta opção se você ainda trabalha nesta empresa."
    )
    data_fim = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de Fim",
        help_text="Deixe em branco se for o emprego atual."
    )
    descricao = models.TextField(
        verbose_name="Descrição das Atividades"
    )

    def clean(self):
        """
        Adiciona uma validação customizada para garantir a lógica entre os campos.
        """
        super().clean()
        if self.emprego_atual and self.data_fim:
            raise ValidationError(
                "Se 'Emprego Atual' está marcado, o campo 'Data de Fim' não pode ser preenchido."
            )
        if not self.emprego_atual and not self.data_fim:
             raise ValidationError(
                "Se este não é o seu emprego atual, você precisa preencher o campo 'Data de Fim'."
            )

    def __str__(self):
        return f"{self.cargo} na empresa {self.nome_empresa}"