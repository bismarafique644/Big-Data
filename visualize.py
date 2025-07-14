import pandas as pd
import matplotlib.pyplot as plt

data = []
with open('output.txt') as f:
    for line in f:
        hour, topics = line.strip().split('\t')
        for topic_count in topics.split(','):
            topic, count = topic_count.split(':')
            data.append([hour, topic, int(count)])

df = pd.DataFrame(data, columns=['hour', 'topic', 'count'])
pivot = df.pivot_table(index='hour', columns='topic', values='count', fill_value=0)

pivot.plot(kind='line', figsize=(14,7))
plt.title("Hourly Trending Topics")
plt.ylabel("Count")
plt.xlabel("Hour")
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()