import logging
import os
from dotenv import load_dotenv

load_dotenv()

os.makedirs('logs', exist_ok=True) # si la carpeta no está se crea


log_path = os.getenv("LOG_PATH")

logging.basicConfig(
    filename=log_path, # directorio
    filemode='a',  # se va agregando
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # nivel debug
)

logger = logging.getLogger()
