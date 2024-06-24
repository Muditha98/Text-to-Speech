# Import required libraries
import logging
import os
from datetime import datetime

# Creating logs directory to store log in files
LOG_DIR = "pylogs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# Creating directory if it does not exists
os.makedirs(LOG_DIR, exist_ok=True)

# Creating file with name as file_name
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"
log_file_path = os.path.join(LOG_DIR, file_name)

# Create and configure logging
logging.basicConfig(level=logging.INFO,
                    filename=log_file_path,
                    format='%(asctime)s %(levelname)s %(module)s ====> %(message)s',
                    datefmt="%d-%m-%Y %H:%M")

# Create object for logging
logger = logging.getLogger()