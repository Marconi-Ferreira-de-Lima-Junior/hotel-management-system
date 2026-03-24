# 🏰 EXECUTORES DO HOTEL TRANSILVÂNIA PDV

## ⚡ Como Usar os Scripts de Inicialização

O projeto possui três scripts para iniciar o sistema automaticamente na página de login:

### 🪟 Windows

**Opção 1: Clique duplo no arquivo**
```
run.bat
```
Clique duas vezes no arquivo `run.bat` que está em `hotel_transilvania_pdv/`

**Opção 2: Via PowerShell/CMD**
```powershell
cd hotel_transilvania_pdv
./run.bat
```

### 🐧 Linux/Mac

**Via Terminal:**
```bash
cd hotel_transilvania_pdv
chmod +x run.sh
./run.sh
```

### 🐍 Via Python (Qualquer SO)

```bash
cd hotel_transilvania_pdv
python run.py
```

ou

```bash
python3 run.py
```

---

## ✨ O Que Os Scripts Fazem

1. ✅ **Verificam o ambiente** - Confere se Python e Django estão instalados
2. ✅ **Ativam o venv** - Se o ambiente virtual estiver desativado
3. ✅ **Executam migrações** - Prepara o banco de dados
4. ✅ **Coletam estáticos** - CSS, JS e arquivos estáticos
5. ✅ **Abrem o navegador** - Automaticamente na página de login
6. ✅ **Iniciam o servidor** - Django pronto para usar

---

## 🔐 Primeiro Acesso

Quando acessar a página de login, você verá:

```
🏰 Hotel Transilvânia
Sistema de Gerenciamento de PDV

[Campo: Usuário]
[Campo: Senha]

[Botão: Acessar Sistema]

Ainda não tem uma conta? Registre-se aqui
```

### Criar Primeira Conta

1. Clique em **"Registre-se aqui"**
2. Preencha os dados:
   - Nome de usuário
   - Email
   - Senha (mínimo 6 caracteres)
   - Confirmar senha
3. Clique em **"Criar Conta"**

### Login Posterior

Use as credenciais que você criou no registro.

---

## 🛑 Como Parar o Servidor

Pressione **Ctrl + C** no terminal onde o servidor está rodando.

---

## 📋 Requisitos

- Python 3.8+
- pip

## Estrutura de Arquivos

```
hotel_transilvania_pdv/
├── run.py           ← Script Python (universal)
├── run.bat          ← Script Windows
├── run.sh           ← Script Linux/Mac
├── manage.py
└── pdv/
```

---

## ❓ Solução de Problemas

### Erro: "manage.py não encontrado"
Execute o script dentro da pasta `hotel_transilvania_pdv/`

### Erro: "Python não está instalado"
- Windows: Baixe em python.org
- Linux: `sudo apt install python3`
- Mac: `brew install python3`

### Erro: "Ambiente virtual não encontrado"
Crie um novo venv:
```bash
python -m venv venv
```

Depois ative:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

E instale dependências:
```bash
pip install -r requirements.txt
```

### Navegador não abre automaticamente
Acesse manualmente: `http://127.0.0.1:8000/login/`

---

**Desenvolvido com ❤️ para Fuctura**
