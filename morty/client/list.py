#!/usr/bin/env python

import requests

response = requests.get('http://127.0.0.1:8000/core/all_images/')

print('Response code', response.status_code)
print('\nBody:')
print(response.text[:100])
print('...\n')
