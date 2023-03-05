## IR-Assignment-1
CS F469 INFORMATION RETRIEVAL Assignment
 
Download following packages before running code
```
pip install nltk
pip install textract
pip install gensim
```
 
In python code do following for running for first time
```
nltk.download('punkt')
nltk.download('words')
nltk.download('stopwords')
```
 
#### For running code
1) First convert the pdf file to docx using some tool.
2) Then run [Preprocess.ipynb](Preprocess.ipynb) file which will create pickle objects for **Inverted Index, Documents and File names**
3) Then add your query in specific input file name you want your query to run in.(Example if you want to retrieve phrase queries add the input to phrase_input.txt)
4) Then run any type of code you want your query to run in. Note to run the code run all the cells of the notebook and you can see the output in the last cell of the respective notebook.
 
| Query Type | Code name |input file name|
|-----|--------|------|
| SINGLE WORD QUERY | [single_word_query.ipynb](Query\single_word_query.ipynb)| ?? |
| ?? | [boolean_retrival.ipynb](Query\boolean_retrival.ipynb)| ?? |
| PHRASE QUERY | [tfidf_phrase_query.ipynb](Query\tfidf_phrase_query.ipynb)| phrase_input.txt |
| ?? | [wildcard.ipynb](Query\wildcard.ipynb)| ?? |
| PHRASE QUERY | [query_with_nlp.ipynb.ipynb](Query\query_with_nlp.ipynb)| phrase_input.txt |
