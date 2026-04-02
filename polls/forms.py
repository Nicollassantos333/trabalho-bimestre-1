from django import forms
# Create your forms here.


class pergunta(forms.Form):
    nome = forms.CharField(verbose_name="Insira seu nome", max_length=20)
    email = forms.EmailField(verbose_name="Insira seu endereço de Email", max_length=250)
    telefone = forms.CharField(verbose_name="Insira seu número de telefone", max_length=20)
