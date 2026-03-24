# 🏰 Hotel Transilvânia PDV

Um sistema profissional de gerenciamento de ponto de venda (PDV) para hotéis, desenvolvido com **Django** e **HTML/CSS** personalizado.

## ✨ Características

- ✅ **Gerenciamento de Clientes** - Cadastro e informações detalhadas
- ✅ **Sistema de Reservas** - Controle de datas e disponibilidade
- ✅ **Gestão de Quartos** - Múltiplos tipos com preços configuráveis
- ✅ **Controle Financeiro** - Despesas e receitas
- ✅ **Dashboard** - Estatísticas em tempo real
- ✅ **Autenticação Segura** - Login e registro de usuários
- ✅ **Design Responsivo** - Tema profissional vampiresco

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- pip
- Virtual Environment (venv)

### Passo a Passo

1. **Clone ou navegue até o projeto:**
```bash
cd "Hotel Transilvania PDV"
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente:**
   - Copie `.env` e configure a `SECRET_KEY` (já fornecido)
   - Ajuste `DEBUG=True` para desenvolvimento

6. **Execute as migrações:**
```bash
cd hotel_transilvania_pdv
python manage.py migrate
```

7. **Crie um superusuário (admin):**
```bash
python manage.py createsuperuser
```

8. **Inicie o servidor:**
```bash
python manage.py runserver
```

9. **Acesse no navegador:**
   - Sistema: `http://127.0.0.1:8000`
   - Admin: `http://127.0.0.1:8000/admin`

## 📁 Estrutura do Projeto

```
Hotel Transilvania PDV/
├── hotel_transilvania_pdv/          # Projeto Django
│   ├── hotel_transilvania_pdv/       # Configurações
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── pdv/                        # Aplicação principal
│   │   ├── models.py               # Modelos de banco de dados
│   │   ├── views.py                # Lógica da aplicação
│   │   ├── forms.py                # Formulários
│   │   ├── urls.py                 # URLs
│   │   ├── static/                 # CSS e arquivos estáticos
│   │   │   ├── globals/style.css
│   │   │   └── login/login.css
│   │   └── templates/pdv/          # Templates HTML
│   ├── db.sqlite3                  # Banco de dados
│   └── manage.py
├── venv/                           # Ambiente virtual
├── .env                            # Variáveis de ambiente
├── requirements.txt                # Dependências Python
└── README.md                       # Este arquivo
```

## 🎨 Paleta de Cores Temática

- **Roxo Escuro:** `#4a1a40` (Primário)
- **Ouro Medieval:** `#d4af37` (Secundário)
- **Preto Vampiresco:** `#1a1a1a` (Background)
- **Marrom Vampiresco:** `#8b4513` (Accent)

## 🔐 Segurança

- ✅ SECRET_KEY protegida em arquivo `.env`
- ✅ DEBUG desativado em produção
- ✅ CSRF protection habilitado
- ✅ Autenticação obrigatória para acesso
- ✅ Validações de entrada personalizadas

## 📊 Modelos de Dados

### Cliente
- Nome, CPF, Email, Telefone, Endereço
- Validação de CPF e telefone
- Histórico de criação e atualização

### Quarto
- Número único, tipo, preço, capacidade
- Status de disponibilidade
- Sistema inteligente de verificação de conflitos

### Reserva
- Cliente, Quarto, Datas
- Status (Pendente, Confirmada, Ativa, Concluída, Cancelada)
- Cálculo automático de valor total
- Validações de data e disponibilidade

### Despesa
- Descrição, Categoria, Valor, Data
- Categorias: Limpeza, Manutenção, Alimentação, etc.

### Receita
- Descrição, Origem, Valor, Data
- Ligação com Reservas
- Status de pagamento

## 🛠️ APIs e Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/login/` | Página de login |
| POST | `/login/` | Autenticar usuário |
| GET | `/register/` | Página de registro |
| POST | `/register/` | Criar nova conta |
| GET | `/dashboard/` | Dashboard principal |
| GET | `/clientes/` | Listar clientes |
| POST | `/cadastrar-cliente/` | Criar cliente |
| GET | `/quartos/` | Listar quartos |
| GET | `/reservas/` | Listar reservas |

## 📝 Uso

### Acessar o Sistema
1. Acesse `http://127.0.0.1:8000`
2. Faça login com suas credenciais
3. Navegue pelos menus principais

### Cadastrar Cliente
1. Clique em "Clientes" na navbar
2. Clique em "Cadastrar Cliente"
3. Preencha os dados no formato correto:
   - CPF: `000.000.000-00`
   - Telefone: `(99)99999-9999`
4. Clique em "Salvar"

### Criar Reserva
1. Clique em "Reservas" na navbar
2. Clique em "Nova Reserva"
3. Selecione Cliente e Quarto
4. Escolha as datas de entrada e saída
5. Confirme a disponibilidade
6. Clique em "Confirmar Reserva"

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
**Solução:** Certifique-se de que o ambiente virtual está ativado e as dependências estão instaladas:
```bash
pip install -r requirements.txt
```

### Erro: "No such table"
**Solução:** Execute as migrações:
```bash
python manage.py migrate
```

### Erro: "Forbidden (403)"
**Solução:** Adicione seu domínio em `ALLOWED_HOSTS` no `settings.py`

## 👨‍💻 Desenvolvimento

### Criar novas migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### Coletar arquivos estáticos
```bash
python manage.py collectstatic
```

### Executar testes
```bash
python manage.py test
```

## 📦 Dependências Principais

- **Django 5.1.6** - Framework web
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **Pillow** - Processamento de imagens
- **gunicorn** - Servidor WSGI para produção


## ✉️ Suporte

Para dúvidas ou sugestões, entre em contato com seu instrutor.

---

**Desenvolvido com ❤️ para Fuctura | Disciplina: Django | Professor(a): Jéssica Andrade**
