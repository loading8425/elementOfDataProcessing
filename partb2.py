import re
import sys

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]","", text)
    text = re.sub(r"\t", "", text)
    text = text.replace('\n',' ')
    text = re.sub(r" +", " ", text)
    text = text.lower()
    return text

def main():
    arg = sys.argv[1]
    arg = arg[7:]

    #open file
    with open("cricket/" + arg, "r") as f:
        text = f.read()
    text = preprocess_text(text)
    print(text)

if __name__ == '__main__':
    main()