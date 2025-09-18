import pandas as pd
from collections import Counter

def aggregate_sentiment(predictions_file, sentiment_col="predicted_sentiment", sample_n=3):
    df = pd.read_csv(predictions_file)

    counts = Counter(df[sentiment_col])
    total = sum(counts.values())
    distribution = {label: f"{(count/total)*100:.1f}%" for label, count in counts.items()}

    samples = df.groupby(sentiment_col).apply(
        lambda x: x.sample(min(sample_n, len(x)))["tweet"].tolist()
    ).to_dict()

    return distribution, samples


