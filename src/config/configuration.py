import os
from src.constants import *
from src.utils.common import read_yaml, create_directories, save_json
from src.entities.config_entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluationConfig
import logging

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        logging.info("Initialization started for class: ConfigurationManager")
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        logging.info("Initialization completed for class: ConfigurationManager")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logging.info("Entered Method: get_data_ingestion_config")
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        logging.info("Exited Method: get_data_ingestion_config")
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        logging.info("Entered Method: get_prepare_base_model_config")
        config = self.config.prepare_base_model
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_optimizer=self.params.OPTIMIZER,
            params_loss=self.params.LOSS
        )
        logging.info("Exited Method: get_prepare_base_model_config")
        return prepare_base_model_config

    def get_training_config(self) -> TrainingConfig:
        logging.info("Entered Method: get_training_config")
        training = self.config.training
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            updated_base_model_path=Path(self.config.prepare_base_model.updated_base_model_path),
            trained_model_path=Path(training.trained_model_path),
            train_dir=Path(training.train_dir),
            val_report=Path(training.val_report),
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_is_augmentation=self.params.AUGMENTATION,
            params_image_size=self.params.IMAGE_SIZE
        )
        logging.info("Exited Method: get_training_config")
        return training_config
    
    
    def get_evaluation_config(self) -> EvaluationConfig:
        logging.info("Entered Method: get_evaluation_config")
        eval = self.config.evaluation
        create_directories([Path(eval.root_dir)])

        eval_config = EvaluationConfig(
            root_dir=Path(eval.root_dir),
            test_dir=Path(eval.test_dir),
            trained_model_path=Path(self.config.training.trained_model_path),
            evaluation_report=Path(eval.evaluation_report),
            mlflow_uri=eval.mlflow_uri,
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        logging.info("Exited Method: get_evaluation_config")
        return eval_config