from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)


class DatabaseConfig:
    def __init__(self):
        self.engine = 'django.db.backends.postgresql'
        self.name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = 'localhost'
        self.port = '5432'
