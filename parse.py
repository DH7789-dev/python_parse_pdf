import sys
import pdfplumber


# doc1 = str(sys.argv[1])
# doc2 = str(sys.argv[2])

# print(doc1)
# print(doc2)

def parser_pdf(docEnter, docExit):
    pdf = pdfplumber.open("23 - Potentiel nation DOC relativité Non start .pdf")
    with open("cc2.text", "a", encoding='utf-8', errors='surrogateescape') as file:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            print(text)
            file.write(text)
        file.close()
        pdf.close()
