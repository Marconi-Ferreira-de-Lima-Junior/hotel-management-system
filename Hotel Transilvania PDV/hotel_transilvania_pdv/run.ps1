# 🏰 Hotel Transilvânia PDV - Script de Inicialização para Windows PowerShell
# Inicia automaticamente o servidor Django e abre a página de login

# Definições de core
$ErrorActionPreference = "Continue"

# Função para imprimir com cores
function Write-Info { Write-Host "ℹ️  $args" -ForegroundColor Cyan }
function Write-Success { Write-Host "✅ $args" -ForegroundColor Green }
function Write-Warning { Write-Host "⚠️  $args" -ForegroundColor Yellow }
function Write-Error { Write-Host "❌ $args" -ForegroundColor Red }
function Write-Header { Write-Host "$args" -ForegroundColor Magenta }

# Header
Write-Host ""
Write-Header "╔════════════════════════════════════════════════════════════════╗"
Write-Header "║         🏰 HOTEL TRANSILVÂNIA PDV - Sistema de Login 🏰        ║"
Write-Header "║                Inicializador PowerShell v2.0                    ║"
Write-Header "╚════════════════════════════════════════════════════════════════╝"
Write-Host ""

# Verifica se está no diretório correto
if (-not (Test-Path "manage.py")) {
    Write-Error "manage.py não encontrado"
    Write-Info "Execute este script no diretório: hotel_transilvania_pdv/"
    Read-Host "Pressione Enter para sair"
    exit 1
}

Write-Info "Verificando ambiente..."

# Verifica se Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Success "Python encontrado: $pythonVersion"
} catch {
    Write-Error "Python não está instalado ou não está no PATH"
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Verifica e ativa venv
Write-Info "Verificando ambiente virtual..."
if ($null -eq $env:VIRTUAL_ENV) {
    Write-Info "Ativando ambiente virtual..."
    if (Test-Path "..\venv\Scripts\Activate.ps1") {
        & ..\venv\Scripts\Activate.ps1
        Write-Success "Ambiente virtual ativado"
    } elseif (Test-Path "venv\Scripts\Activate.ps1") {
        & venv\Scripts\Activate.ps1
        Write-Success "Ambiente virtual ativado"
    } else {
        Write-Warning "Ambiente virtual não encontrado. Continuando mesmo assim..."
    }
} else {
    Write-Success "Ambiente virtual já está ativado"
}

# Executa migrações
Write-Host ""
Write-Info "Executando migrações do banco de dados..."
python manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Warning "Algumas migrações podem não ter sido aplicadas"
} else {
    Write-Success "Migrações completadas"
}

# Coleta arquivos estáticos
Write-Host ""
Write-Info "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput 2>&1 | Out-Null
Write-Success "Arquivos estáticos coletados"

# Aguarda inicialização
Write-Host ""
Write-Info "Aguardando inicialização..."
Start-Sleep -Seconds 2

# Abre o navegador
Write-Success "Abrindo navegador..."
Start-Process "http://127.0.0.1:8000/login/"

# Aguarda o servidor iniciar
Start-Sleep -Seconds 1

# Informa sobre o servidor
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                                                                ║" -ForegroundColor Green
Write-Host "║           🚀 Servidor rodando em http://127.0.0.1:8000        ║" -ForegroundColor Green
Write-Host "║                                                                ║" -ForegroundColor Green
Write-Host "║               🛑 Pressione Ctrl+C no terminal para parar       ║" -ForegroundColor Green
Write-Host "║                                                                ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

# Inicia o servidor Django
python manage.py runserver

Read-Host "Pressione Enter para fechar"
