def readfile():
    f = open("tobeanylized.csv")
    raw_data = f.readlines()
    f.close()
    a = open("completedComments.csv",'w')
    positive=0
    negitive=0
    neutral= 0
    for line in raw_data:
        scores = line.split(",")
        if(float(scores[0].strip())<-.25 and float(scores[1].strip()) >.2):
            a.write("negative\n")
            negitive+=1
        elif(float(scores[0].strip())>.25 and float(scores[1].strip()) > .2):
            a.write("positive\n")
            positive+=1
        else:
            a.write("neutral\n")
            neutral+=1
    a.write("positive "+str(positive))
    a.write("negative "+str(negitive))
    a.write("neutral "+str(neutral))
    print("HMMMM")

def main():
    readfile()


if __name__ == '__main__':
    main()
    
