import tensorflow as tf
import sys

print(f"\nPython Version: {sys.version}")
print(f"TensorFlow Version: {tf.__version__}")

# Check GPU availability
gpus = tf.config.list_physical_devices('GPU')
print(f"\nGPU Devices Found: {len(gpus)}")

if gpus:
    for i, gpu in enumerate(gpus):
        print(f"  GPU {i}: {gpu.name}")
        print(f"  Device Type: {gpu.device_type}")
else:
    print("\n⚠ No GPU detected. TensorFlow will run on CPU only.")