# 🚀 GUIA RÁPIDO - Hotel Transilvânia PDV

## ⚡ Iniciar em 1 Clique (Windows)

### Método 1️⃣: Duplo Clique (Mais Fácil)
```
📁 hotel_transilvania_pdv/
   ├── run.bat           ← 👈 DUPLO CLIQUE AQUI!
   ├── run.ps1
   ├── run.py
   └── manage.py
```

**Passos:**
1. Abra a pasta `hotel_transilvania_pdv`
2. Procure pelo arquivo `run.bat`
3. 👉 **Clique 2 vezes** e pronto! 🎉

---

### Método 2️⃣: PowerShell Moderno
```powershell
# Abra o PowerShell e execute:
cd "C:\Users\marco\OneDrive\Área de Trabalho\Hotel_pdv\Hotel Transilvania PDV\hotel_transilvania_pdv"
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
.\run.ps1
```

---

### Método 3️⃣: CMD Tradicional
```cmd
cd "C:\Users\marco\OneDrive\Área de Trabalho\Hotel_pdv\Hotel Transilvania PDV\hotel_transilvania_pdv"
run.bat
```

---

## 🐧 Iniciar no Linux/Mac

### Via Terminal
```bash
cd ~/Desktop/Hotel_pdv/Hotel\ Transilvania\ PDV/hotel_transilvania_pdv
chmod +x run.sh
./run.sh
```

---

## 🎯 Resultado Esperado

Quando você executar qualquer um dos scripts:

```
╔════════════════════════════════════════════════════════════════╗
║         🏰 HOTEL TRANSILVÂNIA PDV - Sistema de Login 🏰        ║
║                   Inicializador Automático v2.0                 ║
╚════════════════════════════════════════════════════════════════╝

ℹ️  Verificando ambiente...
✅ Python encontrado

ℹ️  Ativando ambiente virtual...
✅ Ambiente virtual ativado

ℹ️  Executando migrações do banco de dados...
✅ Migrações completadas

ℹ️  Coletando arquivos estáticos...
✅ Arquivos estáticos coletados

✅ Abrindo navegador...

╔════════════════════════════════════════════════════════════════╗
║           🚀 Servidor rodando em http://127.0.0.1:8000        ║
║               🛑 Pressione Ctrl+C para parar                   ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 🔐 Página de Login (Automática)

O navegador abre automaticamente em:
```
http://127.0.0.1:8000/login/
```

**Tela que você verá:**

```
        🏰 Hotel Transilvânia
    Sistema de Gerenciamento de PDV

┌─────────────────────────────────────┐
│ 👤 Usuário:                         │
│ [Digite seu nome de usuário]        │
│                                     │
│ 🔐 Senha:                           │
│ [Digite sua senha]                  │
│                                     │
│        [🔓 Acessar Sistema]         │
│                                     │
│ Ainda não tem uma conta?            │
│    👉 Registre-se aqui 👈           │
└─────────────────────────────────────┘
```

---

## 📝 Primeira Vez? Crie Sua Conta!

### Passo 1: Clique em "Registre-se aqui"
Você será redirecionado para a página de registro

### Passo 2: Preencha os Dados
```
🏰 Criar Conta
Registre-se no Sistema de Gerenciamento

┌─────────────────────────────────────┐
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
│        [✅ Criar Conta]             │
│                                     │
│ Já tem uma conta?                   │
│    👉 Faça login aqui 👈            │
└─────────────────────────────────────┘
```

### Passo 3: Pronto!
Após criar a conta, você será redirecionado para login. Use as credenciais que acabou de criar.

---

## ✨ Características do Sistema

| Item | Status |
|------|--------|
| Página de Login | ✅ Automática |
| Botão de Registro | ✅ Disponível |
| Tema Vampiresco | ✅ Roxo + Ouro |
| Responsividade Mobile | ✅ Sim |
| Validação de Formulários | ✅ Sim |
| Segurança | ✅ CSRF Protection |

---

## 🛠️ Scripts Disponíveis

| Script | Sistema | Como Usar |
|--------|---------|-----------|
| `run.bat` | Windows | Duplo clique |
| `run.ps1` | Windows PowerShell | `.\run.ps1` |
| `run.py` | Qualquer | `python run.py` |
| `run.sh` | Linux/Mac | `./run.sh` |

---

## ⚙️ Configuração (Opcional)

Se precisar mudar a porta ou outras configurações:

**settings.py** - Configurações do Django
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Seus hostnames
DEBUG = True  # False em produção
```

**.env** - Variáveis de ambiente
```
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🆘 Problemas Comuns

### "O arquivo não foi encontrado"
- Certifique-se de estar na pasta correta: `hotel_transilvania_pdv/`
- Use o caminho completo se necessário

### "Python não está instalado"
- Baixe em: https://www.python.org/downloads/
- Na instalação, marque: ✅ "Add Python to PATH"

### "Porta 8000 já está em uso"
- Aguarde 30 segundos e tente novamente
- Ou execute: `python manage.py runserver 8001`

### "Navegador não abre"
- Acesse manualmente: `http://127.0.0.1:8000/login/`

---

## 📞 Suporte

Para mais informações, veja:
- [README.md](README.md) - Documentação completa
- [CHANGELOG.md](CHANGELOG.md) - Histórico de mudanças
- [EXECUTORES.md](EXECUTORES.md) - Detalhes técnicos

---

**Hotel Transilvânia PDV v2.0**  
**Desenvolvido com ❤️ para Fuctura**
