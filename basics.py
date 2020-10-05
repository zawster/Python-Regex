import re

text = '''
abcdefghijklmnopqurtuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 hehehe
MetaCharacters: . ^ $ * + ? { } [ ] \ | ( )
dessired.com http://nyatel.com.pk https://google.com
321-555-4321 123.555.1234 123*555*1234 800-555-1234 900-555-1234
Mr. Normal Mr Basic Ms davis Mrs. Complex Mr A cat bat sat mat
'''

# pattern = re.compile(r'[^m]at')
# pattern = re.compile(r'\d\d\d[\.\-]\d[\.\-]\d{4}') # Contacts
pattern = re.compile(r'Mrs?\.?\s[A-Z]\w*')   # Mr and Mrs
# matches = pattern.search(text)
matches = pattern.findall(text)

# matches = re.sub()


print(matches)