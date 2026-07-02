import pickle
import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "Reviews.csv"
MODEL_PATH = BASE_DIR / "sentiment_model_pipeline.pkl"


def clean_text(text):
    """Clean review text by removing HTML, URLs, punctuation, and extra whitespace."""
    if not isinstance(text, str):
        return ""

    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def prepare_dataset(data_path=None):
    """Load the reviews CSV and create a simple label column for sentiment."""
    data_path = Path(data_path or DATASET_PATH)
    df = pd.read_csv(data_path)

    if "Text" not in df.columns or "Score" not in df.columns:
        raise ValueError("Expected 'Text' and 'Score' columns in the dataset.")

    df["review_text"] = df["Summary"].fillna("") + " " + df["Text"].fillna("")
    df["review_text"] = df["review_text"].apply(clean_text)
    df = df[df["review_text"].str.len() > 0]

    df["sentiment"] = df["Score"].apply(
        lambda score: 2 if score > 3 else 1 if score == 3 else 0
    )

    return df[["review_text", "sentiment"]]


def train_model(data_path=None, model_path=None, sample_size=60000):
    """Train a lightweight text classification model and save it to disk."""
    dataset = prepare_dataset(data_path)

    if sample_size and len(dataset) > sample_size:
        dataset = dataset.sample(n=sample_size, random_state=42)

    X = dataset["review_text"]
    y = dataset["sentiment"]

    pipeline = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=2,
                    max_features=50000,
                ),
            ),
            ("classifier", MultinomialNB(alpha=0.5)),
        ]
    )

    pipeline.fit(X, y)

    target_path = Path(model_path or MODEL_PATH)
    with target_path.open("wb") as handle:
        pickle.dump(pipeline, handle)

    return pipeline


def load_model(model_path=None):
    """Load a trained pipeline from disk, or train one if it does not exist."""
    target_path = Path(model_path or MODEL_PATH)
    if target_path.exists():
        with target_path.open("rb") as handle:
            return pickle.load(handle)

    return train_model(model_path=target_path)


def predict_sentiment(text, model_path=None):
    """Predict a sentiment label for a single review string."""
    if not text or not str(text).strip():
        return None

    pipeline = load_model(model_path)
    prediction = pipeline.predict([clean_text(text)])[0]
    return int(prediction)


def get_sentiment_label(prediction):
    """Convert numeric prediction to a display label."""
    mapping = {2: "Positive", 1: "Neutral", 0: "Negative"}
    return mapping.get(int(prediction), "Unknown")
