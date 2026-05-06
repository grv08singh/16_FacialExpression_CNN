:: Remove Previous Environment if Exists ::
conda deactivate
conda env remove -p tf_gpu -y

:: Create New Environment ::
conda create -p tf_gpu python=3.9 -y
conda activate tf_gpu

:: Install Cuda Toolkit and cuDNN ::
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y

:: Install TensorFlow GPU and Required Libraries ::
pip install tensorflow-gpu==2.10.1
pip uninstall -y numpy
pip install numpy==1.23.5
conda install -c conda-forge greenlet -y
pip install -r requirements.txt

:: Verify GPU Installation ::
python verify_gpu.py
