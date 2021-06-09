import pandas as pd
import os
import re
import sys

def main():
    # find directory on disk
    directory = os.listdir(os.getcwd()+'/cricket')

    # set match patterns
    pattern_1 = r'[A-Z]{4}-\d{3}[A-Z]\W'
    pattern_2 = r'[A-Z]{4}-\d{3}'

    # set dataframe
    data = pd.DataFrame(columns=['filename', 'documentID'])

    # start to match patterns
    for i in range(len(directory)):
        if(directory[i][0]=='.'):
            continue
        with open("cricket/"+directory[i], "r") as f:
            text = f.read()
        if re.findall(pattern_1, text):
            ans = re.findall(pattern_1, text)[0][0:9]
        elif re.findall(pattern_2, text):
            ans = re.findall(pattern_2, text)[0]
        else:
            print("Not found")
        data = data.append([{'filename':directory[i], 'documentID':ans}], ignore_index=True)

    arg = sys.argv[1]
    data = data.sort_values(by='filename')
    data.reset_index(inplace=True,drop=True)
    data.to_csv(arg)

if __name__ == '__main__':
    main()