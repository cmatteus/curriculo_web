from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

class InformacaoPessoal(models.Model):
    nome_completo = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        verbose_name="Nome Completo"
    )
    foto_perfil = models.ImageField(
        upload_to='fotos_perfil/',
        blank=True,
        null=True, 
        verbose_name="Foto de Perfil"
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        null=False,
        blank=False
    )
    titulo_principal = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        verbose_name="Título Principal",
        help_text="Ex: Estudante de Sistemas de Informação"
    )
    cargo_atual = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="Cargo Atual",
        help_text="Seu cargo na empresa em que trabalha atualmente."
    )
    biografia = models.TextField(
        null=False,
        blank=False,
        verbose_name="Biografia / Sobre Mim"
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name="E-mail de Contato"
    )
    telefone = PhoneNumberField(
        null=True,
        blank=True,
        region='BR',
        verbose_name="Número de Telefone"
    )
    telefone_e_whatsapp = models.BooleanField(
        null=True,
        blank=True,
        default=True,
        verbose_name="O número também é WhatsApp?"
    )
    rua = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        verbose_name="Rua"
    )
    numero = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name="Número"
    )
    bairro = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name="Bairro"
    )
    cidade = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name="Cidade"
    )
    estado = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name="Estado"
    )
    pais = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name="País",
        default="Brasil"
    )


    def save(self, *args, **kwargs):
        """
        Garante que apenas uma instância deste modelo possa ser criada (Padrão Singleton).
        """
        self.pk = 1 # Define a chave primária como 1
        super(InformacaoPessoal, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Impede a exclusão da instância.
        """
        pass # Não faz nada, efetivamente bloqueando a exclusão

    @classmethod
    def load(cls):
        """
        Método de conveniência para carregar a única instância.
        """
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = "Informação Pessoal"
        verbose_name_plural = "Informações Pessoais"

    def __str__(self):
        return self.nome_completo
    
class RedesSociais(models.Model):
    linkedin = models.URLField(
        blank=True,
        null=True,
        verbose_name="LinkedIn"
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        verbose_name="Instagram"
    )
    github = models.URLField(
        blank=True,
        null=True,
        verbose_name="GitHub"
    )

    def save(self, *args, **kwargs):
        """
        Garante que apenas uma instância deste modelo possa ser criada.
        """
        self.pk = 1
        super(RedesSociais, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Impede a exclusão da instância.
        """
        pass

    @classmethod
    def load(cls):
        """
        Método de conveniência para carregar a única instância.
        """
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = "Rede Social"
        verbose_name_plural = "Redes Sociais"

    def __str__(self):
        return "Links das Redes Sociais"