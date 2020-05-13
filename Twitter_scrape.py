!pip install twitter_scraper
import pandas as pd
from datetime import datetime

tweet_data = []
groupLists=['FactlyIndia','TimesFactCheck','QuintFactCheck']
dateTime = datetime.now()
fileName = 'data_twitter_'+str(dateTime)+'.csv'
for item in groupLists:
  for tweet in get_tweets(item):
    temp_dict=dict(tweet)
    tweet_data.append(temp_dict)
  # print(tweet)
tweet_df = pd.DataFrame(tweet_data)
tweet_df['scrapedDate'] = dateTime
tweet_df.head()
tweet_df.to_csv(fileName)
