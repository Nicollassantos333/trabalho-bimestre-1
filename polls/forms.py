from django import forms
# Create your forms here.


class pergunta(forms.Form):
    nome = forms.CharField(label="Insira seu nome", max_length=20)
    email = forms.EmailField(label="Insira seu endereço de Email", max_length=250)
    senha = forms.CharField(label="Insira sua senha", max_length=20)
