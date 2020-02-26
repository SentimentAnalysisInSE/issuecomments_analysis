curl -X POST -u "apikey:eZBFNDSkHsQM2RtxjOPJdVsj7AgAKx7SBUuO_CITqOyS" \
--header "Content-Type: application/json" \
--data '{
  "text": "Bug Flavio more? Seriously; discuss with Flavio and come up with a patch & test that is deterministic. Another option would be to refactor to allow the code in question to be tested as a true unit test; rather than as a system test (we need to work on that in general in ZK). Mockito?",
  "features": {
    "sentiment": {}
  }
}' \
"https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/9847c3a5-f7cf-44ac-95bf-8af4aba38469/v1/analyze?version=2019-07-12" >> output.txt