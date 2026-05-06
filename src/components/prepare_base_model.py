import os
from src.logger import logging
import tensorflow as tf
from keras.applications import MobileNet
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import Adam, Adagrad, Adamax, SGD, RMSprop
from pathlib import Path
from src.entities.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        logging.info("Initialization started for class PrepareBaseModel")
        self.config = config
        logging.info("Initialization completed for class PrepareBaseModel")
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            logging.info(f"Saving the model at {path}...")
            model.save(str(path))
            logging.info("Model saved successfully.")
        except Exception as e:
            logging.info("Error occurred while saving the model.")
            raise e
    
    def get_base_model(self):
        try:
            logging.info("Entered Method get_base_model")
            logging.info("Creating the base model from Keras.Applications...")
            self.base_model = MobileNet(
                input_shape=self.config.params_image_size,
                weights=self.config.params_weights,
                include_top=self.config.params_include_top
            )
            self.save_model(path=self.config.base_model_path, model=self.base_model)
            logging.info("Base model created successfully.")
            logging.info("Exited Method get_base_model")
        except Exception as e:
            logging.info("Error occurred while creating the base model.")
            raise e
    
    @staticmethod
    def _update_base_model(base_model, classes, freeze_all, freeze_till, optimizer, loss):
        if freeze_all:
            for layer in base_model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in base_model.layers[:-freeze_till]:
                layer.trainable = False
        
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(units=1024, activation="relu")(x)
        predictions = Dense(units=classes, activation="softmax")(x)

        updated_model = Model(inputs=base_model.input, outputs=predictions)

        updated_model.compile(
            optimizer=optimizer,
            loss=loss,
            metrics=["accuracy"]
        )
        updated_model.summary()
        return updated_model
    
    def update_base_model(self):
        try:
            logging.info("Entered Method update_base_model")
            logging.info("Updating the base model...")

            lr = self.config.params_learning_rate
            opt = self.config.params_optimizer.lower()
            if opt == "adam":
                optimizer = Adam(learning_rate = lr)
            elif opt == "adagrad":
                optimizer = Adagrad(learning_rate = lr)
            elif opt == "adamax":
                optimizer = Adamax(learning_rate = lr)
            elif opt == "sgd":
                optimizer = SGD(learning_rate = lr)
            elif opt == "rmsprop":
                optimizer = RMSprop(learning_rate = lr)
            else:
                optimizer = Adam()

            self.updated_model = self._update_base_model(
                base_model=self.base_model,
                classes=self.config.params_classes,
                freeze_all=True,
                freeze_till=None,
                optimizer=optimizer,
                loss = self.config.params_loss
            )
            self.save_model(path=self.config.updated_base_model_path, model=self.updated_model)
            logging.info("Base model updated successfully.")
            logging.info("Exited Method update_base_model")
        except Exception as e:
            logging.info("Error occurred while updating the base model.")
            raise e