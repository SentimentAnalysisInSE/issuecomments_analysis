# referenced http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
import sys, os, base64, datetime, hashlib, hmac
import requests
import json

def getSentiment(data):
    method = 'POST'
    service = 'comprehend'
    host = 'comprehend.us-east-2.amazonaws.com'
    region = 'us-east-2'
    endpoint = 'https://comprehend.us-east-2.amazonaws.com/'

    content_type = 'application/x-amz-json-1.1'

    amz_target = 'Comprehend_20171127.BatchDetectSentiment'

    request_parameters = data

    def sign(key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


    def getSignatureKey(key, date_stamp, regionName, serviceName):
        kDate = sign(('AWS4' + key).encode('utf-8'), date_stamp)
        kRegion = sign(kDate, regionName)
        kService = sign(kRegion, serviceName)
        kSigning = sign(kService, 'aws4_request')
        return kSigning


    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    if access_key is None or secret_key is None:
        print('No access key is available.')
        sys.exit()

    # Create a date for headers and the credential string
    t = datetime.datetime.utcnow()
    amz_date = t.strftime('%Y%m%dT%H%M%SZ')
    date_stamp = t.strftime('%Y%m%d')

    canonical_uri = '/'

    canonical_querystring = ''

    canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amz_date + '\n' + 'x-amz-target:' + amz_target + '\n'

    signed_headers = 'content-type;host;x-amz-date;x-amz-target'

    payload_hash = hashlib.sha256(request_parameters.encode('utf-8')).hexdigest()

    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'
    string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + '\n' + hashlib.sha256(
        canonical_request.encode('utf-8')).hexdigest()

    signing_key = getSignatureKey(secret_key, date_stamp, region, service)

    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    headers = {'Content-Type': content_type,
               'X-Amz-Date': amz_date,
               'X-Amz-Target': amz_target,
               'Authorization': authorization_header}

    r = requests.post(endpoint, data=request_parameters.encode('utf-8'), headers=headers)

    print('Response code: %d\n' % r.status_code)

    return json.loads(r.text)





