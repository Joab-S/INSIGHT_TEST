import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT", 6379))
expiration_time = int(os.getenv("EXPIRATION_TIME", 604800))

try:
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)
    
    # Verificar a conexão com o Redis
    redis_client.ping()
    print("Conexão com o Redis estabelecida com sucesso!")
except redis.exceptions.ConnectionError as e:
    print(f"Erro ao conectar ao Redis: {e}")