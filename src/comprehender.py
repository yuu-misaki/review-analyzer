import boto3
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

class Comprehender:
    def __init__(self):
        # Amazon Comprehendクライアントの作成
        self.AWS_REGION = os.environ['AWS_REGION']
        self.comprehend = boto3.client('comprehend', region_name=self.AWS_REGION)

    def analyze_sentiment(self, text):
        response = self.comprehend.detect_sentiment(Text=text, LanguageCode='ja')
        return response['Sentiment'], response['SentimentScore']

    def run(self, csv_file_path) -> pd.DataFrame:
        # CSVファイルの読み込み
        df = pd.read_csv(csv_file_path)
        
        # 各レビューの感情分析
        df['Sentiment'], df['SentimentScore'] = zip(*df['Content'].apply(self.analyze_sentiment))
        
        # csvファイルに保存
        df.to_csv(csv_file_path, index=False)

        return df
