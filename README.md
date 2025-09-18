

## Ghanaian Twitter Sentiment Analysis Dashboard (MVP)

This project analyses sentiment in Ghanaian tweets, Twi-English specifically using a fine-tuned pretrained transformer model, AfriBerta.
It includes scripts for predicting sentiments in batches of sample data, aggregating sentiments by percentage and visualising mood summaries in a simple console dashboard.

These batches of sample data are preprocessed data split into slices, and named in 'weeks' to simulate public mood tracking over time spans.


### 📂 Project Structure
```
├── datasets/
|   ├── original_data/                   # Raw unprocessed data (for use in replicating the data preprocessing process)
│   ├── preprocessed_data/               # Preprocessed training/validation data (used in training the transformer model)
│   ├── sample_data/                     # Week-sliced datasets (data split into slices of week1.csv, week2.csv and week3.csv.)
│   └── sample_data/script_output_data/  # Prediction outputs (created when model is run)
│
├── model/                # Trained model files (downloaded from Hugging Face when model is run. Ignored in GitHub)
│
├── scripts/
│   ├── model_predict.py          # Predict sentiments for weekly datasets
│   ├── aggregate_sentiment.py    # Aggregate predictions into summaries + samples
│   ├── run_dashboard.py          # Simple console dashboard with weekly sentiment overview
│   └── upload_model.py           # Code to upload model files to Hugging Face
|
├── notebooks/
│   ├── finetuned_model_training.ipynb                             # Train and fine-tune pretrained model AfriBerta
│   ├── preprocessing.ipynb                                        # Preprocess raw data in the datasets/original_data for use in finetuned_model_training.ipynb
│   ├── other_experiments/baseline_model.ipynb/                    # Training experiment with TDF + Logistic Regression model (optional)
│   └── other_experiments/sample_data_simulated_weeks_split.ipynb/ # Split dataset into 'weekX'.csvs 
│
├── results/                      # Saved model checkpoints (ignored in GitHub)
│
├── .gitignore
├── README.md
├── environment.yml               # Environment packages and tools with versions to run notebooks
└── requirements.txt              # Packages and dependencies needed to run scripts
```


<br>

### ⚙️ Requirements
Install dependencies with:  
pip install -r requirements.txt


### 🚀 How to Install/Run the Code
#### 1. Prepare Data  
Ensure your weekly CSV datasets (week1.csv, week2.csv and week3.csv) are in datasets/sample_data:  

- datasets/sample_data/week1.csv  
- datasets/sample_data/week2.csv  
- datasets/sample_data/week3.csv

Each CSV should have at least a tweet column.  
Any additional CSV must follow this naming order - 'week...'.csv.

#### 2. Run Predictions
Ensure you are in the root directory from your terminal   

Run the prediction script with this command:  
python scripts/model_predict.py

Select a week interactively.  
You’ll see a menu to choose week1, week2, or week3.

Predictions are saved automatically in:  
datasets/sample_data/script_output_data/weekX_with_predictions.csv


#### 3. View Dashboard
After predictions, the dashboard runs automatically, showing:

- Summary statement (e.g., “In Week 1, Ghanaians are feeling mostly happy.”)

- Sentiment distribution (positive/negative/neutral %)

- Sample tweets from each sentiment

*aggregate_sentiment.py runs in the background before run_dashboard.py is run.*


#### If you want to re-run the dashboard manually (Optional): 

python scripts/run_dashboard.py --week datasets/sample_data/script_output_data/weekX_with_predictions.csv
*This only works if predictions have been created by running the model_predict.py*


### *Example Output*

📅 Mood Summary for Week1:
   In Week1, Ghanaians are feeling mostly happy or positive.

   Sentiment Distribution:  
     Positive: 65.2%    
     Negative: 20.1%  
     Neutral: 14.7%

   Sample Tweets:
   - (positive) Wo ho yɛ fɛ paa!
   - (negative) Dumsor no bɔ me brɛ
   - (neutral) Eii saa?


<br>

### 🔒 Notes
The contents of the trained model folder (model/) and results (results/) folder are ignored in GitHub to keep repo size small.

If you want to replicate results, you’ll need the fine-tuned model.  
This will automatically be downloaded from Hugging Face when you run the model_predict.py to run the model.

(Optional): You can train it yourself using the notebooks in the (notebooks/) folder and datasets/preprocessed_data/.  
This will download the AfriBerta model from Hugging Face.  
***Ensure that you change paths in the notebooks according to your machine and user***


#### 📌 Future Improvements
- Deploy interactive dashboard as a web app (e.g., Streamlit).
- Add visualization plots for sentiment trends over weeks and topics.
- Automate weekly updates with cron jobs.

<br>

**Author**  
Naa Shidaa Addo – Project development and documentation.

