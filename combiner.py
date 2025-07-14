#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 3:
        continue
    hour, topic, count = parts
    key = f"{hour}\t{topic}"
    count = int(count)

    if current_key == key:
        current_count += count
    else:
        if current_key:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = count

if current_key:
    print(f"{current_key}\t{current_count}")