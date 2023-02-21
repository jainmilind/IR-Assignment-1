from PyPDF2 import PdfReader
 
reader = PdfReader(r'D:\Downloads\Assignment-1\SamplePolicyDocs\Auto\insurance-pdf-NL-SPF-1.pdf')
 
# printing number of pages in pdf file
print(len(reader.pages))
 
# getting a specific page from the pdf file
page = reader.pages[2]
 
# extracting text from page
text = page.extract_text()
print(text)
