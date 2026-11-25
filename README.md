# WhatsApp Chat Analyzer 📊

> Transform raw WhatsApp chat exports into rich NLP insights — activity heatmaps, word clouds, sentiment analysis, and per-user breakdowns.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-red?logo=streamlit)](https://streamlit.io)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://whats-app-chat-analyzer-virid.vercel.app)

🚀 **[Live Demo](https://whats-app-chat-analyzer-virid.vercel.app)**

## Features

- **Message Statistics** — total messages, words, media, links; overall and per-user
- **Activity Heatmap** — message frequency by day of week × hour of day
- **Word Cloud** — most common words (stopwords removed) for group or individual
- **Sentiment Analysis** — positive / negative / neutral message classification per user
- **Top Contributors** — bar chart of most active members
- **Monthly & Daily Timelines** — message volume over time
- **Emoji Analysis** — most used emojis per user

## Tech Stack

| Component | Technology |
|---|---|
| Backend / NLP | Python, NLTK |
| Visualisation | Matplotlib, WordCloud |
| Frontend | Streamlit |
| Parsing | Custom regex WhatsApp parser |

## Setup

```bash
git clone https://github.com/mangalrohan05/WhatsApp-Chat-Analyzer
cd WhatsApp-Chat-Analyzer
pip install -r requirements.txt
streamlit run app.py
```

Export a WhatsApp chat (without media) and upload the .txt file in the app.

## Project Structure

```
WhatsApp-Chat-Analyzer/
├── analyzer.py      # Core NLP & stat functions
├── app.py           # Streamlit web app
├── model/           # Sentiment model artifacts
└── requirements.txt
```