import cv2
import numpy as np
import time

class YOLOv11ObstacleDetector:
    def __init__(self, model_path="models/yolov11-nano.onnx", confidence_threshold=0.5):
        print(f"[AI] Initializing YOLOv11 model: {model_path}")
        self.classes = ["bird", "tree", "building", "wire", "tower", "human"]
        self.conf_threshold = confidence_threshold
        # Check if ONNX model is available, otherwise mock inference
        try:
            self.net = cv2.dnn.readNetFromONNX(model_path)
            self.is_mock = False
        except Exception:
            print("[AI] ONNX model weights not found. Activating simulated AI inference mode...")
            self.is_mock = True

    def process_frame(self, frame):
        """
        Runs YOLOv11 detection on the input camera frame.
        """
        if self.is_mock:
            # Simulate a real obstacle detection after some frames
            time.sleep(0.01)  # Mock GPU/CPU forward pass latency (10ms)
            height, width, _ = frame.shape
            
            # Simulated detection (e.g. wire ahead)
            detections = [
                {
                    "class": "wire",
                    "confidence": 0.89,
                    "bbox": [int(width*0.3), int(height*0.4), int(width*0.4), int(height*0.1)],
                    "distance_estimate_m": 8.5
                }
            ]
            return detections

        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward()
        
        # Post-processing YOLO outputs
        detections = []
        height, width = frame.shape[:2]
        
        for detection in outputs[0]:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > self.conf_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                
                detections.append({
                    "class": self.classes[class_id] if class_id < len(self.classes) else "unknown",
                    "confidence": float(confidence),
                    "bbox": [x, y, w, h],
                    "distance_estimate_m": round(50.0 / (h + 1), 2)  # Proxy distance based on pixel height
                })
        return detections

if __name__ == "__main__":
    # Test execution
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.putText(dummy_frame, "Sky Test Stream", (100, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    detector = YOLOv11ObstacleDetector()
    results = detector.process_frame(dummy_frame)
    print(f"[AI] Detection results: {results}")
