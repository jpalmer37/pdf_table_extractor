#!/usr/bin/env python3

import argparse
import os
import tabula
import pandas as pd
from pathlib import Path

def extract_tables(pdf_path: str, output_dir: str) -> None:
    """
    Extract tables from a PDF file and save them as CSV files.
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_dir (str): Directory where extracted tables will be saved
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract all tables from the PDF
    print(f"Extracting tables from {pdf_path}...")
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    if not tables:
        print("No tables found in the PDF.")
        return
    
    # Save each table as a CSV file
    for i, df in enumerate(tables, 1):
        if not df.empty:
            output_path = os.path.join(output_dir, f"table_{i}.csv")
            df.to_csv(output_path, index=False)
            print(f"Saved table {i} to {output_path}")
    
    print(f"\nExtracted {len(tables)} tables from the PDF.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Extract tables from a PDF file and save them as CSV files"
    )
    parser.add_argument(
        "pdf_path",
        type=str,
        help="Path to the input PDF file"
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Directory where extracted tables will be saved"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Convert to Path objects and resolve
    pdf_path = Path(args.pdf_path).resolve()
    output_dir = Path(args.output_dir).resolve()
    
    # Validate input PDF file
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        return
    
    if not pdf_path.is_file():
        print(f"Error: {pdf_path} is not a file")
        return
        
    if pdf_path.suffix.lower() != '.pdf':
        print(f"Error: {pdf_path} is not a PDF file")
        return
    
    # Extract tables
    extract_tables(str(pdf_path), str(output_dir))

if __name__ == "__main__":
    main()