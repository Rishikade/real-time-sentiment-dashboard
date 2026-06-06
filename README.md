# 📊 Real-Time Sentiment Dashboard

A real-time NLP dashboard built using Streamlit, Hugging Face Transformers, NewsAPI, SQLite, and Plotly.

## Features

- Sentiment Analysis using Hugging Face Transformers
- Live News Sentiment Analysis
- SQLite Database Storage
- Interactive Pie Charts
- Word Cloud Visualization
- CSV Export

## Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- NewsAPI
- SQLite
- Plotly
- Pandas
- WordCloud
- Git & GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/Rishikade/real-time-sentiment-dashboard.git
cd real-time-sentiment-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
NEWS_API_KEY=your_news_api_key
```

## Run the Application

```bash
streamlit run app.py
```

## Project Structure

```text
├── app.py
├── sentiment.py
├── database.py
├── news_fetcher.py
├── requirements.txt
├── README.md
└── .env
```

## Author

Rishika De
