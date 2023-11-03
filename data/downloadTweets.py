import warnings

import pandas as pd
import snscrape.modules.twitter as sntwitter

warnings.filterwarnings("ignore")

day = 31
queryBolsonaro = f'Bolsonaro lang:pt until:2022-11-01 since:2022-10-0{day}'
queryLula = f"Lula lang:pt until:2022-11-01 since:2022-10-{day}"
tweetsBolsonaro = []
tweetsLula = []
limit = 1000


print('Coletando tweets do Bolsonaro.')
for tweet in sntwitter.TwitterSearchScraper(queryBolsonaro).get_items():
    if len(tweetsBolsonaro) == limit:
        break
    else:
        tweetsBolsonaro.append(
            [tweet.date, tweet.user.username, tweet.content])
dfBolsonaro = pd.DataFrame(tweetsBolsonaro, columns=['Data', 'User', 'Texto'])
dfBolsonaro.to_csv(f'SNScraper_Data/Bolsonaro-{day}.csv')
print('Tweets de Bolsonaro salvos com sucesso.')

print('Coletando tweets do Lula.')
for tweet in sntwitter.TwitterSearchScraper(queryLula).get_items():
    if len(tweetsLula) == limit:
        break
    else:
        tweetsLula.append(
            [tweet.date, tweet.user.username, tweet.content])
dfLula = pd.DataFrame(tweetsLula, columns=['Data', 'User', 'Texto'])
dfLula.to_csv(f'SNScraper_Data/Lula-{day}.csv')
print('Tweets de Lula salvos com sucesso.')
