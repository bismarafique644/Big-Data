#!/usr/bin/env python3
import sys
import csv
from datetime import datetime
import re

def clean_text(text):
    text = re.sub(r"http\S+|@\S+|#\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.lower()

reader = csv.DictReader(sys.stdin, delimiter='\t')
for row in reader:
    timestamp = row.get("tweet_created", "")
    text = row.get("text", "")
    if not timestamp or not text:
        continue
    try:
        dt = datetime.strptime(timestamp, "%m/%d/%Y %H:%M")
        hour = dt.strftime("%Y-%m-%d %H")
    except Exception:
        continue
    clean = clean_text(text)
    for token in clean.split():
        if len(token) > 2:
            print(f"{hour}\t{token}\t1")