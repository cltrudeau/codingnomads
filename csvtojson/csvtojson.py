#!/usr/bin/env python
"""
CSV to JSON: A Data Tranformation/Cleaning Example
--------------------------------------------------

This script reads the file "data/orders.csv", deletes the "Region" column,
converts the date column from ISO 8601 format to American month/day/year, and
outputs the result as JSON.
"""

import csv, json
from datetime import datetime

# ---------------------------------------------------------------------------

orders = []

# Read CSV file, removing the Region column and changing the date format
with open('data/orders.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        del row['Region']
        euro_date = datetime.strptime(row['Date'], '%Y-%m-%d')
        row['Date'] = euro_date.strftime('%m/%d/%Y')
        orders.append(row)

# Output result to JSON
result = json.dumps(orders, indent=4, sort_keys=True)
print(result)
