from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    num_pilotos = models.IntegerField()
    dt_criacao = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.nome

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    num_carro = models.IntegerField()
    idade = models.IntegerField()
    #nome_equipe = models.CharField(max_length=100)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Pilotos'

    def __str__(self):
        return self.nome
# Create your models here.
