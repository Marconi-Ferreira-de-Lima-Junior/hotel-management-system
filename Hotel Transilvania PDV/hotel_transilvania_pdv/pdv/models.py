from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

# ==================== VALIDADORES CUSTOMIZADOS ====================

def validar_cpf(value):
    """Valida o formato do CPF"""
    cpf_pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if not re.match(cpf_pattern, value):
        raise ValidationError('CPF deve estar no formato: 000.000.000-00')

def validar_telefone(value):
    """Valida o formato do telefone"""
    phone_pattern = r'^\(\d{2}\)\d{4,5}-\d{4}$'
    if not re.match(phone_pattern, value):
        raise ValidationError('Telefone deve estar no formato: (99)99999-9999')


# ==================== MODELS ====================

class Cliente(models.Model):
    """Modelo de Cliente do Hotel"""
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    cpf = models.CharField(
        max_length=15, 
        unique=True,
        validators=[validar_cpf],
        verbose_name="CPF",
        help_text="Formato: 000.000.000-00"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    telefone = models.CharField(
        max_length=15, 
        validators=[validar_telefone],
        verbose_name="Telefone",
        help_text="Formato: (99)99999-9999"
    )
    endereco = models.TextField(blank=True, null=True, verbose_name="Endereço")
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.nome} - {self.cpf}"


class Quarto(models.Model):
    """Modelo de Quarto do Hotel"""
    TIPOS_QUARTO = [
        ('SOLTEIRO', 'Solteiro'),
        ('CASAL', 'Casal'),
        ('SUITE', 'Suíte'),
        ('SUITE_LUXO', 'Suíte de Luxo'),
    ]

    numero = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name="Número do Quarto"
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_QUARTO,
        verbose_name="Tipo de Quarto"
    )
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Preço por Noite"
    )
    disponivel = models.BooleanField(default=True, verbose_name="Disponível")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    capacidade = models.IntegerField(default=2, verbose_name="Capacidade de Hóspedes")
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Quarto"
        verbose_name_plural = "Quartos"
        ordering = ['numero']

    def __str__(self):
        return f"Quarto {self.numero} - {self.get_tipo_display()}"
    
    def esta_disponivel(self, data_entrada, data_saida):
        """Verifica a disponibilidade do quarto em um período específico"""
        reservas = Reserva.objects.filter(
            quarto=self,
            data_entrada__lt=data_saida,
            data_saida__gt=data_entrada,
            status__in=['CONFIRMADA', 'ATIVA']
        )
        return not reservas.exists()


class Reserva(models.Model):
    """Modelo de Reserva do Hotel"""
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADA', 'Confirmada'),
        ('ATIVA', 'Ativa'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        related_name='reservas',
        verbose_name="Cliente"
    )
    quarto = models.ForeignKey(
        Quarto, 
        on_delete=models.CASCADE,
        related_name='reservas',
        verbose_name="Quarto"
    )
    data_entrada = models.DateTimeField(verbose_name="Data de Entrada")
    data_saida = models.DateTimeField(verbose_name="Data de Saída")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDENTE',
        verbose_name="Status"
    )
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['-data_entrada']

    def __str__(self):
        return f"Reserva de {self.cliente.nome} no quarto {self.quarto.numero}"
    
    def calcular_valor_total(self):
        """Calcula o valor total da reserva"""
        dias = (self.data_saida - self.data_entrada).days
        if dias <= 0:
            dias = 1
        return dias * self.quarto.preco
    
    def clean(self):
        """Validações customizadas"""
        if self.data_saida <= self.data_entrada:
            raise ValidationError({
                'data_saida': 'A data de saída deve ser posterior à data de entrada.'
            })
        
        if self.data_entrada < timezone.now():
            raise ValidationError({
                'data_entrada': 'A data de entrada não pode ser no passado.'
            })
        
        if not self.quarto.esta_disponivel(self.data_entrada, self.data_saida):
            raise ValidationError({
                'quarto': 'Este quarto não está disponível no período solicitado.'
            })


class Despesa(models.Model):
    """Modelo de Despesa do Hotel"""
    CATEGORIAS = [
        ('LIMPEZA', 'Limpeza'),
        ('MANUTENCAO', 'Manutenção'),
        ('ALIMENTACAO', 'Alimentação'),
        ('UTILITARIOS', 'Utilitários'),
        ('FOLHA', 'Folha de Pagamento'),
        ('OUTROS', 'Outros'),
    ]

    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='OUTROS',
        verbose_name="Categoria"
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Valor"
    )
    data = models.DateField(verbose_name="Data da Despesa")
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"
        ordering = ['-data']

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"


class Receita(models.Model):
    """Modelo de Receita do Hotel"""
    ORIGEM_CHOICES = [
        ('RESERVA', 'Reserva'),
        ('SERVICO', 'Serviço Adicional'),
        ('EVENTO', 'Evento'),
        ('OUTROS', 'Outros'),
    ]

    reserva = models.ForeignKey(
        Reserva, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='receitas',
        verbose_name="Reserva"
    )
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    origem = models.CharField(
        max_length=20,
        choices=ORIGEM_CHOICES,
        default='OUTROS',
        verbose_name="Origem"
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Valor"
    )
    data = models.DateField(verbose_name="Data da Receita")
    pago = models.BooleanField(default=False, verbose_name="Pago")
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-data']

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

