# filmes/models.py
from django.db import models
from django.urls import reverse

class Filme(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    diretor = models.CharField(max_length=100, verbose_name="Diretor")
    ano_lancamento = models.IntegerField(verbose_name="Ano de Lançamento")
    genero = models.CharField(max_length=50, verbose_name="Gênero")
    duracao = models.IntegerField(verbose_name="Duração (minutos)")
    sinopse = models.TextField(verbose_name="Sinopse", blank=True)
    capa = models.ImageField(
        upload_to='capas_filmes/',
        verbose_name="Capa do Filme",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('filme-detail', kwargs={'pk': self.pk})