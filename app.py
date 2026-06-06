import streamlit as st
import pandas as pd
import plotly.express as px
from sentiment import analyze_sentiment
from database import save_result, fetch_results
from news_fetcher import get_news
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Real-Time Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Real-Time Sentiment Dashboard")

# -------------------------
# Manual Sentiment Analysis
# -------------------------

st.header("✍️ Manual Sentiment Analysis")

text = st.text_area("Enter Text")

if st.button("Analyze Text"):

    if text:

        result = analyze_sentiment(text)

        sentiment = result["label"]
        confidence = result["score"] * 100

        save_result(
            text,
            sentiment,
            confidence
        )

        st.success(
            f"{sentiment} ({confidence:.2f}%)"
        )

# -------------------------
# News Sentiment Analysis
# -------------------------

st.header("📰 Live News Sentiment Analysis")

topic = st.text_input(
    "Enter Topic",
    placeholder="Tesla, ChatGPT, Bitcoin..."
)

if st.button("Analyze Live News"):

    headlines = get_news(topic)

    if headlines:

        results = []

        for headline in headlines:

            sentiment = analyze_sentiment(headline)

            results.append({
                "Headline": headline,
                "Sentiment": sentiment["label"],
                "Confidence": round(
                    sentiment["score"] * 100,
                    2
                )
            })

        news_df = pd.DataFrame(results)

        st.subheader("News Headlines")

        st.dataframe(
            news_df,
            use_container_width=True
        )

        sentiment_counts = (
            news_df["Sentiment"]
            .value_counts()
        )

        fig = px.pie(
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            title=f"{topic} Sentiment Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Word Cloud
        all_headlines = " ".join(
            news_df["Headline"]
        )

        wc = WordCloud(
            width=800,
            height=400,
            background_color="white"
        ).generate(all_headlines)

        st.subheader("☁️ News Word Cloud")

        fig2, ax = plt.subplots(
            figsize=(10, 5)
        )

        ax.imshow(wc)

        ax.axis("off")

        st.pyplot(fig2)

# -------------------------
# Database Records
# -------------------------

st.header("💾 Saved Records")

records = fetch_results()

if records:

    db_df = pd.DataFrame(
        records,
        columns=[
            "ID",
            "Text",
            "Sentiment",
            "Confidence"
        ]
    )

    st.dataframe(
        db_df,
        use_container_width=True
    )

    csv = db_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📥 Download CSV",
        csv,
        "sentiment_data.csv",
        "text/csv"
    )