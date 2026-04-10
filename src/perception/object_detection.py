import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        self.net = cv2.dnn.readNet("models/yolov3.weights", "models/yolov3.cfg")

        with open("models/coco.names", "r") as f:
            self.classes = f.read().strip().split("\n")

        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

    def detect(self, frame):
        height, width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True)
        self.net.setInput(blob)

        outputs = self.net.forward(self.output_layers)

        detections = []

        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:
                    detections.append(self.classes[class_id])

        return detections