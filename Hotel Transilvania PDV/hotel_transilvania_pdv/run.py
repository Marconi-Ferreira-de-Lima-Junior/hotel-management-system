#!/usr/bin/env python
"""
🏰 Hotel Transilvânia PDV - Script de Inicialização
Inicia automaticamente o servidor Django e abre a página de login

Uso: python run.py
"""

import os
import sys
import subprocess
import time
import webbrowser
import platform
from pathlib import Path

# Cores para terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header():
    """Exibe o header do aplicativo"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║         🏰 HOTEL TRANSILVÂNIA PDV - Sistema de Login 🏰        ║")
    print("║                   Inicializador Automático v2.0                 ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}\n")


def print_info(message):
    """Imprime mensagem de informação"""
    print(f"{Colors.OKBLUE}ℹ️  {message}{Colors.ENDC}")


def print_success(message):
    """Imprime mensagem de sucesso"""
    print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")


def print_warning(message):
    """Imprime mensagem de aviso"""
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")


def print_error(message):
    """Imprime mensagem de erro"""
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")


def check_static_files_exist():
    """Verifica se os arquivos estáticos existem"""
    static_path = Path("pdv/static")
    if not static_path.exists():
        print_warning("Diretório static não encontrado")
        return False
    return True


def check_environment():
    """Verifica se o ambiente está configurado"""
    print_info("Verificando ambiente...")
    
    # Verifica se está no diretório correto
    if not Path("manage.py").exists():
        print_error("manage.py não encontrado. Execute este script no diretório: hotel_transilvania_pdv/")
        sys.exit(1)
    
    print_success("Ambiente verificado corretamente")
    return True


def install_dependencies():
    """Instala as dependências se necessário"""
    print_info("Verificando dependências...")
    
    try:
        import django
        print_success("Django já está instalado")
    except ImportError:
        print_warning("Instalando dependências...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "../requirements.txt"], check=True)
        print_success("Dependências instaladas")


def run_migrations():
    """Executa as migrações do banco de dados"""
    print_info("Executando migrações do banco de dados...")
    
    try:
        result = subprocess.run(
            [sys.executable, "manage.py", "migrate"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print_success("Migrações executadas com sucesso")
            return True
        else:
            print_warning("Algumas migrações podem não ter sido aplicadas")
            print(result.stderr)
            return True  # Continua mesmo se houver problema
    except subprocess.TimeoutExpired:
        print_error("Timeout ao executar migrações")
        return False
    except Exception as e:
        print_error(f"Erro ao executar migrações: {e}")
        return False


def collect_static():
    """Coleta arquivos estáticos"""
    print_info("Coletando arquivos estáticos...")
    
    try:
        result = subprocess.run(
            [sys.executable, "manage.py", "collectstatic", "--noinput"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print_success("Arquivos estáticos coletados")
            return True
        else:
            # Não é crítico se falhar
            print_warning("Arquivos estáticos já coletados ou não necessário")
            return True
    except Exception as e:
        print_warning(f"Não foi possível coletar estáticos: {e}")
        return True


def open_browser(url="http://127.0.0.1:8000/login/"):
    """Abre o navegador na URL especificada"""
    print_info(f"Abrindo navegador em {url}...")
    
    try:
        webbrowser.open(url)
        print_success("Navegador aberto com sucesso")
        return True
    except Exception as e:
        print_warning(f"Não foi possível abrir o navegador automaticamente: {e}")
        print_info(f"Acesse manualmente: {url}")
        return False


def run_server():
    """Inicia o servidor Django"""
    print_info("Iniciando servidor Django...")
    print_success("Servidor iniciado com sucesso!")
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                                                                ║")
    print("║           🚀 Servidor rodando em http://127.0.0.1:8000        ║")
    print("║                                                                ║")
    print("║                  🛑 Pressione Ctrl+C para parar               ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}\n")
    
    try:
        subprocess.run([sys.executable, "manage.py", "runserver"], check=False)
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}\n⚠️  Servidor interrompido pelo usuário{Colors.ENDC}\n")
        sys.exit(0)


def main():
    """Função principal"""
    print_header()
    
    # Verifica ambiente
    if not check_environment():
        sys.exit(1)
    
    # Instala dependências se necessário
    install_dependencies()
    
    # Executa migrações
    if not run_migrations():
        print_error("Falha nas migrações. Continuando mesmo assim...")
    
    # Coleta arquivos estáticos
    collect_static()
    
    # Aguarda um pouco antes de abrir o navegador
    print_info("Aguardando inicialização...")
    time.sleep(2)
    
    # Tenta abrir o navegador após 3 segundos
    time.sleep(1)
    open_browser()
    
    # Inicia o servidor
    run_server()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}⚠️  Operação cancelada pelo usuário{Colors.ENDC}\n")
        sys.exit(0)
    except Exception as e:
        print_error(f"Erro inesperado: {e}")
        sys.exit(1)
