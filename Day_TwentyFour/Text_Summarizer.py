import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
import docx
import PyPDF2

# Text-to-Speech
engine = pyttsx3.init()


def summarize_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter some text or load a file!")
        return

    summary_ratio = float(length_var.get()) / 100
    algorithm = algo_var.get()

    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    summarizers = {
        "LSA": LsaSummarizer(),
        "LexRank": LexRankSummarizer(),
        "Luhn": LuhnSummarizer()
    }

    summarizer = summarizers[algorithm]
    summary = summarizer(parser.document, int(
        len(parser.document.sentences) * summary_ratio))

    summarized_text = "\n".join(str(sentence) for sentence in summary)
    summary_output.delete("1.0", tk.END)
    summary_output.insert(tk.END, summarized_text)


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[(
        "Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word files", "*.docx")])
    if not file_path:
        return

    text = ""
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    elif file_path.endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = " ".join(page.extract_text()
                            for page in reader.pages if page.extract_text())
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = "\n".join(para.text for para in doc.paragraphs)

    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, text)


def save_summary():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(summary_output.get("1.0", tk.END))
        messagebox.showinfo("Saved", "Summary saved successfully!")


def read_aloud():
    text = summary_output.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showerror("Error", "No summary available to read aloud!")


# GUI Setup
root = tk.Tk()
root.title("Enhanced Text Summarizer")
root.geometry("700x600")

tk.Label(root, text="Enter or Load Text:").pack()
text_input = tk.Text(root, height=10)
text_input.pack()

btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Load File",
          command=load_file).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Summarize",
          command=summarize_text).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Save Summary",
          command=save_summary).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Read Aloud",
          command=read_aloud).pack(side=tk.LEFT, padx=5)

# Summary Settings
tk.Label(root, text="Summary Length (%):").pack()
length_var = tk.StringVar(value="30")
tk.Entry(root, textvariable=length_var).pack()

algo_var = tk.StringVar(value="LSA")
tk.Label(root, text="Algorithm:").pack()
tk.OptionMenu(root, algo_var, "LSA", "LexRank", "Luhn").pack()

# Summary Output
summary_output = tk.Text(root, height=10)
summary_output.pack()

root.mainloop()
