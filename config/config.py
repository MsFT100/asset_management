from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# dotenv_path = Path('../.env')
# load_dotenv(dotenv_path=dotenv_path)


class DatabaseConfig:
    def __init__(self):
        self.engine = os.getenv('DB_ENGINE')
        self.name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')

test = 3453