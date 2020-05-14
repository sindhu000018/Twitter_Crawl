!pip install twitter_scraper
import pandas as pd
from datetime import datetime, timedelta

tweet_data = []
duration = datetime.today() - timedelta(days=7)
groupLists=['FactlyIndia','TimesFactCheck','QuintFactCheck']
dateTime = datetime.now()
fileName = 'data_twitter_'+str(dateTime)+'.csv'
for item in groupLists:
  for tweet in get_tweets(item, pages=20):
    post_date = (tweet['time'])
    if post_date > duration: 
      temp_dict=dict(tweet)
      tweet_data.append(temp_dict)
tweet_df = pd.DataFrame(tweet_data)
tweet_df['scrapedDate'] = dateTime
tweet_df.head()
tweet_df.to_csv(fileName)
