from django import forms
from polls.models import pergunta
# Create your forms here.

class CadastroForm(forms.ModelForm):
    class Meta:
        model = pergunta
        fields = ['nome', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

class LoginForm(forms.Form): # O login continua sendo um Form simples
    nome = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput())