import os
import glob
from twilio.rest import Client

# Credenciais do Twilio
account_sid = '.......................'
auth_token = '.......................'
client = Client(account_sid, auth_token)

# Caminho para o diretório de logs de erro de backup
log_dir = '/erro_log/'

# Listar todos os arquivos no diretório de erro_log com a extensão .txt
log_files = glob.glob(os.path.join(log_dir, '*.txt'))

if not log_files:
    latest_log_name = "Nenhum arquivo de log encontrado."
else:
    # Obter o arquivo mais recente pelo tempo de modificação
    latest_log = max(log_files, key=os.path.getmtime)
    # Extrair o nome do arquivo
    latest_log_name = os.path.basename(latest_log)

# Montar a mensagem com o nome do arquivo de log
message_body = f"Ocorreu um erro na criação do Backup, por favor verique o arquivo de log: \n {latest_log_name}"

# Enviar a mensagem pelo Twilio
message = client.messages.create(
    from_='whatsapp:+5511999999999',
    body=message_body,
    to='whatsapp:+5511999999999'
)


print(message.sid)
