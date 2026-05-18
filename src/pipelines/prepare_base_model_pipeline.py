from src.logger import logging
from src.config.configuration import ConfigurationManager
from src.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare Base Model"

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


if __name__ == '__main__':
    try:
        logging.info(f"{STAGE_NAME} started:")
        pipeline = PrepareBaseModelPipeline()
        pipeline.main()
        logging.info(f"{STAGE_NAME} completed\n\n")
    except Exception as e:
        logging.exception(e)
        raise e