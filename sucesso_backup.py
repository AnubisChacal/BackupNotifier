import os
import glob
from twilio.rest import Client

# Credenciais do Twilio
account_sid = '.......................'
auth_token = '.......................'
client = Client(account_sid, auth_token)

# Caminho para o diretório de backups
backup_dir = '/backup'

# Listar todos os arquivos no diretório de backups com a extensão .tar.gz
backup_files = glob.glob(os.path.join(backup_dir, '*.tar.gz'))

if not backup_files:
    latest_backup_name = "Nenhum arquivo de backup encontrado."
else:
    # Obter o arquivo mais recente pelo tempo de modificação
    latest_backup = max(backup_files, key=os.path.getmtime)
    # Extrair apenas o nome do arquivo (sem o caminho completo)
    latest_backup_name = os.path.basename(latest_backup)

# Montar a mensagem com o nome do arquivo de backup
message_body = f"Backup do servidor de Minecraft realizado: \n {latest_backup_name}"

# Enviar a mensagem pelo Twilio
message = client.messages.create(
    from_='whatsapp:+5511999999999',  
    body=message_body,
    to='whatsapp:+5511999999999'   
)

# Exibir o SID da mensagem enviada
print(message.sid)
