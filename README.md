# PDF Table Extractor

A Python script to extract tables from PDF documents and save them as CSV files.

## Requirements

- Python 3.6 or higher
- Java Runtime Environment (JRE) - required by tabula-py
- Required Python packages (install using requirements.txt)

## Installation

1. Clone this repository or download the files
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line with two required arguments:

```bash
python extract_tables.py <path_to_pdf> <output_directory>
```

Example:
```bash
python extract_tables.py document.pdf output/
```

This will:
1. Extract all tables from `document.pdf`
2. Save each table as a separate CSV file in the `output/` directory
3. Name the files sequentially as `table_1.csv`, `table_2.csv`, etc.

## Output

- Each table found in the PDF will be saved as a separate CSV file
- Files are named sequentially: `table_1.csv`, `table_2.csv`, etc.
- The script will create the output directory if it doesn't exist
- Empty tables are skipped

## Error Handling

The script includes basic error handling for:
- Missing PDF file
- Invalid file type
- Invalid file path