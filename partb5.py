import sys
import pandas as pd
import math as m
from partb2 import preprocess_text
from nltk.stem.porter import *


def get_cos(x, y):
    Sum = 0
    sumX = 0
    sumY = 0
    for i in range(len(x)):
        Sum = Sum + x[i] * y[i]
        sumX = sumX + x[i] * x[i]
        sumY = sumY + y[i] * y[i]
    sumX = m.sqrt(sumX)
    sumY = m.sqrt(sumY)
    return round((Sum/(sumX * sumY)),4)

def main():
    
    porterStemmer = PorterStemmer()
    arg = sys.argv[1:]
    
    # get matched document, store as dataframe
    text_id = pd.read_csv('partb1.csv', encoding='ISO-8859-1')
    split_text = None
    result = pd.DataFrame(columns=['filename','documentID', 'score'])
    for row in text_id.itertuples():
        # safety purpose
        if row[2] is None:
            break

        # open file and pre-processing text
        with open("cricket/" + row[2], "r") as f:
            text = f.read()
        
        #pre-process it
        text = preprocess_text(text)
        split_text = text.split()
        for i in range(len(split_text)):
            split_text[i] = porterStemmer.stem(split_text[i])
            text = ' '.join(split_text)

        # compare each keywords with text
        flag = 1
        for i in range(len(arg)):
            stemArg = porterStemmer.stem(arg[i])
            if not re.findall(r'\b' + stemArg + r'\b', text):
                flag = 0
                break
        if flag == 1:
            result = result.append([{'documentID':row[3], 'filename':row[2]}], ignore_index=True)

    # process on result text
    i = 0
    for row in result.itertuples():
        # read text from disk
        with open("cricket/" + row[1], "r") as f:
            text = f.read()

        #pre-process it
        wordDict = {}
        keyWordDict = {}
        text = preprocess_text(text)
        split_text = text.split()

        # count each word in split_text
        for word in split_text:
            stemWord = porterStemmer.stem(word)
            if stemWord in wordDict:
                wordDict[stemWord] = wordDict[stemWord] + 1
            else:
                keyWordDict[stemWord] = 0
                if stemWord in arg:
                    keyWordDict[stemWord] = 1
                wordDict[stemWord] = 1

        X = list(wordDict.values())
        Y = list(keyWordDict.values())
        result.loc[i,'score'] = get_cos(X, Y)
        i = i + 1

    # print result
    result = result.sort_values(by = 'score',ascending = False)
    print('documentID score')
    for row in result.itertuples():
        print(row[2], row[3])

    
if __name__ == '__main__':
    main()