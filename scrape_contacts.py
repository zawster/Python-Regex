import re
import requests

re_phones = r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})'
re_emails = r'([\d\w\.]+@[\d\w\.\-]+\.\w+)'

data = requests.get('https://www.randomlists.com/email-addresses')#'https://www.thegolfclubatfossilcreek.com/club-contacts')

# phones = re.findall(re_phones,data.text)
emails = re.findall(re_emails,data.text)
# print(phones)
print(data.text)



