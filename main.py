from src.logger import logging
from src.pipelines.data_ingestion_pipeline import DataIngestionPipeline
from src.pipelines.prepare_base_model_pipeline import PrepareBaseModelPipeline
from src.pipelines.model_training_pipeline import ModelTrainingPipeline
from src.pipelines.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logging.info(f"Exception occurred in stage {STAGE_NAME} stage")
    raise e


STAGE_NAME = "Model Training"
try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logging.info(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logging.info(e)
    raise e