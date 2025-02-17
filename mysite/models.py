from django.db import models
from django.contrib.auth.models import User

class Modelo(models.Model):
    TYPE_CHOICES = [
        (1, 'Público'),
        (2, 'Privado')
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = value = models.TextField()
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    date_inclusion = models.DateTimeField(auto_now_add=True)
    user_inclusion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'modelo'
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return self.name
    
class ModeloVestigio(models.Model):
    TYPE_CHOICES = [
        (1, 'Público'),
        (2, 'Privado')
    ]
    
    TYPE_VESTIGIO_CHOICES = [
        (1, 'Armamento'),
        (2, 'Arquivo Digital'),
        (3, 'Dispositivo Tecnológico'),
        (4, 'Documento'),
        (5, 'Impressão Papiloscópica'),
        (6, 'Material'),
        (7, 'Objeto'),
        (8, 'Veículo')
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = value = models.TextField()
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    type_vestigio = models.PositiveSmallIntegerField(choices=TYPE_VESTIGIO_CHOICES, default=1)
    date_inclusion = models.DateTimeField(auto_now_add=True)
    user_inclusion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'modelo_vestigio'
        verbose_name = 'Modelo Vestigio'
        verbose_name_plural = 'Modelos Vestigios'

    def __str__(self):
        return self.name
    
class Variavel(models.Model):
    TIPO_CHOICES = [
        (0, 'Geral'),
        (1, 'Armamento'),
        (2, 'Arquivo Digital'),
        (3, 'Dispositivo Tecnológico'),
        (4, 'Documento'),
        (5, 'Impressão Papiloscópica'),
        (6, 'Material'),
        (7, 'Objeto'),
        (8, 'Veículo')
    ]

    id = models.AutoField(primary_key=True)
    variavel = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)

    class Meta:
        db_table = 'variaveis'
        verbose_name = 'Variável'
        verbose_name_plural = 'Variáveis'

    def __str__(self):
        return f"{self.variavel} ({self.get_tipo_display()})"

class Chamado(models.Model):
    RESPONSAVEL_CHOICES = [
        (1, 'Cliente'),
        (2, 'Admin'),
    ]

    STATUS_CHOICES = [
        (1, 'Aberto'),
        (2, 'Em Andamento'),
        (3, 'Finalizado'),
    ]

    URGENCIA_CHOICES = [
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    ]

    id = models.AutoField(primary_key=True)
    assunto = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    responsavel = models.PositiveSmallIntegerField(choices=RESPONSAVEL_CHOICES, default=2)
    urgencia = models.PositiveSmallIntegerField(choices=URGENCIA_CHOICES, default=2)
    date_inclusion = models.DateTimeField(auto_now_add=True)
    user_inclusion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'chamados'
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'

    def __str__(self):
        return f"{self.assunto} ({self.get_status_display()})"

class RespostaChamado(models.Model):
    id = models.AutoField(primary_key=True)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name="respostas")
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    mensagem = models.TextField()
    date_inclusion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'respostas_chamados'
        verbose_name = 'Resposta de Chamado'
        verbose_name_plural = 'Respostas de Chamados'

    def __str__(self):
        return f"Resposta de {self.autor.username if self.autor else 'Usuário desconhecido'} em {self.date_inclusion}"

