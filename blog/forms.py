from django import forms  
from .models import Post, Categoria

opcoes = Categoria.objects.all().values_list('name','name')

lista_opcoes = []

for item in opcoes:
    lista_opcoes.append(item)

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post  
        fields = ('title','title_tag','author','category', 'body', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'category': forms.Select(choices=lista_opcoes,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }