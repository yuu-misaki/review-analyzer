
from src.scrapyer import Scraper
from src.comprehender import Comprehender
from src.score_plotter import ScorePlotter


def run(csv_save_path:str,url:str)->None:
    """apple storeのレビュー分析を行い、感情分析の結果とレビューの相関をプロットする

    Args:
        csv_file (_type_): _description_
        url (_type_): _description_
    """
    
    # scrapyingして、csvファイルを作成
    scraper = Scraper()
    scraper.run(csv_save_path=csv_save_path,target_url=url)

    # 感情分析
    comprehender = Comprehender()
    df = comprehender.run(csv_file_path=csv_save_path)

    # レビューと感情分析の結果をプロット
    score_plotter = ScorePlotter()
    score_plotter.run(df)


