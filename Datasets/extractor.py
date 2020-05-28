
filer = open("github_gold.txt",encoding="utf-8")
filew = open("githubComments.txt","w",encoding="utf-8")
lines = filer.readlines()
for line in lines:
    line = line.replace(";",",")
    filew.write(line)
