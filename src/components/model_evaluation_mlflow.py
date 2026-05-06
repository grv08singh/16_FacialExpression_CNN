import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from src.entities.config_entity import EvaluationConfig
from src.utils.common import save_json
import logging



class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _test_generator(self):
        logging.info("Entered Method: _test_generator in class Evaluation")
        test_datagen = ImageDataGenerator(rescale = 1./255)

        self.test_generator = test_datagen.flow_from_directory(
            directory=self.config.test_dir,
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )
        logging.info("Exited Method: _test_generator in class Evaluation")
    
    def load_model(self):
        logging.info(f"Entered Method: load_model in class Evaluation")
        self.model = tf.keras.models.load_model(self.config.trained_model_path)
        logging.info(f"Exited Method: load_model in class Evaluation")
    
    def save_score(self):
        logging.info(f"Entered Method: save_score in class Evaluation")
        scores = {"loss": float(self.score[0]), "accuracy": float(self.score[1])}
        save_json(path=self.config.evaluation_report, data=scores)
        logging.info(f"Exited Method: save_score in class Evaluation")
    
    def evaluate(self):
        logging.info("Entered Method: evaluate in class Evaluation")
        self._test_generator()
        self.load_model()
        self.score = self.model.evaluate(self.test_generator)
        logging.info(f"Score: {self.score}")
        self.save_score()
        logging.info("Exited Method: evaluate in class Evaluation")
    
    def log_into_mlflow(self):
        logging.info("Entered Method: log_into_mlflow in class Evaluation")
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="MobileNet")
            else:
                mlflow.keras.log_model(self.model, "model")
        logging.info("Exited Method: log_into_mlflow in class Evaluation")

