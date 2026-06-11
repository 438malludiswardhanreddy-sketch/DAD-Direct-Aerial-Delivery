import sys
import os
import unittest
import numpy as np

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai.vision.obstacle_detector import YOLOv11ObstacleDetector
from ai.weather.weather_classifier import WeatherClassifier
from backend.database import DatabaseManager

class TestDADSystem(unittest.TestCase):
    def test_obstacle_detector_mock(self):
        detector = YOLOv11ObstacleDetector()
        dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        results = detector.process_frame(dummy_frame)
        
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]["class"], "wire")
        self.assertGreater(results[0]["confidence"], 0.5)

    def test_weather_classifier(self):
        classifier = WeatherClassifier()
        dummy_frame = np.zeros((224, 224, 3), dtype=np.uint8)
        result = classifier.classify(dummy_frame)
        
        self.assertIn("condition", result)
        self.assertIn("confidence", result)
        self.assertIn(result["condition"], classifier.labels)

    def test_database_init(self):
        db_path = "test_dad_logistics.db"
        if os.path.exists(db_path):
            os.remove(db_path)
            
        db = DatabaseManager(db_path)
        drones = db.get_all_drones()
        self.assertEqual(len(drones), 3)
        self.assertEqual(drones[0]["id"], "drone_01")
        
        # Cleanup
        if os.path.exists(db_path):
            os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
