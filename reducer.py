#!/usr/bin/env python3
import sys
from collections import defaultdict, Counter

current_hour = None
topic_counts = defaultdict(int)
TOP_N = 10

def output_top_topics(hour, counts):
    top = Counter(counts).most_common(TOP_N)
    line = f"{hour}\t" + ",".join([f"{topic}:{count}" for topic, count in top])
    print(line)

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 3:
        continue
    hour, topic, count = parts
    count = int(count)
    if current_hour is None:
        current_hour = hour
    if hour != current_hour:
        output_top_topics(current_hour, topic_counts)
        topic_counts = defaultdict(int)
        current_hour = hour
    topic_counts[topic] += count

if current_hour is not None:
    output_top_topics(current_hour, topic_counts)