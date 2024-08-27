# 🔔 BackupNotifier

BackupNotifier é um sistema automatizado que combina scripts Bash e Python para realizar backups de diretórios importantes e enviar notificações via WhatsApp utilizando a API do Twilio. O projeto garante que você esteja sempre informado sobre o status dos seus backups, seja em caso de sucesso ou falha.

## 🛠️ Funcionalidades

- **Backup Automatizado**: Criação de backups comprimidos (`.tar.gz`) de diretórios especificados, armazenando-os em um local seguro.
- **Notificações via WhatsApp**: Envio de mensagens via WhatsApp para notificar o sucesso ou falha na criação dos backups.
- **Logs de Erro**: Geração de logs detalhados em caso de falha, com informações específicas para facilitar a resolução do problema.
- **Gerenciamento de Backups Antigos**: Remoção automática de backups antigos, mantendo o sistema de armazenamento organizado.

## 📂 Estrutura do Projeto

- **`BKP_to_Whatsapp.sh`** 🚀: Script Bash principal que realiza o backup, verifica o status do processo e chama os scripts Python apropriados para enviar notificações.
- **`sucesso_backup.py`** ✅: Script Python que envia uma mensagem de sucesso via WhatsApp usando a API do Twilio.
- **`falha_backup.py`** ❌: Script Python que envia uma mensagem de falha via WhatsApp usando a API do Twilio, incluindo o nome do arquivo de log gerado.
- **`/backup`** 🗄️: Diretório onde os backups são armazenados.
- **`/erro_log`** 🛠️: Diretório onde os logs de erro são armazenados.

## 🚀 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/AnubisChacal/BackupNotifier.git
    ```

2. **Configure suas credenciais do Twilio**:
    - Substitua `account_sid` e `auth_token` pelas suas credenciais do Twilio nos arquivos `sucesso_backup.py` e `falha_backup.py`.

3. **Edite os diretórios de origem e destino**:
    - No script `BKP_to_Whatsapp.sh`, defina `SRC` para o diretório que você deseja fazer backup e `DEST` para o diretório onde o backup será armazenado.

4. **Execute o script de backup**:
    ```bash
    bash BKP_to_Whatsapp.sh
    ```

5. **Receba notificações**:
   - Você receberá uma mensagem no WhatsApp informando o sucesso ou falha do backup.

## 🛠️ Requisitos

- **Bash** (para execução de scripts)
- **Python 3.x**
- **Biblioteca `twilio` para Python** (instale com `pip install twilio`)
- **Twilio Account** (para enviar mensagens via WhatsApp)

## 🔧 Personalização

- **Configurações de Backup**: Ajuste o script `BKP_to_Whatsapp.sh` para atender às suas necessidades de backup, como o diretório de origem e o tempo de retenção dos backups.
- **Notificações**: Personalize as mensagens enviadas nos scripts Python (`sucesso_backup.py` e `falha_backup.py`) conforme necessário.
