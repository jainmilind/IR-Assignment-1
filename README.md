# IR-Assignment-1
CS F469 INFORMATION RETRIEVAL Assignment


# ADD ALL PIP install you do in requirements.txt

### One word query (creation of inverted index)
1) Create a list of dummy docs of particular number of words(100) and original doc name.
2) iterate over original doc.
3) for each word corresponding in dummy doc.
    a) if its not a stop word convert it to its stemming root
    b) then add document id and doc name in dict for that particular root word.
