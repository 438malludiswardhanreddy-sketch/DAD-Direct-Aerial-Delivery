import numpy as np
import time

class WeatherClassifier:
    def __init__(self, weights_path="models/weather-efficientnet.h5"):
        print(f"[AI] Loading EfficientNet weather classifier: {weights_path}")
        self.labels = ["Clear", "Rain", "Fog", "StrongWind", "DustStorm"]
        self.is_mock = True

    def classify(self, frame) -> dict:
        """
        Classifies current meteorological visibility and conditions.
        """
        # Under SITL testing, weather is dynamic or controlled by sim variables
        # We simulate a 5ms forward pass and return a sample classification
        time.sleep(0.005)
        
        # Simulate: 95% chance Clear, 5% other
        probabilities = [0.95, 0.02, 0.01, 0.01, 0.01]
        max_idx = np.argmax(probabilities)
        
        return {
            "condition": self.labels[max_idx],
            "confidence": probabilities[max_idx],
            "all_probabilities": dict(zip(self.labels, probabilities))
        }

if __name__ == "__main__":
    classifier = WeatherClassifier()
    dummy_img = np.zeros((224, 224, 3), dtype=np.uint8)
    result = classifier.classify(dummy_img)
    print(f"[AI] Weather classification: {result}")
