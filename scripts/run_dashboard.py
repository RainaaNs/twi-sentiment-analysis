import argparse
import os
from aggregate_sentiment import aggregate_sentiment

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_dashboard(week_file):
    distribution, samples = aggregate_sentiment(week_file)

    dominant = max(distribution.items(), key=lambda x: float(x[1].replace("%", "")))[0]

    mood_map = {
        "positive": "happy",
        "negative": "unhappy",
        "neutral": "normal"
    }
    mood_word = mood_map.get(dominant, dominant)

    week_name = os.path.basename(week_file).replace("_with_predictions.csv", "").capitalize()

    print("\n =========== PUBLIC MOOD TRACKER DASHBOARD ==========")
    print(f"\n📅 Mood Summary for {week_name}:")
    print(f"   In {week_name}, Ghanaians are feeling mostly {mood_word} or {dominant}.\n")

    print("   Sentiment Distribution:")
    for label, percent in distribution.items():
        print(f"     {label.capitalize()}: {percent}")

    print("\n   Sample Tweets:")
    for label, tweets in samples.items():
        for t in tweets:
            print(f"   • ({label}) {t}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=str, required=True, help="Path to weekly CSV file")
    args = parser.parse_args()

    run_dashboard(args.week)

