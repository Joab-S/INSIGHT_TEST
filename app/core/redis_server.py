import subprocess
import time

def start_redis_server():
    try:
        redis_process = subprocess.Popen(["redis-server"])

        # Espera um curto período de tempo para garantir que o servidor Redis tenha tempo para iniciar completamente
        time.sleep(2)

        # Verifica se o processo do servidor Redis está em execução
        if redis_process.poll() is None:
            print("Servidor Redis iniciado com sucesso!")
        else:
            print("Falha ao iniciar o servidor Redis.")
    except Exception as e:
        print(f"Erro ao iniciar o servidor Redis: {e}")
