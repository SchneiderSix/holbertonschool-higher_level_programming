#!/usr/bin/python3
"""Module"""


import json
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fp = 'add_item.json'
li = []

if os.path.exists(fp) and os.path.getsize(fp) > 0:
    li = load_from_json_file(fp)

if len(sys.argv) > 1:
    for ele in len(sys.argv[1:]):
        li.append(i)
save_to_json_file(li, fp)
