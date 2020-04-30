import csv
import pandas as pd
from postScript import *


csvPathRead = '../Datasets/Jira.csv'
sentiment = []
sentimentScores = []
data = {}
data['LanguageCode'] = 'en'
data['TextList'] = []
removedComments = []
comment = ''
i = 0
with open(csvPathRead, 'r', encoding="ISO-8859-1") as csvRead:
    csvReader = csv.DictReader(csvRead)
    df = pd.read_csv(csvPathRead, encoding="ISO-8859-1")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    for row in csvReader:
        curr = row['comment']
        if len(curr.encode('utf8')) > 5000:             #text has 5000 byte limit
            data['TextList'].append(curr[:5000])
        elif len(curr) >= 1:
            data['TextList'].append(str(curr))
        else:
            data['TextList'].append(str(curr) + ' ')    #blank comments cause errors
        i += 1
        if i >= 25:          #request body takes a maximum of 25 text comments
            requestBody = json.dumps(data)
            sentimentVals = getSentiment(requestBody)

            for obj in sentimentVals['ResultList']:
                currValue = obj.get('Sentiment')
                sentiment.append(currValue)
                changeCase = currValue.lower()
                currValue = currValue[0] + changeCase[1:]
                scores = obj.get('SentimentScore')
                sentimentScores.append(scores.get(currValue))
            i = 0
            data['TextList'] = []
    requestBody = json.dumps(data)
    sentimentVals = getSentiment(requestBody)

    for obj in sentimentVals['ResultList']:
        currValue = obj.get('Sentiment')
        sentiment.append(currValue)
        changeCase = currValue.lower()
        currValue = currValue[0] + changeCase[1:]
        scores = obj.get('SentimentScore')
        sentimentScores.append(scores.get(currValue))

    df['AWS Labels'] = pd.Series(sentiment, dtype='str')
    df['AWS Scores'] = pd.Series(sentimentScores, dtype='float64')
    df.to_csv('rest30.csv')





