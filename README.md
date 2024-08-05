#BKP_to_Whatsapp

📚 **Sobre**

Este projeto consiste em um shell script que realiza o backup de um diretório, criando um arquivo comprimido dos dados com a data e hora atuais. O arquivo de backup é salvo em um diretório de destino especificado. Se o backup for bem-sucedido, um script Python (sucesso_backup.py) é executado para notificar o sucesso via WhatsApp. Em caso de falha, o erro é registrado em um log, e outro script Python (falha_backup.py) é executado para enviar uma notificação de falha. Além disso, backups antigos com mais de 2 dias são removidos automaticamente para liberar espaço em disco.

** Twilio📜 

Para utilizar os scripts Python de notificação via WhatsApp, é necessário criar uma conta no Twilio. O Twilio é uma plataforma de comunicação em nuvem que permite enviar mensagens de texto, voz e multimídia. Você pode criar uma conta gratuita no site oficial do Twilio e obter as credenciais necessárias (Account SID e Auth Token) para configurar as notificações em seus scripts.

Após a criação da conta, você precisará:

Verificar um número de telefone que será usado como remetente das mensagens.
Configurar suas credenciais no código dos scripts ou em variáveis de ambiente para garantir a segurança.


🚀 **Instalação
```
git clone https://github.com/AnubisChacal/BKP_to_Whatsap.git
cd nome-do-projeto
pip install -r requirements.txt
```
