import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321_schafer@my-work.net
'''


email_re = r'[a-zA-Z0-9_.-]+[^!#$%^&*()]@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
pattern = re.compile(email_re)

matches = pattern.finditer(emails)

# for match in matches:
#     print(match)




#
# Scraped Emails
#
import requests

with open('wiki.html') as f:
    corpus = f.read()
data = re.findall(email_re,corpus)

print(data)


