# 🎬 Catálogo de Filmes - Sistema Django com Class-Based Views

Sistema web completo desenvolvido em Django utilizando Class-Based Views (CBV) para gerenciamento de um catálogo de filmes. O projeto implementa operações CRUD completas com interface moderna e responsiva.

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Rotas e URLs](#-rotas-e-urls)
- [Models e Banco de Dados](#-models-e-banco-de-dados)
- [Class-Based Views](#-class-based-views)
- [Templates](#-templates)
- [Upload de Imagens](#-upload-de-imagens)
- [Executando o Projeto](#-executando-o-projeto)
- [Capturas de Tela](#-capturas-de-tela)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🚀 Funcionalidades

### ✅ CRUD Completo
- **Create**: Adicionar novos filmes com formulário validado
- **Read**: Listar e visualizar detalhes dos filmes
- **Update**: Editar informações dos filmes existentes
- **Delete**: Remover filmes com confirmação

### 🎨 Interface
- Design responsivo com Bootstrap 5
- Layout moderno e intuitivo
- Upload e exibição de capas dos filmes
- Navegação simplificada entre páginas
- Mensagens de estado vazio

### 📊 Gestão de Dados
- 7 campos por filme (incluindo imagem)
- Ordenação automática por título
- Validação de dados nos formulários
- Armazenamento seguro de arquivos de mídia

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 4.2**: Framework web principal
- **Python 3.8+**: Linguagem de programação
- **Pillow**: Processamento de imagens
- **SQLite**: Banco de dados (desenvolvimento)

### Frontend
- **Bootstrap 5**: Framework CSS
- **HTML5**: Estrutura das páginas
- **CSS3**: Estilos customizados
- **Font Awesome**: Ícones (CDN)

### Ferramentas
- **Git**: Controle de versão
- **GitHub**: Hospedagem do código
- **PIP**: Gerenciamento de pacotes

## 📁 Estrutura do Projeto
catalogo_filmes/
├── catalogo_filmes/ # Configurações do projeto
│ ├── init.py
│ ├── settings.py # Configurações Django
│ ├── urls.py # URLs principais
│ └── wsgi.py
├── filmes/ # Aplicação principal
│ ├── migrations/ # Migrações do banco
│ ├── templates/filmes/ # Templates HTML
│ │ ├── base.html
│ │ ├── listar.html
│ │ ├── detalhe.html
│ │ ├── form.html
│ │ └── confirm_delete.html
│ ├── init.py
│ ├── admin.py # Configuração admin
│ ├── apps.py
│ ├── models.py # Model Filme
│ ├── tests.py
│ ├── urls.py # URLs do app
│ └── views.py # Class-Based Views
├── media/ # Arquivos uploadados
│ └── capas_filmes/ # Capas dos filmes
├── static/ # Arquivos estáticos
├── manage.py
├── requirements.txt
└── README.md


## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- PIP (Gerenciador de pacotes Python)
- Git (para clone do repositório)
- Navegador web moderno

## 🎯 Como Executar

1. Clone o repositório
2. Instale as dependências: `pip install django`
3. Execute as migrações: `python manage.py migrate`
4. Inicie o servidor: `python manage.py runserver`
5. Acesse: `http://localhost:8000`

