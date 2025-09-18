import os
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from run_dashboard import run_dashboard 

# MODEL_PATH = "model/sentiment_model"
MODEL_PATH = "rainaans/twi-sentiment-model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

label_map = {0: 'negative', 1: 'positive', 2: 'neutral'}

def predict_sentiments(tweets):
    inputs = tokenizer(
        tweets,
        padding=True,
        truncation=True,
        max_length=64,
        return_tensors="pt"
    )
    with torch.no_grad():
        outputs = model(**inputs)
        preds = torch.argmax(outputs.logits, dim=-1).cpu().numpy()
    return [label_map[p] for p in preds]

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "../datasets/sample_data")
    OUTPUT_DIR = os.path.join(INPUT_DIR, "script_output_data")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    weeks = [f for f in os.listdir(INPUT_DIR) if f.startswith("week") and f.endswith(".csv")]
    weeks.sort()

    if not weeks:
        print("No weekly CSV files found in:", INPUT_DIR)
        exit(1)

    while True:
        print("\nSelect a week file for predictions:")
        for i, w in enumerate(weeks, start=1):
            print(f"{i}. {w}")
        print("q. Quit")

        choice = input("\nEnter number (or q to quit): ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            print("Exiting.")
            exit(0)

        if not choice.isdigit() or not (1 <= int(choice) <= len(weeks)):
            print("Invalid input, try again.")
            continue

        week_file = weeks[int(choice) - 1]
        break

    input_path = os.path.join(INPUT_DIR, week_file)
    df = pd.read_csv(input_path)
    df["predicted_sentiment"] = predict_sentiments(df["tweet"].tolist())

    output_file = os.path.join(OUTPUT_DIR, week_file.replace(".csv", "_with_predictions.csv"))
    df.to_csv(output_file, index=False)

    print(f"\n Predictions saved to {output_file}")

    # Auto-run dashboard
    run_dashboard(output_file)
