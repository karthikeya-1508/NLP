import pandas as pd
import sys
sys.path.append('.')
from model_train_and_predict import prepare_dataset, train_model, predict_sentiment

df = pd.read_csv('Reviews.csv')
text = 'Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as "Jumbo".'
subset = df[df['Text'].str.contains('Product arrived labeled as Jumbo Salted Peanuts', na=False)]
print('Matches in csv:', len(subset))
print(subset[['Score','Summary','Text']].head(5).to_string())

train_df = prepare_dataset('Reviews.csv')
print('Label mapping example for Score 1 ->', train_df[train_df['review_text'].str.contains('product arrived labeled as jumbo salted peanuts', na=False)]['sentiment'].unique())
model = train_model(sample_size=10000)
pred = predict_sentiment(text)
print('Predict sample text:', pred)
print('Label:', 'Positive' if pred==2 else 'Neutral' if pred==1 else 'Negative')
X = train_df['review_text'].sample(n=3000, random_state=42)
y = train_df.loc[X.index,'sentiment']
preds = model.predict(X)
print('Sample accuracy:', (preds==y).mean())
