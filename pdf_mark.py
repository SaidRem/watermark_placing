import PyPDF2
from pathlib import Path
import os


def mark_pdfs(path_to, watermark):
    os.makedirs('marked_pdfs', exist_ok=True)
    path_to = Path(path_to)
    if not watermark.endswith('.pdf'):
        return 'Enter to pdf format of watermark'
    if path_to.is_dir():
        return 'Enter path to a pdf file'
    elif path_to.is_file() and path_to.suffix == '.pdf':
        with open(path_to, 'rb') as pdf, open(watermark, 'rb') as watermark:
            pdf_obj = PyPDF2.PdfFileReader(pdf)
            watermark_obj = PyPDF2.PdfFileReader(watermark)
            first_page = pdf_obj.getPage(0)
            first_page.mergePage(watermark_obj.getPage(0))
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(first_page)
            for page_num in range(1, pdf_obj.numPages):
                page_obj = pdf_obj.getPage(page_num)
                pdf_writer.addPage(page_obj)
            result_pdf = open(Path('marked_pdfs', path_to.stem + '_marked.pdf'), 'wb')
            pdf_writer.write(result_pdf)
            result_pdf.close()
    return 'Done'

