"""
Document Analysis Module
Analyzes PDF and DOCX files for forensic evidence
"""

import os
from pathlib import Path

class DocumentAnalyzer:
    def __init__(self):
        self.name = "Document Analyzer"
    
    def analyze(self, doc_path):
        """
        Analyze a document file (PDF or DOCX)
        """
        try:
            file_ext = os.path.splitext(doc_path)[1].lower()
            file_size = os.path.getsize(doc_path)
            
            result = {
                "status": "success",
                "file": os.path.basename(doc_path),
                "format": file_ext,
                "size_bytes": file_size,
                "analysis": "Document properties extracted"
            }
            
            if file_ext == ".pdf":
                result["type"] = "PDF Document"
            elif file_ext == ".docx":
                result["type"] = "Word Document"
            else:
                result["type"] = "Unknown Document Type"
            
            return result
        
        except Exception as e:
            return {"status": "error", "message": str(e)}
