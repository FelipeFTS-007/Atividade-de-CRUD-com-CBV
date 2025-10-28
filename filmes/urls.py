# filmes/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', FilmeListView.as_view(), name='filme-list'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='filme-detail'),
    path('filme/novo/', FilmeCreateView.as_view(), name='filme-create'),
    path('filme/<int:pk>/editar/', FilmeUpdateView.as_view(), name='filme-update'),
    path('filme/<int:pk>/deletar/', FilmeDeleteView.as_view(), name='filme-delete'),
]