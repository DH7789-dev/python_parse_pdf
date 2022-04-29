import sys
import pdfplumber




def parser_pdf(docEnter, docExit):
    pdf = pdfplumber.open(docEnter)
    with open(docExit, "a", encoding='utf-8', errors='surrogateescape') as file:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            print(text)
            file.write(text)
        file.close()
        pdf.close()
