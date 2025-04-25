# Import FPDF class for creating PDF documents
from fpdf import FPDF
# Import os module for interacting with the operating system
import os
# Import datetime class for handling date and time
from datetime import datetime

# Define a class for creating PDF reports
class PDFReport(FPDF):
    # Define the header of the PDF
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Web Research Report", border=False, ln=True, align="C")
        self.ln(10)

    # Define the footer of the PDF
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}", 0, 0, "C")

# Function to export content to a PDF file
def export_to_pdf(query: str, report_text: str, filename="output.pdf"):
    # Create a PDFReport object
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    # Add the user query to the PDF
    pdf.multi_cell(0, 10, f"User Query:\n{query}\n\n", align="L")

    # Add the report text to the PDF
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, report_text, align="L")

    # Define the output path and ensure the directory exists
    output_path = os.path.join("output", filename)
    os.makedirs("output", exist_ok=True)
    # Output the PDF to the specified path
    pdf.output(output_path)
    return output_path
