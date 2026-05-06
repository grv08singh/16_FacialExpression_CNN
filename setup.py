from setuptools import setup, find_packages
from typing import List
import os

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    #This function will return the list of requirements
    try:
        with open(file_path) as f:
            requirements = [r.strip() for r in f.readlines()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
            return requirements
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return []

SRC_REPO = "CNN_Classifier"
VERSION = "0.1"
AUTHOR = "Grv"
AUTHOR_EMAIL = "grv08singh@gmail.com"
AUTHOR_USER_NAME = "grv08singh"
REPO_NAME = "16_FacialExpression_CNN"

setup(
    name=SRC_REPO,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
)