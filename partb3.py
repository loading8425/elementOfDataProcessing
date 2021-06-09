import sys
import pandas as pd
import re
from partb2 import preprocess_text

def main():
    arg = sys.argv[1:]
    text_id = pd.read_csv('partb1.csv',encoding = 'ISO-8859-1')
    for row in text_id.itertuples():
        # safety purpose
        if row[2] is None:
            break
    
        # open file and pre-process text
        with open("cricket/" + row[2], "r") as f:
            text = f.read()
        text = preprocess_text(text)
        flag = 1
    
        # compare text with keywords
        for i in range(len(arg)):
            if not re.findall(r'\b' + arg[i].lower() + r'\b', text):
                flag = 0
                break
        if flag == 1:
            print(row[3])

if __name__ == '__main__':
    main()