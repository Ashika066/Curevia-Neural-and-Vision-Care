import tensorflow as tf
import numpy as np
from PIL import Image

class BrainTumorPredictor:
    def __init__(self, model_path):
        """Initialize the Brain Tumor predictor with model path."""
        self.model = tf.keras.models.load_model(model_path)
        # Based on your training: glioma, meningioma, notumor, pituitary
        self.class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']
        self.image_size = 128  # Your model uses 128x128
        
    def augment_image(self, image):
        """Apply the same augmentation used during training."""
        from PIL import ImageEnhance
        import random
        
        image = ImageEnhance.Brightness(image).enhance(random.uniform(0.8, 1.2))
        image = ImageEnhance.Contrast(image).enhance(random.uniform(0.8, 1.2))
        return image
        
    def predict(self, image_path):
        """
        Predict brain tumor from MRI image.
        
        Args:
            image_path: Path to the MRI image file
            
        Returns:
            dict: Prediction results with class name, index, and confidence
        """
        # Load image
        img = Image.open(image_path)
        img = img.resize((self.image_size, self.image_size))
        
        # Apply augmentation (optional - remove if you want consistent predictions)
        # img = self.augment_image(img)
        
        # Convert to array and normalize
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        predictions = self.model.predict(img_array, verbose=0)
        predicted_class_index = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_index])
        
        return {
            'class_name': self.class_names[predicted_class_index],
            'class_index': int(predicted_class_index),
            'confidence': confidence,
            'all_predictions': predictions[0].tolist()
        }
