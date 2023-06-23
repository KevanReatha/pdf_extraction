# PDF Extraction Project

The PDF Extraction project is a Python-based solution that automates the extraction of invoice data from PDF files. The project aims to streamline the process of gathering invoice information by parsing PDF documents and converting them into structured data for further analysis or processing.

## Features:

Extraction of Invoice Data: The project utilizes the PyPDF2 library to read and extract textual content from PDF invoices.
Invoice Parsing: The extracted content is parsed to identify specific charges mentioned in the invoices.
Data Transformation: The parsed data is transformed into a structured format, making it easier to analyze and work with.
CSV Export: The extracted and transformed data is saved as a CSV file for convenient storage and sharing.

## Usage:

Place PDF invoice files in the specified directory.
Run the script to automatically extract and parse the invoice data.
The extracted data is saved as a CSV file named "test.csv" for further analysis or processing.

##Dependencies:
The project relies on the following Python libraries:

- PyPDF2: Used for reading and extracting text from PDF documents.
- pandas: Used for creating and manipulating structured data in tabular form.
