from src.logger import logging
from src.config.configuration import ConfigurationManager
from src.components.model_training import Training
import warnings as wr
wr.filterwarnings("ignore", category=FutureWarning)

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logging.info("Model Training Pipeline started")
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_updated_base_model()
        training.train_valid_generator()
        training.train()
        logging.info("Model Training Pipeline completed")