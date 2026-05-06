import os
from box.exceptions import BoxValueError
import yaml
from src.logger import logging
import joblib
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logging.info(f"YAML file is empty: {path_to_yaml}")
        raise ValueError("YAML file is empty")
    except Exception as e:
        logging.info(f"Error occurred while loading YAML file: {path_to_yaml}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        content = json.load(f)
    logging.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logging.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(filename=path)
    logging.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_bytes = os.path.getsize(path)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    return f"{size_in_kb:.2f} KB"

def decode_Image(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())