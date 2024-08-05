# 📦BKP_to_Whatsapp📦

📚 Sobre
O shellscript faz o backup de um diretorio, criando um arquivo comprimido dos dados com a data e hora atuais, salvando-o em um diretório de destino. Se o backup for bem-sucedido, um script Python é executado para notificar o sucesso; em caso de falha, o erro é registrado em um log e outro script Python é executado para notificação. Além disso, backups antigos com mais de 2 dias são removidos automaticamente

#sucesso_backup.py e falha_backup.py:# Envia uma notificação de sucesso via WhatsApp usando a API do Twilio.
