import datetime
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_report(file_name):
    pdf = PDF()
    pdf.add_page()

    pdf.set_font('Arial', '', 12)
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    pdf.cell(0, 10, f'Generated on: {current_time}', 0, 1)

    pdf.output(file_name)

if __name__ == '__main__':
    create_pdf_report('report.pdf')