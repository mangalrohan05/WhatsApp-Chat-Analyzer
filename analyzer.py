import pandas as pd
import re
from collections import Counter
import emoji
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

toxic_model = pickle.load(open("model/toxic_model.pkl", "rb"))
tfidf = pickle.load(open("model/tfidf.pkl", "rb"))

lemma = WordNetLemmatizer()
st = set(stopwords.words('english'))
st.discard('not')

sia = SentimentIntensityAnalyzer()

pattern = r"(\d{1,2}/\d{2}/\d{2,4}),\s(\d{1,2}:\d{2}\s(?:AM|PM))\s-\s([^:]+):\s(.*)"

def preprocess(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join([lemma.lemmatize(w) for w in text.split() if w not in st])

def parse_chat(file):
    lines = file.read().decode("utf-8").split("\n")
    chats = []
    curr = None

    for line in lines:
        match = re.match(pattern, line)
        if match:
            if curr:
                chats.append(curr)
            curr = list(match.groups())
        else:
            if curr:
                curr[3] += " " + line

    if curr:
        chats.append(curr)

    df = pd.DataFrame(chats, columns=['Date', 'Time', 'Name', 'Message'])
    df = df[df["Name"].notna()]
    df["Message"] = df["Message"].apply(preprocess)
    return df

def sentiment(df):
    df["SentimentScore"] = df["Message"].apply(lambda x: sia.polarity_scores(x)["compound"])
    return df

def toxicity(df):
    vec = tfidf.transform(df["Message"])
    probs = toxic_model.predict_proba(vec)
    df["toxicity"] = probs.max(axis=1)
    return df

def analytics(df):
    user_activity = df['Name'].value_counts().to_dict()

    sentiment_trend = (
        df.groupby('Date')['SentimentScore']
        .mean()
        .reset_index()
    )

    words = " ".join(df['Message']).split()
    top_words = dict(Counter(words).most_common(20))

    return {
        "user_activity": user_activity,
        "sentiment_trend": {
            "dates": sentiment_trend['Date'].tolist(),
            "scores": sentiment_trend['SentimentScore'].tolist()
        },
        "top_words": top_words
    }

def run_pipeline(file):
    df = parse_chat(file)
    df = sentiment(df)
    df = toxicity(df)
    result = analytics(df)
    return result