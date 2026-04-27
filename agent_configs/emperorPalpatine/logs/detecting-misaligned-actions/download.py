import urllib.request
import json
import os
import subprocess

with open('next_paper.json') as f:
    paper = json.load(f)

pdf_url = "https://koala.science" + paper["pdf_url"]
print("Downloading PDF from:", pdf_url)
urllib.request.urlretrieve(pdf_url, "logs/detecting-misaligned-actions/paper.pdf")

# extract text
subprocess.run(["pdftotext", "logs/detecting-misaligned-actions/paper.pdf", "logs/detecting-misaligned-actions/paper.txt"])
print("Extracted paper.txt")
