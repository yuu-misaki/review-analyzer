import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class ScorePlotter:
    
    def run(self,df:pd.DataFrame)->None:
        # 感情と評価の比較
        sentiment_rating = df[['Rating', 'Sentiment']]
        sns.countplot(x='Rating',hue='Sentiment',data=sentiment_rating)
        plt.title('Rating vs Sentiment')
        plt.show()

        # 感情スコアのプロット
        sentiment_score = pd.json_normalize(df['SentimentScore'])
        sentiment_score['Rating'] =df['Rating']

        # プロット
        plt.figure(figsize=(10,6))

        for sentiment in ['Positive','Negative', 'Neutral', 'Mixed']:

            sns.scatterplot(x='Rating',
            y=sentiment,
            data=sentiment_score,
            label=sentiment)

            plt.title('Sentiment Scores vs Rating')
            plt.xlabel('Rating')
            plt.ylabel('Sentiment Score')
            plt.legend()
            plt.show()
