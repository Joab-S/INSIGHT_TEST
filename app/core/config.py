import redis
import os

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
expiration_time = int(os.getenv("EXPIRATION_TIME", 604800))

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)