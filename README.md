# Text Summarizer

## 📌 Introduction
The **Text Summarizer** is a Python-based application that helps users generate concise summaries from large text documents. It utilizes Natural Language Processing (NLP) techniques to extract the most important information while maintaining coherence.

## 🚀 Features
- Supports summarization of plain text, PDFs, and Word documents (.docx)
- Uses **LexRank Algorithm** for efficient text summarization
- **GUI-based interface** using Tkinter for easy interaction
- **File Import Option** for uploading documents
- Allows users to **copy summaries to clipboard**
- **Saves output as a text file**
- **Dark Mode & Light Mode Toggle** for better usability
- Works completely offline

## 🛠️ Installation

### Prerequisites
Ensure you have **Python 3.8+** installed.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Burhanali2211/Text-Summarizer.git
cd text-summarizer
```

### 2️⃣ Install Dependencies
Run the following command to install required Python packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Required NLTK Resources
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## 🎯 Usage

### Run the application
```bash
python Text_Summarizer.py
```

### How to Use
1. **Enter or Upload Text**: Paste text or load a file (PDF, DOCX, or TXT).
2. **Click Summarize**: The tool extracts the key points.
3. **Copy or Save**: Copy the summary to the clipboard or save it as a file.

## 📜 Requirements (requirements.txt)
```
nltk
sumy
pdfplumber
python-docx
PyPDF2
tkinter
```

## 🛠️ Troubleshooting
- **Error: Missing NLTK Data**
  Run the following in Python:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```
- **GUI not opening?** Ensure Tkinter is installed (pre-installed with Python).

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Added a new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a Pull Request

## 📄 License
This project is licensed under the MIT License.

