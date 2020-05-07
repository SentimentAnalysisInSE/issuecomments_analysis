import subprocess
import time

privateinfo = open("Private.txt","r")
APIkey = privateinfo.readline()
WatsonURL = privateinfo.readline()
theGoodStuff = open("theComments.txt","r")
i=0

while i < 500:
    bashWrite = open("theDark.sh","w")
    startwrite ="curl -X POST -u \"apikey:"+APIkey+"\" \\\n"
    startwrite += "--header \"Content-Type: application/json\" \\\n"
    startwrite += "--data \'{ \n"
    startwrite += "\t\"text\": \""
    toFormat = theGoodStuff.readline()
    toFormat = toFormat.replace('"',"" )
    toFormat = toFormat.replace("'", "")
    toFormat = toFormat.strip("\n")
    toFormat += "\" ,\n"
    startwrite += toFormat
    startwrite +="\t\"features\": { \n"
    startwrite += "\t\t\"sentiment\":{}\n"
    startwrite += "\t}\n }\' \\\n"
    startwrite += "\""+WatsonURL+"9847c3a5-f7cf-44ac-95bf-8af4aba38469/v1/analyze?version=2019-07-12\" >> output.txt"
    bashWrite.write(startwrite)
    bashWrite.close()
    i+=1
    subprocess.Popen("./theDark.sh", shell=True, executable='/bin/bash')
    time.sleep(2)

privateinfo.close()
theGoodStuff.close()
bashWrite.close()
