#!/bin/bash

# 🏰 Hotel Transilvânia PDV - Script de Inicialização para Linux/Mac
# Inicia automaticamente o servidor Django e abre a página de login

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "\n${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         🏰 HOTEL TRANSILVÂNIA PDV - Sistema de Login 🏰        ║${NC}"
echo -e "${BLUE}║                Inicializador para Linux/Mac v2.0                ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}\n"

# Verifica se está no diretório correto
if [ ! -f "manage.py" ]; then
    echo -e "${RED}❌ Erro: manage.py não encontrado${NC}"
    echo "   Execute este script no diretório: hotel_transilvania_pdv/"
    exit 1
fi

echo -e "${BLUE}ℹ️  Verificando ambiente...${NC}"

# Verifica se python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 não está instalado${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python 3 encontrado$(python3 --version)${NC}"

# Verifica se venv está ativado ou tenta ativar
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${BLUE}ℹ️  Ativando ambiente virtual...${NC}"
    if [ -f "../venv/bin/activate" ]; then
        source ../venv/bin/activate
        echo -e "${GREEN}✅ Ambiente virtual ativado${NC}"
    elif [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        echo -e "${GREEN}✅ Ambiente virtual ativado${NC}"
    else
        echo -e "${YELLOW}⚠️  Ambiente virtual não encontrado. Continuando mesmo assim...${NC}"
    fi
else
    echo -e "${GREEN}✅ Ambiente virtual já está ativado${NC}"
fi

echo -e "\n${BLUE}ℹ️  Executando migrações do banco de dados...${NC}"
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Algumas migrações podem não ter sido aplicadas${NC}"
fi
echo -e "${GREEN}✅ Migrações completadas${NC}"

echo -e "\n${BLUE}ℹ️  Coletando arquivos estáticos...${NC}"
python3 manage.py collectstatic --noinput > /dev/null 2>&1
echo -e "${GREEN}✅ Arquivos estáticos coletados${NC}"

echo -e "\n${BLUE}ℹ️  Aguardando inicialização...${NC}"
sleep 2

echo -e "${GREEN}✅ Abrindo navegador...${NC}"

# Tenta abrir o navegador de acordo com o sistema
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open http://127.0.0.1:8000/login/
elif command -v xdg-open &> /dev/null; then
    # Linux
    xdg-open http://127.0.0.1:8000/login/
else
    echo -e "${YELLOW}⚠️  Não foi possível abrir o navegador automaticamente${NC}"
    echo -e "${BLUE}    Acesse manualmente: http://127.0.0.1:8000/login/${NC}"
fi

echo -e "\n${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                                ║${NC}"
echo -e "${GREEN}║           🚀 Servidor rodando em http://127.0.0.1:8000        ║${NC}"
echo -e "${GREEN}║                                                                ║${NC}"
echo -e "${GREEN}║                  🛑 Pressione Ctrl+C para parar               ║${NC}"
echo -e "${GREEN}║                                                                ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}\n"

# Inicia o servidor Django
python3 manage.py runserver
