

curl -X POST -u "apikey:$1" \
--header "Content-Type: application/json" \
#need to pass line from csv to text
#pass data from java call
--data $2 \
"$3/v1/analyze?version=2019-07-12"\
>> output.txt
#need to securely add api and url to the script