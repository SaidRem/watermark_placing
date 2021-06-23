import PyPDF2
import os

def watermarking(pdf_files, watermark):
    os.makedirs('watermarked_pdfs', exist_ok=True)
    pdfs_f = list(filter(lambda x: x.endswith('.pdf'), os.listdir('.')))
    pass