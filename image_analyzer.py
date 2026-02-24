"""
Image Analysis Module
Analyzes images for forensic evidence
"""

import cv2
from PIL import Image
import os

class ImageAnalyzer:
    def __init__(self):
        self.name = "Image Analyzer"
    
    def analyze(self, image_path):
        """
        Analyze an image file
        """
        try:
            # Read image
            img = cv2.imread(image_path)
            
            if img is None:
                return "Error: Could not read image file"
            
            # Get image properties
            height, width, channels = img.shape
            
            # Get file info
            file_size = os.path.getsize(image_path)
            
            result = {
                "status": "success",
                "file": os.path.basename(image_path),
                "width": width,
                "height": height,
                "channels": channels,
                "size_bytes": file_size,
                "format": os.path.splitext(image_path)[1],
                "analysis": "Image dimensions and basic properties extracted"
            }
            
            return result
        
        except Exception as e:
            return {"status": "error", "message": str(e)}
          
