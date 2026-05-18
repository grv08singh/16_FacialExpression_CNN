# 16_Detect_Facial_Expression_DL_Proj
detect facial expressions using CNN.

## Workflows

01. Update config.yaml
02. Update secrets.yaml [Optional]
03. Update params.yaml
04. Update the entity
05. Update the configuration manager in src config
06. Update the components
07. Update the pipeline 
08. Update the main.py
09. Update the dvc.yaml
10. app.py


#### clone the repository
``` bash
git clone https://github.com/grv08singh/16_FacialExpression_CNN.git
```
#### create conda env inside the project directory
``` bash
conda create -p tf_gpu python=3.9 -y
conda activate tf_gpu
```
#### Install Cuda Toolkit and cuDNN ::
``` bash
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y
```
#### Install TensorFlow GPU and Required Libraries
``` bash
pip install tensorflow-gpu==2.10.1
pip uninstall -y numpy
pip install numpy==1.23.5
conda install -c conda-forge greenlet -y
pip install -r requirements.txt
``` 



##### cmd
``` bash
mlflow ui
```
### dagshub
MLFLOW_TRACKING_URI=https://dagshub.com/grv08singh/16_FacialExpression_CNN.mlflow \
MLFLOW_TRACKING_USERNAME=grv08singh \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/grv08singh/16_FacialExpression_CNN.mlflow
export MLFLOW_TRACKING_USERNAME=entbappy 
export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0
```


### DVC cmd
``` git bash
dvc init
dvc repro
dvc dag
```

## About MLflow & DVC
#### MLflow
 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model
#### DVC
 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)