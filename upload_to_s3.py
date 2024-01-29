import boto3
import os
import datetime
import requests
from tqdm import tqdm  

# Configurações do S3
AWS_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_BUCKET_NAME = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_REGION = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

# Configurações do Webhook
WEBHOOK_URL = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

# Variáveis para o nome do cliente
cliente_nome = 'XXXXX'  # Altere para o nome desejado

def upload_to_s3(file_path):
    # Inicializa o cliente S3
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

    # Obtém a data atual
    current_date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        # Constrói o novo nome do arquivo com o cliente, data e nome original do arquivo
        new_file_name = f"{cliente_nome}_{current_date}_{os.path.basename(file_path)}"

        # Configura a barra de progresso
        file_size = os.path.getsize(file_path)
        with tqdm(total=file_size, unit='B', unit_scale=True, desc='Upload') as pbar:
            # Atualiza o callback para a barra de progresso
            def progress_callback(bytes_amount):
                pbar.update(bytes_amount)

            # Faz o upload do arquivo para o S3 com o callback
            s3.upload_file(file_path, AWS_BUCKET_NAME, new_file_name, Callback=progress_callback)

        # Registra os detalhes no log
        log_message = f"Data de envio: {current_date}, Tamanho do arquivo: {file_size / (1024 * 1024):.2f} MB, Nome do arquivo: {new_file_name}"

        with open('upload_log.txt', 'a') as log_file:
            log_file.write(log_message + '\n')

        # Envia alerta via webhook (sucesso)
        send_webhook_alert(f"Upload bem-sucedido: {log_message}")

        print("Upload concluído com sucesso!")

    except Exception as e:
        # Registra mensagem de erro no log
        error_message = f"Erro ao fazer o upload para o S3: {e}"
        with open('upload_log.txt', 'a') as log_file:
            log_file.write(error_message + '\n')

        # Envia alerta via webhook (erro)
        send_webhook_alert(f"Erro durante o upload: {error_message}")

        print(f"Erro ao fazer o upload para o S3: {e}")

def send_webhook_alert(message):
    payload = {'content': message}
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    # Substitua 'C:/Sistema/Dados/DADOS.FDB' pelo caminho do seu arquivo
    file_path = 'C:/Sistema/Dados/DADOS.FDB' 
    upload_to_s3(file_path)
