from src.config.configuration import ConfigurationManager
from src.components.model_evaluation_mlflow import Evaluation
from src.logger import logging

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        logging.info("Entered Method main of class ModelEvaluationPipeline")
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluate()
        evaluation.save_score()
        evaluation.log_into_mlflow()
        logging.info("Exited Method main of class ModelEvaluationPipeline")


if __name__ == '__main__':
    pipeline = ModelEvaluationPipeline()
    pipeline.main()