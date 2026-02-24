"""
AI Digital Evidence Analyzer
Main entry point for the application
"""

from analyzers.image_analyzer import ImageAnalyzer
from analyzers.document_analyzer import DocumentAnalyzer
from analyzers.log_analyzer import LogAnalyzer
import os

def main():
    print("=" * 50)
    print("AI DIGITAL EVIDENCE ANALYZER")
    print("=" * 50)
    print("\nWelcome! Choose what you want to analyze:\n")
    print("1. Image Analysis")
    print("2. Document Analysis")
    print("3. Log File Analysis")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        image_path = input("Enter path to image file: ")
        if os.path.exists(image_path):
            analyzer = ImageAnalyzer()
            result = analyzer.analyze(image_path)
            print("\n--- Image Analysis Result ---")
            print(result)
        else:
            print("File not found!")
    
    elif choice == "2":
        doc_path = input("Enter path to document file (PDF/DOCX): ")
        if os.path.exists(doc_path):
            analyzer = DocumentAnalyzer()
            result = analyzer.analyze(doc_path)
            print("\n--- Document Analysis Result ---")
            print(result)
        else:
            print("File not found!")
    
    elif choice == "3":
        log_path = input("Enter path to log file: ")
        if os.path.exists(log_path):
            analyzer = LogAnalyzer()
            result = analyzer.analyze(log_path)
            print("\n--- Log Analysis Result ---")
            print(result)
        else:
            print("File not found!")
    
    elif choice == "4":
        print("Thank you for using AI Digital Evidence Analyzer!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
