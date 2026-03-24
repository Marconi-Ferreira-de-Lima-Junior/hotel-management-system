# 🎯 COMECE AGORA EM 3 PASSOS

## 🪟 USUÁRIOS WINDOWS (Mais Fácil!)

### PASSO 1️⃣: Localize a Pasta
```
📁 C:\Users\marco\OneDrive\Área de Trabalho\Hotel_pdv
       └─ 📁 Hotel Transilvania PDV
              └─ 📁 hotel_transilvania_pdv  ← ENTRE AQUI
```

### PASSO 2️⃣: Encontre o Arquivo
```
📁 Dentro de hotel_transilvania_pdv, procure:

  📄 run.bat        ← 👈 ESTE AQUI!
  
Outros arquivos:
  📄 run.py
  📄 run.ps1
  📄 run.sh
  📄 manage.py
```

### PASSO 3️⃣: Clique 2 Vezes! 🖱️🖱️
```
DUPLO CLIQUE em run.bat

Pronto! O sistema vai:
  ✅ Preparar o banco de dados
  ✅ Carregar os arquivos
  ✅ Abrir o navegador
  ✅ Ir direto para o login
```

---

## 💻 USUÁRIOS TERMINAL / COMMAND PROMPT

### Windows CMD
```cmd
cd "C:\Users\marco\OneDrive\Área de Trabalho\Hotel_pdv\Hotel Transilvania PDV\hotel_transilvania_pdv"
run.bat
```

### Windows PowerShell
```powershell
cd "C:\Users\marco\OneDrive\Área de Trabalho\Hotel_pdv\Hotel Transilvania PDV\hotel_transilvania_pdv"
.\run.ps1
```

### Linux/Mac Terminal
```bash
cd ~/Desktop/Hotel_pdv/Hotel\ Transilvania\ PDV/hotel_transilvania_pdv
chmod +x run.sh
./run.sh
```

---

## 📺 O QUE VOCÊ VERÁ

### 1. Terminal Executando:
```
╔════════════════════════════════════════════════════════════════╗
║         🏰 HOTEL TRANSILVÂNIA PDV - Sistema de Login 🏰        ║
║                   Inicializador Automático v2.0                 ║
╚════════════════════════════════════════════════════════════════╝

ℹ️  Verificando ambiente...
✅ Python 3.9.0 encontrado

ℹ️  Executando migrações do banco de dados...
✅ Migrações completadas

ℹ️  Coletando arquivos estáticos...
✅ Arquivos estáticos coletados

ℹ️  Aguardando inicialização...
✅ Abrindo navegador...

╔════════════════════════════════════════════════════════════════╗
║           🚀 Servidor rodando em http://127.0.0.1:8000        ║
║               🛑 Pressione Ctrl+C para parar                   ║
╚════════════════════════════════════════════════════════════════╝
```

### 2. Navegador Abrindo:
```
http://127.0.0.1:8000/login/
```

### 3. Página de Login:
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│              🏰 Hotel Transilvânia                   │
│         Sistema de Gerenciamento de PDV             │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │ 👤 Usuário:                                    │ │
│  │ [Digite seu nome de usuário]                   │ │
│  │                                                 │ │
│  │ 🔐 Senha:                                      │ │
│  │ [Digite sua senha]                             │ │
│  │                                                 │ │
│  │             [🔓 Acessar Sistema]               │ │
│  │                                                 │ │
│  │ Ainda não tem uma conta?                       │ │
│  │           Registre-se aqui 👈                  │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## ✨ PRIMEIRA VEZ? CRIE SUA CONTA

### Clique em "Registre-se aqui"
```
Você será levado para:
  http://127.0.0.1:8000/register/
```

### Crie Sua Conta
```
┌─────────────────────────────────────┐
│      🏰 Criar Conta                 │
│ Registre-se no Sistema               │
│                                     │
│ 👤 Nome de Usuário:                 │
│ [seu_usuario_aqui]                  │
│                                     │
│ 📧 Email:                           │
│ [seu.email@exemplo.com]             │
│                                     │
│ 🔐 Senha:                           │
│ [minimo 6 caracteres]               │
│                                     │
│ 🔐 Confirmar Senha:                 │
│ [repita a senha]                    │
│                                     │
│       [✅ Criar Conta]              │
│                                     │
│ Já tem uma conta?                   │
│       Faça login aqui 👈            │
└─────────────────────────────────────┘
```

### Pronto! 🎉
Após criar a conta, você voltará para o login. Use suas novas credenciais!

---

## 🎯 FLUXO VISUAL

```
                    INÍCIO
                      ↓
        ┌─────────────────────────┐
        │  Executar Inicializador │
        │  (duplo clique / CMD)   │
        └──────────┬──────────────┘
                   ↓
        ┌──────────────────────────┐
        │ Banco de Dados           │
        │ ✅ Migrações prontas     │
        └──────────┬───────────────┘
                   ↓
        ┌──────────────────────────┐
        │ Arquivos Estáticos       │
        │ ✅ CSS e JS carregados   │
        └──────────┬───────────────┘
                   ↓
        ┌──────────────────────────┐
        │ Navegador                │
        │ ✅ Abrindo automaticamente
        └──────────┬───────────────┘
                   ↓
        ┌──────────────────────────────┐
        │ Página de Login              │
        │ http://127.0.0.1:8000/login/ │
        └──────────┬────────────────────┘
                   ↓
           ┌───────┴────────┐
           ↓                 ↓
        ✅ Faz login    ❌ Primeiro acesso
           │                 │
           │                 ↓
           │      [Registre-se aqui]
           │                 │
           │                 ↓
           │      Cria nova conta
           │                 │
           └────────┬────────┘
                    ↓
            🎉 SISTEMA PRONTO!
```

---

## ⚡ ATALHOS ÚTEIS

### Para Parar o Servidor
```
Pressione: Ctrl + C
```

### Para Retomar
```
Execute o inicializador novamente
```

### Acessar Admin Django
```
http://127.0.0.1:8000/admin/
(Use as mesmas credenciais de login)
```

### Modificar Configurações
```
Arquivo: hotel_transilvania_pdv/settings.py
Bus na linha: ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

---

## ❓ PERGUNTAS FREQUENTES

### P: O script não funciona
**R:** Certifique-se de:
- Estar na pasta `hotel_transilvania_pdv/`
- Python estar instalado: `python --version`
- Ambiente virtual existir: veja se existe pasta `venv/`

### P: Navegador não abre
**R:** Acesse manualmente:
```
http://127.0.0.1:8000/login/
```

### P: Esqueci a senha
**R:** Você precisa criar uma nova conta
*Nota: Este é um banco de dados local, não há recuperação*

### P: Quero mudar a porta
**R:** Use:
```
python manage.py runserver 8001
```

### P: Sistema está muito lento
**R:** Isso é normal em desenvolvimento. Aguarde.

---

## 📖 DOCUMENTAÇÃO COMPLETA

Se precisar de mais informações:

- **GUIA_RAPIDO.md** - Instruções detalhadas
- **EXECUTORES.md** - Como funcionam os scripts
- **README.md** - Documentação completa do projeto
- **CHANGELOG.md** - Histórico de mudanças

---

## 🆘 PROBLEMAS?

### Terminal mostra erro
Leia a mensagem de erro e procure em:
- GUIA_RAPIDO.md (seção "Solução de Problemas")
- Este arquivo (seção "Perguntas Frequentes")

### Sistema não inicia
1. Feche o navegador
2. Finalize o terminal
3. Tente novamente
4. Se persistir, reinstale `venv`: `python -m venv venv`

---

## 🎓 PRÓXIMO PASSO

Após fazer login:
1. ✅ Você será redirecionado ao Dashboard
2. ✅ Clique em "Clientes" para começar
3. ✅ Explore os menus disponíveis

---

## 🏆 BOM LUCK! 

Você agora tem um **sistema profissional de gerenciamento de hotel** executando localmente!

Se tiver dúvidas, revise este documento ou a documentação completa.

---

**Hotel Transilvânia PDV v2.0**  
**Seu sistema de gestão está pronto para usar! 🏰✨**
