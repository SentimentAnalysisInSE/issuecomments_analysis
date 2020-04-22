import csv

csvFilePath = '../Datasets/Jira.csv'

def getComments():
    data = '['
    i = 0
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            curr = row['comment']
            #print(len(curr.encode("utf8")))
            if len(curr.encode("utf8")) < 5000 and i < 24:
                data += '"' + curr + '",\n'
            else:
                data += '"' + curr + '"\n'
            i += 1
            if i >= 25:
                break
    data += ']'
    print(data)
    return data
