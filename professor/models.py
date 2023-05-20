from django.db import models



class Curso(models.Model):
    curso = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.curso


class Faculdade(models.Model):
    faculdade = models.CharField(max_length=1, blank=False, null=False)

    def __str__(self):
        return self.faculdade

class Período(models.Model):
    periodo = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.periodo


class Professor(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,)
    faculdade = models.ForeignKey(Faculdade,on_delete=models.CASCADE,)
    periodo = models.ForeignKey(Período,on_delete=models.CASCADE,)


    def __str__(self):
        return self.nome