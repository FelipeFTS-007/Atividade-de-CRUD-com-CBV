# filmes/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Filme

class FilmeListView(ListView):
    model = Filme
    template_name = 'filmes/listar.html'
    context_object_name = 'filmes'
    ordering = ['titulo']

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filmes/detalhe.html'
    context_object_name = 'filme'

class FilmeCreateView(CreateView):
    model = Filme
    template_name = 'filmes/form.html'
    fields = ['titulo', 'diretor', 'ano_lancamento', 'genero', 'duracao', 'sinopse', 'capa']
    success_url = reverse_lazy('filme-list')

class FilmeUpdateView(UpdateView):
    model = Filme
    template_name = 'filmes/form.html'
    fields = ['titulo', 'diretor', 'ano_lancamento', 'genero', 'duracao', 'sinopse', 'capa']
    success_url = reverse_lazy('filme-list')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filmes/confirm_delete.html'
    success_url = reverse_lazy('filme-list')
    context_object_name = 'filme'