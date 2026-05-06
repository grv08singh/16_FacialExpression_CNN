from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    params_optimizer: str
    params_loss: str

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    updated_base_model_path: Path
    trained_model_path: Path
    train_dir: Path
    val_report: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

@dataclass(frozen=True)
class EvaluationConfig:
    root_dir: Path
    test_dir: Path
    trained_model_path: Path
    evaluation_report: Path
    mlflow_uri: str
    all_params: dict
    params_image_size: list
    params_batch_size: int