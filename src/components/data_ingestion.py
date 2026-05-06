import os
import zipfile
import gdown
from src.logger import logging
from src.utils.common import get_size
from src.entities.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        logging.info("Initialization started for class: DataIngestion")
        self.config = config
        logging.info("Initialization completed for class: DataIngestion")
        
    def unzip_file(self):
        logging.info("Entered Method unzip_file")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)
        logging.info("Exited Method unzip_file")