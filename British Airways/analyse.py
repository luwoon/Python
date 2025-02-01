import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk

df = pd.read_csv('BA_reviews_cleaned.csv')

# Word Cloud

text = " ".join(review for review in df['Review'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Sentiment Analysis

def get_sentiment(review):
    blob = TextBlob(review)
    return blob.sentiment.polarity

df['sentiment'] = df['Review'].apply(get_sentiment)

df['sentiment_label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

print(df[['Review', 'sentiment', 'sentiment_label']].head())

df['sentiment_label'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

positive_reviews = df[df['sentiment_label'] == 'Positive']
negative_reviews = df[df['sentiment_label'] == 'Negative']

positive_text = " ".join(positive_reviews['Review'])
negative_text = " ".join(negative_reviews['Review'])

positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(negative_text)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Reviews')

plt.subplot(1, 2, 2)
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Reviews')

plt.show()

# Topic Modelling

nltk.download('punkt_tab')
df['tokens'] = df['Review'].apply(lambda x: nltk.word_tokenize(x.lower()))

# Create a TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer to the reviews data
X = vectorizer.fit_transform(df['Review'])

# Fit LDA model
lda = LatentDirichletAllocation(n_components=3, random_state=42)
lda.fit(X)

# Display the top words for each topic
terms = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic #{topic_idx}:")
    print(" ".join([terms[i] for i in topic.argsort()[:-11:-1]]))