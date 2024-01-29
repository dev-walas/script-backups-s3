Script de Upload para Amazon S3

Este é um script Python que realiza o upload de um arquivo para o serviço de armazenamento Amazon S3. O script também gera um log com a data de envio, o tamanho do arquivo e o nome do arquivo enviado. Além disso, um alerta é enviado por meio de um webhook para notificar sobre o sucesso ou erro do upload.

Funcionalidades Principais:

Upload para S3: Utiliza a biblioteca boto3 para interagir com a API do Amazon S3 e realizar o upload do arquivo.
Log de Envio: Registra os detalhes do envio, como data, tamanho do arquivo em MB e nome do arquivo, em um arquivo de log (upload_log.txt).
Alerta via Webhook: Utiliza a biblioteca requests para enviar alertas sobre o status do upload por meio de um webhook.
Configurações Necessárias:
Antes de executar o script, é necessário configurar algumas variáveis no código:

AWS_ACCESS_KEY: Sua chave de acesso da AWS.<br>
AWS_SECRET_KEY: Sua chave secreta da AWS.<br>
AWS_BUCKET_NAME: Nome do bucket S3 de destino.<br>
AWS_REGION: Região AWS onde o bucket está localizado.<br>
WEBHOOK_URL: URL do webhook para receber alertas.<br>
cliente_nome: Nome do cliente, usado na formação do nome do arquivo enviado.<br>

Instalação e Configuração:

Instale as Dependências:
Certifique-se de ter as bibliotecas necessárias instaladas usando o seguinte comando:<br>

pip install boto3 requests tqdm

Clone o Repositório:

git clone https://github.com/dev-walas/script-backups-s3.git
cd script-backups-s3

Configure as Credenciais e Parâmetros:
Abra o script upload_to_s3.py e substitua as variáveis de configuração no início do script com suas credenciais AWS, informações do bucket e URL do webhook.

Execute o Script Manualmente:
Teste o script manualmente para garantir que tudo está configurado corretamente.
python upload_to_s3.py

Configure Agendamento (Opcional):
Se desejar executar o script automaticamente, configure uma tarefa agendada no Agendador de Tarefas do Windows ou usando uma ferramenta de agendamento de tarefas no seu ambiente.

Ajuste Adicional (Opcional):
Personalize o script conforme necessário para atender aos requisitos específicos do seu projeto.

Este script fornece uma solução simples para o envio automatizado de arquivos para o Amazon S3 e é facilmente adaptável para diferentes necessidades. Certifique-se de manter suas credenciais seguras e revisar periodicamente o log gerado para monitorar o status dos envios.
