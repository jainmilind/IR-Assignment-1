import nltk
import textract
from nltk.corpus import *

path_name = r"Docs\Auto\1215E.2.docx"
text = textract.process(path_name)
text = text.decode("utf8")

# ! Uncomment in first run 
# nltk.download('punkt')
# nltk.download('words')
# nltk.download('stopwords')

tokens = nltk.tokenize.word_tokenize(str(text))
new_token = []

stop_words = set(stopwords.words('english'))

for i in tokens:
    if i.isalnum() and i.lower() not in stop_words:
        new_token.append(i.lower())
tokens = new_token

print(tokens)
