# Miryo Document Reader

A local document-reading tool for Claude Code, developed as part of the MiryoLove project.

## Supported formats

- TXT
- DOCX
- XLSX
- XLS
- PDF with extractable text

## Requirements

Python 3 and the packages listed in requirements.txt.

On Arch Linux:

    sudo pacman -S python-docx python-openpyxl python-xlrd python-pypdf

## Usage

    python scripts/miryo_read_file.py "/path/to/document.docx"

The tool extracts document text locally and does not intentionally modify the source file.

Scanned PDFs and image OCR are not currently supported by the extraction script.

## Project

Part of MiryoLove.

## Copyright

Copyright © 2026 Bogdan Melnikov.

MiryoLove is an independent project created by Bogdan Melnikov.

All original source code, project architecture, documentation, and original materials are protected under applicable copyright laws.

Third-party libraries, dependencies, and other external materials remain distributed under their respective licenses.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
See the `LICENSE` file for the full license text.
