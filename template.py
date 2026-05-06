import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "facial-expression-recognition"

list_of_files = [
    "app.py",
    ".github/workflows/.gitkeep",
    "artifacts/.gitkeep",
    "logs/.gitkeep",
    "notebooks/data/.gitkeep",
    "notebooks/01_test.ipynb",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/model_evaluation_mlflow.py",
    "src/components/model_training.py",
    "src/components/prepare_base_model.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/constants/__init__.py",
    "src/entities/__init__.py",
    "src/entities/config_entity.py",
    "src/pipelines/__init__.py",
    "src/pipelines/data_ingestion_pipeline.py",
    "src/pipelines/model_evaluation_pipeline.py",
    "src/pipelines/model_training_pipeline.py",
    "src/pipelines/prepare_base_model_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "templates/index.html",
    ".gitignore",
    "config.yaml",
    "dvc.yaml",
    "main.py",
    "params.yaml",
    "README.md",
    "requirements.txt",
    "setup_tf_gpu_env.bat",
    "setup.py",
    "template.py",
    "verify_gpu.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")