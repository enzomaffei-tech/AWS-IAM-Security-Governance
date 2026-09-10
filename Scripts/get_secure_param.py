import boto3
from botocore.exceptions import ClientError

def get_secret_parameter(param_name, region_name="us-east-1"):
    """
    Recupera com segurança um parâmetro criptografado no AWS SSM Parameter Store.
    """
    # Cria o cliente do Systems Manager (SSM)
    ssm_client = boto3.client('ssm', region_name=region_name)

    try:
        print(f"[+] Solicitando parâmetro seguro: {param_name}...")
        
        # O parâmetro WithDecryption=True força a descriptografia via AWS KMS
        response = ssm_client.get_parameter(
            Name=param_name,
            WithDecryption=True
        )
        
        param_value = response['Parameter']['Value']
        print("[✓] Parâmetro recuperado com sucesso!")
        return param_value

    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDeniedException':
            print("[✗] ERRO DE SEGURANÇA: Acesso negado pela política IAM.")
        else:
            print(f"[✗] Erro ao buscar parâmetro: {e}")
        return None

if __name__ == "__main__":
    # Nome do parâmetro de teste
    PARAM_NAME = "/config/db_password"
    
    # Execução da consulta
    secret = get_secret_parameter(PARAM_NAME)
    
    if secret:
        print(f"[RESULTADO] Valor recuperado: {secret}")
