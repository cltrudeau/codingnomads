#!/usr/bin/env python

from pathlib import Path
import unicodedata

output = []
filename = Path(__file__).parent.resolve() / "data/books.tsv"

with open(filename) as handle:
    lines = handle.readlines()

# lines will contain a row for each line in the file

# Loop through lines and do data scrubbing, put each result in output
for line in lines:
    fields = line.split('\t')

    # Start with known blank values
    num = fields[0]
    last_name = ''
    first_name = ''
    title = ''
    date = ''
    subjects = ''

    if len(fields) > 1:
        # Has a "name" field
        parts = fields[1].split(',')
        first_name = ''
        last_name = parts[0]

        if len(parts) > 1:
            first_name = parts[1]

            if "(" in first_name:
                first_name, _ = first_name.split('(')

    if len(fields) > 2:
        title = fields[2]
        nfkd_form = unicodedata.normalize('NFKD', title)
        title = nfkd_form.encode('ASCII', 'ignore')
        title = title.decode('utf-8')

    out_line = f'{num}\t{last_name}\t{first_name}\t{title}'
    output.append(out_line)


for line in output:
    print(line)
