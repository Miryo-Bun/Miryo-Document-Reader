#!/usr/bin/env python

import sys
from pathlib import Path

MAX_CHARS = 30000

def read_file(path):
    ext = path.suffix.lower()

    if ext == ".txt":
        return path.read_text(encoding="utf-8", errors="replace")

    if ext == ".docx":
        from docx import Document
        doc = Document(path)
        parts = [p.text for p in doc.paragraphs if p.text.strip()]
        for table in doc.tables:
            for row in table.rows:
                parts.append(" | ".join(cell.text for cell in row.cells))
        return "\n".join(parts)

    if ext == ".xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(path, read_only=True, data_only=True)
        parts = []
        for sheet in wb.worksheets:
            parts.append(f"\n=== Лист: {sheet.title} ===")
            for row in sheet.iter_rows(values_only=True):
                values = [str(v) if v is not None else "" for v in row]
                if any(values):
                    parts.append(" | ".join(values))
        wb.close()
        return "\n".join(parts)

    if ext == ".xls":
        import xlrd
        wb = xlrd.open_workbook(path)
        parts = []
        for sheet in wb.sheets():
            parts.append(f"\n=== Лист: {sheet.name} ===")
            for row in range(sheet.nrows):
                parts.append(" | ".join(str(v) for v in sheet.row_values(row)))
        return "\n".join(parts)

    if ext == ".pdf":
        from pypdf import PdfReader
        reader = PdfReader(path)
        return "\n".join(
            f"\n=== Страница {i + 1} ===\n{page.extract_text() or ''}"
            for i, page in enumerate(reader.pages)
        )

    raise ValueError(f"Неподдерживаемый формат: {ext}")

def main():
    if len(sys.argv) != 2:
        print("Использование: miryo-read-file <путь-к-файлу>")
        sys.exit(1)

    path = Path(sys.argv[1]).expanduser()

    if not path.is_file():
        print(f"Файл не найден: {path}")
        sys.exit(1)

    try:
        text = read_file(path)
        print(text[:MAX_CHARS])
        if len(text) > MAX_CHARS:
            print(f"\n[Вывод ограничен: показаны первые {MAX_CHARS} символов]")
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
