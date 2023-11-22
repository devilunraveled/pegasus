from PyPDF2 import PdfReader

def Parser( pdfFile = None):
    # First task is to convert the pdf file to a text file.
    if pdfFile is None:
        return None

    reader = PdfReader(pdfFile)
    content = ""
    
    for page in reader.pages:
        content += page.extract_text()
    
    with open(pdfFile.replace('.pdf', '.txt'), 'w') as f:
        f.write(content)

    return content


if __name__ == "__main__":
    Parser()
