import subprocess
import time
i = 0
bashWrite = open("theDark.sh","w")
theGoodStuff = open("comments.txt","r")
while i < 1560:
    bashWrite = open("theDark.sh","w")
    startwrite = "export GOOGLE_APPLICATION_CREDENTIALS=\"eminent-expanse-270800-41306623a2a7.json\"\n"
    startwrite +="curl -X POST \\\n"
    startwrite +="-H \"Authorization: Bearer \"$(gcloud auth application-default print-access-token) \\\n"
    startwrite +="-H \"Content-Type: application/json; charset=utf-8\" \\\n"
    startwrite += "--data \"{\n 'encodingType': 'UTF8',\n'document': {\n'type': 'PLAIN_TEXT',\n'content': '"
    toFormat = theGoodStuff.readline()
    toFormat = toFormat.replace('"',"")
    toFormat = toFormat.replace("'", "")
    toFormat = toFormat.strip("\n")
    startwrite += toFormat
    startwrite +="'\n}\n}\" \"https://language.googleapis.com/v1/documents:analyzeSentiment\" >> output.txt\n"
    bashWrite.write(startwrite)
    i+=1
    bashWrite.close()
    time.sleep(1)
    subprocess.Popen("./theDark.sh", shell=True, executable='/bin/bash')
    time.sleep(6)
    subprocess.Popen("./segrigate.sh", shell=True, executable='/bin/bash')
    time.sleep(1)

theGoodStuff.close()