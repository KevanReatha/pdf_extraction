from PyPDF2 import PdfReader
import os
import re
from datetime import datetime
import pandas as pd

def extract_invoice_data_from_pdf(invoice_files, charges_list):
    """
    Extracts invoice data from PDF files and returns a pandas DataFrame.

    Args:
        invoice_files (list): List of PDF invoice filenames.
        charges_list (list): List of charges to extract from invoices.

    Returns:
        pandas.DataFrame: DataFrame containing the extracted invoice data.
    """
    line_items = []
    line_items_2 = []

    for invoice in invoice_files:
        invoice_number = invoice.split("_")[:2][0][-3:] + "-" + invoice.split("_")[:2][1]
        invoice_date = datetime.strptime(invoice.split("_")[2][-10:].split(".")[0], '%y%m%d').date()

        # Read content
        reader = PdfReader(invoice)
        page_extract = ""

        for page_number in range(2):
            page = reader.pages[page_number]
            page_extract += page.extract_text()

        # Read line items of invoice
        for charge in charges_list:
            try:
                charge_id = charge[0]
                details = charge + str(re.search(rf"(?<={charge_id}).*", page_extract)[0]).split()
                # Add details to line items list
                line_items.append(details)
                detail_2 = [invoice] + [invoice_number] + [invoice_date.strftime("%d/%m/%Y")] + details
                line_items_2.append(detail_2)
            except:
                pass

    df = pd.DataFrame(line_items_2,
                      columns=['Invoice', 'Invoice number', 'Invoice date', 'Description of charges',
                               'Invoice amount', 'Charge amount', 'Currency', 'Tax rate'])

    return df


def main():
    invoice_directory = '/Users/kevantamom/Desktop/Aesop Ceva Invoices Reader'
    charges_list = [['YARD STORAGE COYNES 8 DAYS'],
                    ['TERMINAL OFFLOADING CHARGE'],
                    ['ORIGIN PORT CHARGES'],
                    ['CUSTOMS CLEARANCE'],
                    ['ADMINISTRATION FEE'],
                    ['DANGEROUS GOODS FEE'],
                    ['ORIGIN PICK UP'],
                    ['HANDLING & PROCESSING'],
                    ['FCL FREIGHT OCEAN'],
                    ['CARRIER DG SURCHARGE'],
                    ['BAF'],
                    ['DESTINATION PORT CHARGES'],
                    ['DEST. CHARGES BILLING'],
                    ['DEST. CONT. DRAYAGE'],
                    ['DEST. HAULAGE DG SURCH'],
                    ['DEST. CUSTOMS CLEARANCE'],
                    ['DEST. FUEL SURCHARGE'],
                    ['DEST. DELIVERY BILLING'],
                    ['WAITING TIME TTL 0.25'],
                    ['LOW SULPHUR SURCHARGE'],
                    ['PANAMA CANAL SURCHARGE'],
                    ['CONGESTION SURCHARGE'],
                    ['WAITING TIME TTL 0.50'],
                    ['DEST. ISF FILING'],
                    ['FUTILE CONTAINER TRIP'],
                    ['AFTER HOURS DELIVERY SAT'],
                    ['CHASSIS CHARGE-CARRIER'],
                    ['YARD STORAGE COYNES 29 DAY'],
                    ['DOCUMENTATION FEE']]

    # Get list of invoice files in the directory
    invoice_files = [file for file in os.listdir(invoice_directory) if file.startswith("Ceva")]

    # Extract invoice data from PDF files
    df = extract_invoice_data_from_pdf(invoice_files, charges_list)

    # Save DataFrame as CSV
    df.to_csv("test.csv")


if __name__ == "__main__":
    main()
