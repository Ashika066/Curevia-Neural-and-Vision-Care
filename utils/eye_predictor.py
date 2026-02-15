import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import numpy as np
from PIL import Image

class EyeDiseasePredictor:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.class_names = ['AMD', 'CNV', 'CSR', 'DME', 'DR', 'DRUSEN', 'MH', 'NORMAL'] # Updated classes
        self.image_size = 224

    def predict(self, image_path):
        img = Image.open(image_path)
        img = img.resize((self.image_size, self.image_size))
        img_array = np.array(img)
        if img_array.shape[-1] != 3:
            img_array = np.stack((img_array,) * 3, axis=-1)
        img_array = np.expand_dims(img_array, axis=0)

        predictions = self.model.predict(img_array, verbose=0)
        predicted_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_idx])
        all_probs = [float(p) for p in predictions[0]]

        return {
            'class_name': self.class_names[predicted_idx],
            'class_index': int(predicted_idx),
            'confidence': confidence,
            'all_predictions': all_probs # List of probabilities per class
        }