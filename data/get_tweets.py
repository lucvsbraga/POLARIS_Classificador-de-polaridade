import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tweepy

warnings.filterwarnings("ignore")


day = 21

bearer_token = "AAAAAAAAAAAAAAAAAAAAALZ6ZwEAAAAAlkfIIUkUSNtYrgRJ9%2B%2FXjx3BRUY%3DkhUBUIAqncgVgzTUXlsMTCHWG3n9ipn2XFf2C5lv8umdZtbW8Y"
client = tweepy.Client(bearer_token)

response_bolsonaro = client.search_recent_tweets("Bolsonaro -is:retweet", tweet_fields=['created_at'], user_fields=['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'], expansions=[
                                                 'attachments.poll_ids', 'attachments.media_keys', 'author_id', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id'], start_time=f'2022-10-{day}T00:00:00Z', end_time=f'2022-10-{day}T23:59:00Z', max_results=100)
response_lula = client.search_recent_tweets("Lula -is:retweet", tweet_fields=['created_at'], user_fields=['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'], expansions=[
                                            'attachments.poll_ids', 'attachments.media_keys', 'author_id', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id'], start_time=f'2022-10-{day}T00:00:00Z', end_time=f'2022-10-{day}T23:59:00Z', max_results=100)


dfBolsonaro = pd.DataFrame(response_bolsonaro.data)
dfLula= pd.DataFrame(response_lula.data)


dfBolsonaro['created_at'] = pd.to_datetime(
    dfBolsonaro.created_at).dt.tz_localize(None)
dfLula['created_at'] = pd.to_datetime(
    dfLula.created_at).dt.tz_localize(None)


# dfBolsonaro.to_excel(f'DATA/Bolsonaro_{day}-10.xlsx',
#                      index=False, encoding='unicode-escape')
# print('Tweets de Bolsonaro importados com sucesso.')

# dfLula.to_excel(f'DATA/Lula_{day}-10.xlsx',
#                      index=False, encoding='unicode-escape')
dfLula.to_excel(f'DATA/TESTE{day}-10.xlsx',
                     index=False, encoding='unicode-escape')

print('Tweets de Lula importados com sucesso.')
