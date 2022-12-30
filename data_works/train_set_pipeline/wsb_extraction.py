import pandas as pd

df = pd.read_csv('./../timeseries_1.csv', index_col="date")
df.drop(["word_count"], axis=1, inplace=True)

def get_wc_ts(ticker) -> pd.Series:
    """
    Get wordcount timeseries for specified ticker.
    Source is the wallstreetbets subreddit.
    """

    target_words = [ticker]

    # Compute accumulated target word frequency as feature
    df['word_count'] = df['title'].map(
        lambda title: sum(title.count(word) for word in target_words)
    )

    return pd.Series(df['word_count'])