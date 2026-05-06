from src.logger import logging
from src.config.configuration import ConfigurationManager
from src.components.prepare_base_model import PrepareBaseModel

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        logging.info("Entered Method main of class PrepareBaseModelPipeline")
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        logging.info("Exited Method main of class PrepareBaseModelPipeline")
