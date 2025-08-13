from __future__ import annotations
import csv
import json
import re
from datetime import datetime
from pathlib import Path

# --- Settings ---
csv_file = Path("test.csv")
sql_file = Path("data.sql")
nosql_file = Path("data.json")
table_name = csv_file.stem  # table name from file name

def detect_type(value: str) -> str:
    """Guess SQL data type based on value."""
    if not value:
        return "TEXT"

    match value:
        case _ if re.fullmatch(r"-?\d+", value):
            return "INT"
        case _ if re.fullmatch(r"-?\d+\.\d+", value):
            return "REAL"
        case _:
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return "DATE"
            except ValueError:
                return "TEXT"

# --- Read CSV ---
with csv_file.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    headers = reader.fieldnames or []

# --- Determine column types ---
col_types: dict[str, str] = {}
for header in headers:
    detected_types = {detect_type(row[header]) for row in rows if row[header]}
    col_types[header] = detected_types.pop() if len(detected_types) == 1 else "TEXT"

# --- Create SQL file ---
with sql_file.open("w", encoding="utf-8") as f:
    # CREATE TABLE
    f.write(f"CREATE TABLE {table_name} (\n")
    f.write(",\n".join([f"  `{col}` {col_types[col]}" for col in headers]))
    f.write("\n);\n\n")

    # INSERT statements
    for row in rows:
        values: list[str] = []
        for h in headers:
            val = row[h]
            if not val:
                values.append("NULL")
            elif col_types[h] in ("INT", "REAL"):
                values.append(val)
            else:
                # Escape single quotes inside string
                escaped_val = val.replace("'", "''")
                values.append(f"'{escaped_val}'")
        f.write(f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(values)});\n")

print(f"SQL file created: {sql_file}")

# --- Create NoSQL JSON file ---
with nosql_file.open("w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=4)

print(f"NoSQL JSON file created: {nosql_file}")
