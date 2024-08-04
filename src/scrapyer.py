import requests
from bs4 import BeautifulSoup
import csv
import time

class Scraper:
    # スクレイピング関数
    def run(self,csv_save_path, target_url)->None:
        # CSVファイルのセットアップ
        csv_file = open(csv_save_path, mode='w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title','Content', 'Rating', 'Author', 'Date'])

        # レビューページのスクレイピング
        headers = {
        'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        response = requests.get(target_url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        reviews = soup.find_all('div', class_='we-customer-review')

        # レビューをCSVファイルに書き込み
        for review in reviews:
            title = review.find('h3', class_='we-customer-review__title').text.strip()
            content = review.find('blockquote', class_='we-customer-review__body').text.strip()
            rating_class = review.find('span', class_='we-star-rating-stars')['class']
            rating = int([s for s in rating_class if s.startswith('we-star-rating-stars-')][0].split('-')[-1])
            author = review.find('span', class_='we-customer-review__user').text.strip()
            date = review.find('time')['datetime']

            csv_writer.writerow([title, content, rating, author, date])

        print(f"Scraped {len(reviews)} reviews from {target_url}")