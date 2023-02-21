import nltk
import textract

path_name = r"D:\3-2\IR\Assignment\Assignment-1\SamplePolicyDocs\Auto\1215E.2.pdf"
text = textract.process(path_name)
text = text.decode("utf8")

nltk.download('punkt')
nltk.download('words')

tokens = nltk.tokenize.word_tokenize(str(text))
new_token = []

for i in tokens:
    if i.isalnum():
        new_token.append(i.lower())
tokens = new_token

print(set(tokens))
