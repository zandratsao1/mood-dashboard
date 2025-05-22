import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/mood_bot.csv")

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Optional: Sort by time
df = df.sort_values(by='timestamp')

plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['mood'], marker='o', linestyle='-', alpha=0.7)
plt.title('Mood Over Time')
plt.xlabel('Date')
plt.ylabel('Mood')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

mood_counts = df['mood'].value_counts()

plt.figure(figsize=(8, 5))
mood_counts.plot(kind='bar', color='skyblue')
plt.title('Mood Frequency')
plt.xlabel('Mood')
plt.ylabel('Count')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
