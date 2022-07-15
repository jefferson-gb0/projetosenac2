from distutils.command.upload import upload
from mailbox import NotEmptyError
from tkinter import Y
from django.db import models

# Create your models herer.
class Departamento(models.Model):
    nome = models.CharField(max_length=20)



    def __str__(self):
        return self.nome 


class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)


    def __str__(self):
        return self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=8000)
    imagens = models.ImageField(upload_to="imagens/")
    estoque = models.IntegerField()
    lancamento = models.BooleanField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__ (self):
        return self.nome 



