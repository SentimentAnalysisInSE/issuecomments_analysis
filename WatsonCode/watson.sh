curl -X POST -u "apikey:$1" \
--header "Content-Type: application/json" \
$2 \
"$3/v1/analyze?version=2019-07-12" >>output.txt