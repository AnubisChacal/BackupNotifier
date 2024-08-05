#!/bin/bash

# Diretório de origem (o que será copiado)
SRC="/root/user/projeto"

# Diretório de destino (onde o backup será armazenado)
DEST="/backup"

# Nome do arquivo de backup (com data e hora)
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_NAME="projeto_$DATE.tar.gz"

# Criando o backup
tar -czvf "$DEST/$BACKUP_NAME" "$SRC"

# Verifica se o backup foi criado com sucesso
if [ $? -eq 0 ]; then
    echo "Backup realizado com sucesso: $BACKUP_FILE"

    # Caminho para o script Python
    PYTHON_SCRIPT="/sucesso_backup.py"

    # Executando o script Python
    python3 "$PYTHON_SCRIPT"


else
    # Mensagem de erro
    ERROR_MESSAGE="Erro ao realizar o backup: $(date)"

    # Exibindo a mensagem de erro
    echo "$ERROR_MESSAGE" >&2

    # Data e hora atuais para o nome do arquivo de log
    DATE=$(date +"%Y-%m-%d_%H-%M-%S")

    # Caminho para o arquivo de log de erros, incluindo a data
    ERROR_LOG="/erro_log/error_log_$DATE.txt"

    # Salvando a mensagem de erro no arquivo de log
    echo "$ERROR_MESSAGE" >> "$ERROR_LOG"

    # Caminho para o script Python em caso de falha
    PYTHON_SCRIPT="/falha_backup.py"

    # Executando o script Python de falha
    python3 "$PYTHON_SCRIPT"

    exit 1
fi

# Remover backup antigo
find $DEST -type f -name "projeto_*.tar.gz" -mtime +2 -exec rm {} \;
