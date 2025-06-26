from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

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

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

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
    
    class Meta:
        verbose_name = "Experiência Profissional"
        verbose_name_plural = "Experiências Profissionais"

    def __str__(self):
        return f"{self.cargo} na empresa {self.nome_empresa}"
    
class Lingua(models.Model):

    class Nivel(models.TextChoices):
        ELEMENTAR = 'Elementar', 'Elementar'
        BASICO = 'Básico', 'Básico'
        BASICO_INTERMEDIARIO = 'Básico-Intermediário', 'Básico-Intermediário'
        INTERMEDIARIO = 'Intermediário', 'Intermediário'
        INTERMEDIARIO_AVANCADO = 'Intermediário-Avançado', 'Intermediário-Avançado'
        AVANCADO = 'Avançado', 'Avançado'
        FLUENTE = 'Fluente', 'Fluente'
        NATIVO = 'Nativo', 'Nativo'

    lingua = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        verbose_name="Língua"
    )
    icone = models.ImageField(
        upload_to='icones_linguas/',
        blank=False,
        null=False,
        verbose_name="Ícone da Língua"
    )
    nivel = models.CharField(
        blank=False,
        null=False,
        choices=Nivel.choices,
        verbose_name="Nível"
    )

    class Meta:
        verbose_name = "Língua"
        verbose_name_plural = "Línguas"

    def __str__(self):
        return f"{self.lingua} ({self.get_nivel_display()})"
    
class Habilidade(models.Model):

    class Tipo(models.TextChoices):
        HARD_SKILL = 'HARD', 'Hard Skill'
        SOFT_SKILL = 'SOFT', 'Soft Skill'

    habilidade = models.CharField(
        blank=False,
        null=False, 
        max_length=100,
        verbose_name="Habilidade"
    )
    icone = models.ImageField(
        upload_to='icones_habilidades/',
        blank=False,
        null=False, 
        verbose_name="Ícone da Habilidade"
    )
    tipo = models.CharField(
        blank=False,
        null=False, 
        max_length=4,
        choices=Tipo.choices,
        default=Tipo.HARD_SKILL,
        verbose_name="Tipo de Habilidade"
    )
    descricao = models.TextField(
        blank=True,
        null=True, 
        verbose_name="Descrição",
        help_text="Descreva brevemente a habilidade."
    )

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return f"{self.habilidade} - {self.get_tipo_display()}"
    
class Educacao(models.Model):

    class Tipo(models.TextChoices):
        CURSO = 'CURSO', 'Curso'
        CERTIFICACAO = 'CERT', 'Certificação'

    titulo = models.CharField(
        blank=False,
        null=False,
        max_length=200,
        verbose_name="Título"
    )
    instituicao = models.CharField(
        blank=False,
        null=False,
        max_length=200,
        verbose_name="Instituição / Empresa"
    )
    tipo = models.CharField(
        blank=False,
        null=False,
        max_length=5,
        choices=Tipo.choices,
        default=Tipo.CURSO,
        verbose_name="Tipo"
    )
    data_conclusao = models.DateField(
        blank=False,
        null=False,
        verbose_name="Data de Conclusão"
        )
    descricao = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição"
    )
    link_certificado = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link para o Certificado"
    )

    class Meta:
        verbose_name = "Formação Educacional"
        verbose_name_plural = "Formações Educacionais"

    def __str__(self):
        return self.titulo
    
class Formacao(models.Model):

    class Grau(models.TextChoices):
        ENSINO_FUNDAMENTAL = 'Ensino Fundamental', 'Ensino Fundamental'
        ENSINO_MEDIO = 'Ensino Médio', 'Ensino Médio'
        CURSO_TECNICO = 'Curso Técnico', 'Curso Técnico'
        CURSO_SUPERIOR = 'Curso Superior', 'Curso Superior'
        ESPECIALIZACAO = 'Especialização', 'Especialização'
        MBA = 'MBA', 'MBA'
        MESTRADO = 'Mestrado', 'Mestrado'
        DOUTORADO = 'Doutorado', 'Doutorado'

    curso = models.CharField(
        blank=False,
        null=False,
        max_length=200,
        verbose_name="Curso"
    )
    instituicao = models.CharField(
        blank=False,
        null=False,
        max_length=200,
        verbose_name="Instituição"
    )
    logo_instituicao = models.ImageField(
        upload_to='logos_instituicoes/',
        blank=False,
        null=False,
        verbose_name="Logo da Instituição"
    )
    grau = models.CharField(
        blank=False,
        null=False,
        choices=Grau.choices,
        verbose_name="Grau"
    )
    data_inicio = models.DateField(
        blank=False,
        null=False,
        verbose_name="Data de Início"
    )
    em_andamento = models.BooleanField(
        default=False,
        verbose_name="Em andamento?",
        help_text="Marque esta opção se esta formação ainda não foi concluída."
    )
    data_fim = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de Fim (ou Previsão)",
        help_text="Deixe em branco ou use uma data futura se estiver em andamento."
    )

    def clean(self):
        """
        Validação atualizada:
        - Se a formação NÃO está em andamento, a data de fim é obrigatória.
        """
        super().clean()
        if not self.em_andamento and not self.data_fim:
             raise ValidationError(
                {'data_fim': "Se esta formação não está em andamento, você precisa preencher o campo 'Data de Fim'."}
            )

    class Meta:
        verbose_name = "Formação Acadêmica"
        verbose_name_plural = "Formações Acadêmicas"

    def __str__(self):
        return f"{self.grau} em {self.curso} - {self.instituicao}"