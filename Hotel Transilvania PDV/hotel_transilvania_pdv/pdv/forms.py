from django import forms
from .models import Cliente, Reserva, Quarto, Despesa, Receita
from django.contrib.auth.models import User

# ==================== WIDGETS CUSTOMIZADOS ====================

class FormFieldMixin:
    """Mixin para adicionar classes CSS aos campos de formulário"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'rows': '4'
                })
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


# ==================== FORMULÁRIOS ====================

class ClienteForm(FormFieldMixin, forms.ModelForm):
    """Formulário para criar e editar clientes"""
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome completo',
                'class': 'form-control'
            }),
            'cpf': forms.TextInput(attrs={
                'placeholder': '000.000.000-00',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@exemplo.com',
                'class': 'form-control'
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': '(99)99999-9999',
                'class': 'form-control'
            }),
            'endereco': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Digite o endereço completo'
            }),
        }


class ReservaForm(FormFieldMixin, forms.ModelForm):
    """Formulário para criar e editar reservas"""
    class Meta:
        model = Reserva
        fields = ['cliente', 'quarto', 'data_entrada', 'data_saida', 'status', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'quarto': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'data_saida': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Digite observações adicionais (opcional)'
            }),
        }


class QuartoForm(FormFieldMixin, forms.ModelForm):
    """Formulário para criar e editar quartos"""
    class Meta:
        model = Quarto
        fields = ['numero', 'tipo', 'preco', 'disponivel', 'descricao', 'capacidade']
        widgets = {
            'numero': forms.TextInput(attrs={
                'placeholder': 'Ex: 101',
                'class': 'form-control'
            }),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'form-control',
                'step': '0.01'
            }),
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Descrição do quarto (opcional)'
            }),
            'capacidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
        }


class DespesaForm(FormFieldMixin, forms.ModelForm):
    """Formulário para criar e editar despesas"""
    class Meta:
        model = Despesa
        fields = ['descricao', 'categoria', 'valor', 'data']
        widgets = {
            'descricao': forms.TextInput(attrs={
                'placeholder': 'Descrição da despesa',
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'form-control',
                'step': '0.01'
            }),
            'data': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }


class ReceitaForm(FormFieldMixin, forms.ModelForm):
    """Formulário para criar e editar receitas"""
    class Meta:
        model = Receita
        fields = ['reserva', 'descricao', 'origem', 'valor', 'data', 'pago']
        widgets = {
            'reserva': forms.Select(attrs={
                'class': 'form-control',
                'required': False
            }),
            'descricao': forms.TextInput(attrs={
                'placeholder': 'Descrição da receita',
                'class': 'form-control'
            }),
            'origem': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'form-control',
                'step': '0.01'
            }),
            'data': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class UserRegistrationForm(forms.ModelForm):
    """Formulário para registro de novos usuários"""
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )
    password_confirm = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu.email@exemplo.com'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("❌ As senhas não coincidem. Tente novamente.")
            if len(password) < 6:
                raise forms.ValidationError("❌ A senha deve ter no mínimo 6 caracteres.")

        return cleaned_data
