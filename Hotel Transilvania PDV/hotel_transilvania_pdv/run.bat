@echo off
REM 🏰 Hotel Transilvânia PDV - Script de Inicialização para Windows
REM Inicia automaticamente o servidor Django e abre a página de login

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║         🏰 HOTEL TRANSILVÂNIA PDV - Sistema de Login 🏰        ║
echo ║                   Inicializador para Windows v2.0              ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Verifica se está no diretório correto
if not exist "manage.py" (
    echo ❌ Erro: manage.py não encontrado
    echo    Execute este script no diretório: hotel_transilvania_pdv/
    pause
    exit /b 1
)

echo ℹ️  Verificando ambiente...

REM Verifica se python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não está instalado ou não está no PATH
    pause
    exit /b 1
)
echo ✅ Python encontrado

REM Verifica se venv está ativado
if not defined VIRTUAL_ENV (
    echo ℹ️  Ativando ambiente virtual...
    if exist "..\venv\Scripts\activate.bat" (
        call ..\venv\Scripts\activate.bat
        echo ✅ Ambiente virtual ativado
    ) else if exist "venv\Scripts\activate.bat" (
        call venv\Scripts\activate.bat
        echo ✅ Ambiente virtual ativado
    ) else (
        echo ⚠️  Ambiente virtual não encontrado. Continuando mesmo assim...
    )
) else (
    echo ✅ Ambiente virtual já está ativado
)

echo.
echo ℹ️  Executando migrações do banco de dados...
python manage.py migrate
if errorlevel 1 (
    echo ⚠️  Algumas migrações podem não ter sido aplicadas
)
echo ✅ Migrações completadas

echo.
echo ℹ️  Coletando arquivos estáticos...
python manage.py collectstatic --noinput >nul 2>&1
echo ✅ Arquivos estáticos coletados

echo.
echo ℹ️  Aguardando inicialização...
timeout /t 2 /nobreak

echo ✅ Abrindo navegador...
start http://127.0.0.1:8000/login/

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║           🚀 Servidor rodando em http://127.0.0.1:8000        ║
echo ║                                                                ║
echo ║               🛑 Pressione Ctrl+C no terminal para parar       ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Inicia o servidor Django
python manage.py runserver

pause
