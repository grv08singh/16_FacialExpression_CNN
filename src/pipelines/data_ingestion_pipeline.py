from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logger import logging

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logging.info(f"entered main method of DataIngestionPipeline")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.unzip_file()
            logging.info(f"exited main method of DataIngestionPipeline\n\n")
        except Exception as e:
            logging.exception(e)
            raise e

if __name__ == '__main__':
    try:
        logging.info(f"{STAGE_NAME} started:")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logging.info(f"{STAGE_NAME} completed\n\n")
    except Exception as e:
        logging.exception(e)
        raise e