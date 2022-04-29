import sys

from parse import parser_pdf
doc1 = str(sys.argv[1])
doc2 = str(sys.argv[2])

# print(doc1)
# print(doc2)
if __name__ == '__main__':
    parser_pdf(doc1,doc2)
