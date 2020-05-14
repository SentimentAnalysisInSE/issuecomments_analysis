Google App web output site: eminent-expanse-270800.appspot.com
link to 1st refrence paper(dataset): https://dl.acm.org/doi/pdf/10.1145/2901739.2903505

Watson: Watson Natrual Language unsderstanding is used for the anylisis. Watson supports 13 different languages  : Arabic, Chinese (Simplified), Dutch, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Swedish. Watson uses the Sentiment keyword to extract a score and label for the setement. any score that is +- .2 of zero is assigned neautral with negitive scores being labeled negitive setement and positive scores gaining a positive lable for sentiment. This process is done automatically by the IBM servers with only the data being sent out required. To make a valid request you must provide the API key, URL and the Data to be anylized. For our anylisis we used the curl command with an automated script in python to make the call. this can be found on the github

Watson Scores: range from -1 to 1, scores determened to be within a threshold of zero are automatically set to zero by watson and labled neutral. 

Google: Google Natural Languae was used for the anylisis of the comments. Google supports many languages and forms by combining its translation API with the natural language API giving all languages that google translate allowes. It can further support audio and scanned documents but for our purposes we provided raw text through the curl command. as feedback google provides the comment anaylized the magnitude and score of the setiment. Google does not auto assign labels instead leaving that to the requestor of the anylisis.

Google scores have both magnitude and score magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) contributes to the text's magnitude (so longer text blocks may have greater magnitudes)scores range from -1 to 1 with -.25 to .25 considered mixed or neutral.

AWS: Amazon Comprehend was used for sentiment analysis of the comments. The 'detect sentiment' operation returns the most likely sentiment for the text object as well as the scores for each of the four sentiments. The overall sentiment will be either positive, negative, neutral, or mixed.

Amazon scores range from 0.0 to 1.0 and describe the level of confidence Amazon Comprehend has in the accuracy of its detection of sentiment. The most likely sentiment returned by the operation will have the highest score of the four sentiments. As seen in the example response, neutral is the determined sentiment even though the scores for neutral and positive are similar. The errror list documents which text items had errors. The error code, message, and index from the input list would be given for each error list object.



Example AWS Response:
{
  "ErrorList": [], 
  "ResultList": [
    {
      "Index": 0, 
      "Sentiment": "NEUTRAL", 
      "SentimentScore": {
        "Mixed": 0.010275892913341522, 
        "Negative": 0.16961470246315002, 
        "Neutral": 0.4149356484413147, 
        "Positive": 0.40517377853393555}
      },
}

