"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Camera Detection Processing
Description: Receives frame streams and simulates bounding box coordinate outputs 
             representing objects such as wires, trees, poles, or birds.
"""

class CameraObstacleDetector:
    def __init__(self, confidence_cutoff=0.6):
        self.cutoff = confidence_cutoff
        print("[Sensor Fusion] Camera obstacle detector module initialised.")

    def parse_detections(self, frame_id, mock_onnx_outputs):
        """
        Parses simulated ONNX inference raw output arrays.
        Filters targets below the specified confidence threshold.
        """
        valid_obstacles = []
        for det in mock_onnx_outputs:
            confidence = det.get("confidence", 0.0)
            if confidence >= self.cutoff:
                valid_obstacles.append({
                    "frame_id": frame_id,
                    "class_name": det.get("class"),
                    "bbox": det.get("bbox"),  # [x, y, width, height]
                    "confidence": round(confidence, 2)
                })
        return valid_obstacles
