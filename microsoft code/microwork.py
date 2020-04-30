f = open("private.txt")
endpoint=f.readline().strip()
key= f.readline().strip()
f.close()

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis(client):
    c = open("comments.txt")
    data = c.readlines()
    for line in data:
        documents = [line]
        response = client.analyze_sentiment(documents = documents)[0]
        print("Document Sentiment: {}".format(response.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))

    f.close
          
sentiment_analysis(client)