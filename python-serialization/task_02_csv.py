#!/usr/bin/python3
"""
2. Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
     Function that takes CSV file and writes
    the JSON data to data.json
      """
    try:
        with open(csv_filename) as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
