export GOOGLE_APPLICATION_CREDENTIALS="eminent-expanse-270800-41306623a2a7.json"
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
--data "{
 'encodingType': 'UTF8',
'document': {
'type': 'PLAIN_TEXT',
'content': 'Reviews appreciated.'
}
}" "https://language.googleapis.com/v1/documents:analyzeSentiment" >> output.txt
