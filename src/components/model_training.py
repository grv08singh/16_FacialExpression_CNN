import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from pathlib import Path
from src.logger import logging
from src.entities.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_updated_base_model(self):
        logging.info("Entered Method: get_base_model in class Training")
        self.model = load_model(
            self.config.updated_base_model_path
        )
        logging.info("Exited Method: get_base_model in class Training")
    
    def train_valid_generator(self):
        logging.info("Entered Method: train_valid_generator in class Training")

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.2
        )
        
        if self.config.params_is_augmentation:
            datagenerator = ImageDataGenerator(
                rotation_range = 40,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip = True,
                fill_mode = 'nearest',
                **datagenerator_kwargs
            )
        else:
            datagenerator = ImageDataGenerator(**datagenerator_kwargs)
        
        dataflow_kwargs = dict(
            directory=self.config.train_dir,
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            class_mode="categorical",
            interpolation = "bilinear"
        )
        
        self.train_generator = datagenerator.flow_from_directory(
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

        self.valid_generator = datagenerator.flow_from_directory(
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        logging.info("Exited Method: train_valid_generator in class Training")
    


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        logging.info(f"Entered Method: save_model in class Training")
        model.save(str(path))
        logging.info(f"Exited Method: save_model in class Training")

    def train(self):
        logging.info("Entered Method: train in class Training")
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps
        )
        
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
        
        logging.info("Exited Method: train in class Training")

