from PyPDF2 import PdfFileMerger

pdfs = ['pdf1.pdf', 'pdf2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("mergedPDF.pdf")
merger.close()