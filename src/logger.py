import logging 
import os 
from datetime import datetime

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s"
)
