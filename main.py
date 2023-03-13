from nltk.tokenize import word_tokenize
import tokenize
import csv
import os

numOpinions = 0
print ("started")
# tests all files in a directory.
for filename in os.listdir("courtOpinions"):
    f = open("courtOpinions/"+filename, "r")
    opinion = f.read()
    numOpinions = numOpinions + 1
    f.close()

    words = word_tokenize(opinion) # this just separates out each word.

    negWords = []  # an empty list to dump the negLexicon into
    posWords = []  # an empty list to dump the posLexicon into


    # put the files into lists
    with open('wordBanks/posLexicon.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')   
        for word in readCSV:
            posWords.append(word[0])

    with open('wordBanks/negLexicon.csv') as csvfile:
        readCSV2 = csv.reader(csvfile, delimiter=',')   
        for word in readCSV2:
            negWords.append(word[0])

    # initalize the counters
    posCounter = 0
    negCounter = 0


    # check which list each word in the opinion is in and then increment the counters
    for word in words:
        for posWord in posWords:
            if word==posWord:
                posCounter = posCounter+1
        for negWord in negWords:
            if word==negWord:
                negCounter = negCounter+1

    # compare the counters            
    if posCounter>negCounter:
        feeling = "positive"
    elif posCounter<negCounter:
        feeling = "negative"
    else:
        feeling = "inconclusive"

    # print eveything
    print ("% positive", "{:.2f}".format(posCounter/len(words)*100), "%")
    print ("% negative", "{:.2f}".format(negCounter/len(words)*100), "%")
  
    print ( filename, "is generally" , feeling)

print (numOpinions, "opinions were tested.")



 
