!pip install twitter_scraper
import pandas as pd
tweet_data = []
import pandas as pd
from twitter_scraper import get_tweets
for tweet in get_tweets('FactlyIndia'):
  temp_dict=dict(tweet)
  tweet_data.append(temp_dict)
  # print(tweet)
tweet_df = pd.DataFrame(tweet_data)
tweet_df.head()
tweet_df.to_csv('FactlyIndia.csv')
