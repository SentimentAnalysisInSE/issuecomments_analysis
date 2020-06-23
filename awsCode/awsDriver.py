import csv
import pandas as pd
import numpy as np
from postScript import *


csvPathRead = '../Datasets/stack_overflow.csv'
sentiment = []
sentimentScores = []
data = {}
data['LanguageCode'] = 'en'
data['TextList'] = []
comment = ''
i = 0

def getNextSentiment(obj):
    scores = list(obj.get('SentimentScore').values())
    sentiments = list(obj.get('SentimentScore').keys())
    sortedIndices = np.argsort(scores)
    sentimentScores.append(scores[sortedIndices[len(sortedIndices)-2]])
    sentiment.append(sentiments[sortedIndices[len(sortedIndices)-2]])

def parseSentiment(obj, currValue):
    sentiment.append(currValue)
    changeCase = currValue.lower()
    currValue = currValue[0] + changeCase[1:]
    scores = obj.get('SentimentScore')
    sentimentScores.append(scores.get(currValue))

with open(csvPathRead, 'r', encoding="ISO-8859-1") as csvRead:
    csvReader = csv.DictReader(csvRead)
    df = pd.read_csv(csvPathRead, encoding="ISO-8859-1", dtype='str')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df[['id','comment','label']]
    for row in csvReader:
        curr = row['comment']
        if len(curr.encode('utf8')) > 4700:             #text has 5000 byte limit
            data['TextList'].append(curr[:4700])
        elif len(curr) >= 1:
            data['TextList'].append(str(curr))
        else:
            data['TextList'].append(str(curr) + ' ')
        i += 1
        if i >= 25:          #request body takes a maximum of 25 text comments
            requestBody = json.dumps(data)
            sentimentVals = getSentiment(requestBody)

            for obj in sentimentVals['ResultList']:
                currValue = obj.get('Sentiment')
                parseSentiment(obj, currValue)
            i = 0
            data['TextList'] = []
    requestBody = json.dumps(data)
    sentimentVals = getSentiment(requestBody)

    for obj in sentimentVals['ResultList']:
        currValue = obj.get('Sentiment')
        parseSentiment(obj, currValue)

    df['AWS Labels'] = pd.Series(sentiment, dtype='str')
    df['AWS Scores'] = pd.Series(sentimentScores, dtype='float64')
    df.to_csv('stackAWS.csv')