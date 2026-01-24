<div align="center">

# 📦 SGE - Sistema de Gestão de Estoque

**Sistema completo de gestão de estoque desenvolvido em Django, com API REST e integração com IA para análise de dados.**

<img src="https://github.com/patresio/sge-django-master/raw/master/.gitassets/capa.png" width="600" alt="SGE Dashboard" />

[![GitHub stars](https://img.shields.io/github/stars/patresio/sge-django-master?style=for-the-badge)](https://github.com/patresio/sge-django-master/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/patresio/sge-django-master?style=for-the-badge)](https://github.com/patresio/sge-django-master/network)
[![GitHub issues](https://img.shields.io/github/issues/patresio/sge-django-master?style=for-the-badge)](https://github.com/patresio/sge-django-master/issues)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

## 📋 Sobre o Projeto

O **SGE (Sistema de Gestão de Estoque)** é uma aplicação web full-stack desenvolvida para **gerenciamento completo de inventário empresarial**. O sistema oferece controle de produtos, movimentações de entrada/saída, gestão de fornecedores e análises inteligentes através de integração com IA.

### 🎯 Objetivo

Este projeto foi desenvolvido para demonstrar proficiência em:

- Desenvolvimento backend com **Django** e boas práticas de arquitetura
- Criação de **APIs RESTful** com Django REST Framework
- Modelagem de dados relacionais com **PostgreSQL**
- Integração com serviços de **Inteligência Artificial (Gemini)**
- Containerização com **Docker**
- Autenticação e autorização de usuários

---

## ✨ Funcionalidades

### 🏢 Gestão de Cadastros
| Módulo | Descrição |
|--------|-----------|
| **Produtos** | CRUD completo com preço de custo, preço de venda, número de série e quantidade |
| **Categorias** | Organização hierárquica de produtos |
| **Marcas** | Gestão de fabricantes e marcas |
| **Fornecedores** | Cadastro de fornecedores com dados de contato |

### 📊 Controle de Estoque
| Funcionalidade | Descrição |
|----------------|-----------|
| **Entradas (Inflows)** | Registro de compras com vínculo a fornecedor e produto |
| **Saídas (Outflows)** | Registro de vendas/baixas com atualização automática de quantidade |
| **Rastreabilidade** | Histórico completo de movimentações com timestamps |

### 📈 Dashboard & Analytics
- **Métricas de produtos**: total, valor em estoque, por categoria
- **Métricas de vendas**: faturamento diário, quantidade vendida
- **Gráficos interativos**: distribuição por categoria e marca
- **Análise por IA**: insights gerados pelo Google Gemini

### 🔌 API REST
API completa com endpoints para todas as entidades:

```
GET/POST   /api/products/
GET/DELETE /api/products/<id>/
GET/POST   /api/brands/
GET/POST   /api/categories/
GET/POST   /api/suppliers/
GET/POST   /api/inflows/
GET/POST   /api/outflows/
```

---

## 🏗️ Arquitetura

```
sge-django-master/
├── core/               # Configurações do Django (settings, urls, wsgi)
├── authentication/     # Sistema de autenticação de usuários
├── dashboard/          # Dashboard principal com métricas e gráficos
├── products/           # CRUD de Produtos
├── brands/             # CRUD de Marcas
├── categories/         # CRUD de Categorias
├── suppliers/          # CRUD de Fornecedores
├── inflows/            # Gestão de Entradas de Estoque
├── outflows/           # Gestão de Saídas de Estoque
├── api/                # Endpoints REST (Django REST Framework)
├── ai/                 # Integração com Google Gemini AI
├── templates/          # Templates HTML (Bootstrap)
├── utils/              # Funções auxiliares e métricas
└── services/           # Camada de serviços externos
```

### 📦 Principais Dependências

| Pacote | Função |
|--------|--------|
| `django` | Framework web principal |
| `djangorestframework` | API REST |
| `djangorestframework-simplejwt` | Autenticação JWT para API |
| `google-generativeai` | Integração com Gemini AI |
| `python-decouple` | Gerenciamento de variáveis de ambiente |
| `dj-database-url` | Configuração de banco via URL |
| `dj-static` | Servir arquivos estáticos |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10+
- PostgreSQL (ou SQLite para desenvolvimento)
- Docker & Docker Compose (opcional)

### 🐳 Com Docker (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/patresio/sge-django-master.git
cd sge-django-master

# Execute com Docker Compose
docker-compose up -d
```

### 🐍 Instalação Manual

```bash
# Clone o repositório
git clone https://github.com/patresio/sge-django-master.git
cd sge-django-master

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env  # Configure suas credenciais

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse: **http://localhost:8000**

---

## 📸 Screenshots

<div align="center">

![Dashboard](https://github.com/patresio/sge-django-master/raw/master/.gitassets/2.jpg)
*Dashboard com métricas e gráficos*

</div>

---

## 🛠️ Tecnologias Utilizadas

<table>
<tr>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python" />
<br>Python
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="48" height="48" alt="Django" />
<br>Django
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="48" height="48" alt="PostgreSQL" />
<br>PostgreSQL
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="48" height="48" alt="Docker" />
<br>Docker
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="48" height="48" alt="Bootstrap" />
<br>Bootstrap
</td>
</tr>
</table>

---

## 📚 Documentação Adicional

- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Google Gemini API](https://ai.google.dev/docs)

---

## 📄 Licença

Este projeto foi desenvolvido para fins didáticos e de demonstração de habilidades técnicas.

---

## 👤 Autor

Desenvolvido por **[@patresio](https://github.com/patresio)**

<div align="center">

⭐ **Se este projeto foi útil, considere dar uma estrela!** ⭐

</div>