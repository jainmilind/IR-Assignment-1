import nltk
import textract
from nltk.corpus import *
from nltk.stem.porter import *
import os
from Constants import *

# ! Uncomment in first run 
# nltk.download('punkt')
# nltk.download('words')
# nltk.download('stopwords')

# stemming porter object
stemmer = PorterStemmer()

cwd = os.getcwd() + r"\Docs"

# list of all doc names
files = list()
for dir in [r"\Auto", r"\Property"]:
    cur_dir = cwd + dir
    for file in os.listdir(cur_dir):
        cur_path = cur_dir + "\\" + file
        files.append(cur_path)
files.sort()

# set of Stop words
stop_words = set(stopwords.words('english'))

"""
{
   key : string (normalized)
   value: list of ("doc index", file_index, frequency) 
}
"""
inverted_idx = dict()

# list of string modified document of DOC_LEN
documents = list()

count_id = 0

def process(file_index):
    """
    Reads file, tokenize it, normalizes it and builds the inverted index
    """
    global count_id
    text = textract.process(files[file_index]).decode("utf8")

    tokens = nltk.tokenize.word_tokenize(str(text))
    
    new_token = list()
    for i in tokens:
        if i.isalnum():
            new_token.append(i.lower())
    tokens = new_token
    
    for i in range(0, len(tokens), DOC_LEN):
        documents.append("")
        
        normalised_word_freq = dict()

        for j in range(i, min(len(tokens), i + DOC_LEN)):
            documents[-1] += tokens[j] + " "

            normal = stemmer.stem(tokens[j].lower())
            if normalised_word_freq.get(normal) != None:
                normalised_word_freq[normal] += 1
            else:
                normalised_word_freq[normal] = 1 
        
        visited = set()

        for j in range(i, min(len(tokens), i + DOC_LEN)):
            normalised_word = stemmer.stem(tokens[j].lower())
            if tokens[j].lower() not in stop_words and normalised_word not in visited:
                visited.add(normalised_word)

                if inverted_idx.get(normalised_word) != None:
                    inverted_idx[normalised_word].append((count_id, file_index, normalised_word_freq[normalised_word]))
                else:
                    inverted_idx[normalised_word] = [(count_id, file_index, normalised_word_freq[normalised_word])]
        count_id += 1

for i in range(len(files)):
    process(i)


for x in inverted_idx:
    inverted_idx[x] = sorted(inverted_idx[x], key=lambda y: -y[2])


def query(query_str):
    """
    Normalize query string and search in inverted index and retervive doc
    """

    query_str = stemmer.stem(query_str.lower())
    if inverted_idx.get(query_str) == None:
        return "Not found kill yourself"
    else:
        ans = []
        for i in range(min(len(inverted_idx[query_str]), 3)):
            ans.append((documents[inverted_idx[query_str][i][0]], files[inverted_idx[query_str][i][1]]))
        return ans

for i in ["ontario", "Milind", "illegal", "Canadian", "dollar", "TerrIbLe", "PoliCy", "Tyre", "Mobile", "Motor", "LMAO", "Induction", "Proof"]:
    print(i, query(i))
