import sys
import pandas as pd
from nltk.stem.porter import *
from partb2 import preprocess_text

def main():
    porterStemmer = PorterStemmer()
    arg = sys.argv[1:]
    text_id = pd.read_csv('partb1.csv',encoding = 'ISO-8859-1')
    split_text = None
    for row in text_id.itertuples():
        # safety purpose
        if row[2] is None:
            break
        
        # open file and pre-processing text
        with open("cricket/" + row[2], "r") as f:
            text = f.read()
        text = preprocess_text(text)
        split_text = text.split()
        for i in range(len(split_text)):
            split_text[i] = porterStemmer.stem(split_text[i])
    
        text = ' '.join(split_text)
    
        # compare each keywords with text
        flag = 1
        for i in range(len(arg)):
            stemArg = porterStemmer.stem(arg[i])
            if re.findall(r'\b'+stemArg+r'\b', text) == []:
                flag = 0
                break
        if flag == 1:
            print(row[3])
            
if __name__ == '__main__':
    main()
