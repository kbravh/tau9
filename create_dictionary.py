"""
Uses a raw csv of words and creates a dictionary ordered by word frequency.
  Nota bene: All dictionaries should be concatenated before this point.
"""

import csv
import sys
from util import wordToKeypad

input_file = sys.argv[1]
output_file = "dictionary.csv"

frequencies = {}

with open(input_file, 'r') as csv_input:
  reader = csv.reader(csv_input)
  for row in reader:
    word = row[0].lower()
    frequencies[word] = frequencies.get(word, 0) + 1

with open(output_file, 'w') as csv_output:
  writer = csv.DictWriter(csv_output, fieldnames=["word", "sequence"])
  for word,count in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
    sequence = wordToKeypad(word)
    writer.writerow({"word": word, "sequence": sequence})

with open(input_file, 'r') as csv_input:
  with open(output_file, 'w') as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.DictWriter(csv_output, fieldnames=["word", "sequence"])
    writer.writeheader()
    for row in reader:
      word = row[0]
      writer.writerow({"word": word, "sequence": wordToKeypad(word)})
