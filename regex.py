import re

# with open('FYP-logs.log') as file:
#     logs = [ line[:-2] for line in file.readlines()[:20]]
# pattern = r'[0-9\@\#\$\%\*\(\)\-\'\:\/\.\[\]]'
# # pattern = r'[a-zA-Z]'
# for log in logs:
#     matches = re.sub(pattern,'',log).replace(' ','')
# # matches = re.search(pattern,lines[0])
#     print(matches)

text = '''Udana is 19 years old, and Murlie is 25 years old. Elsse is 57, 
        and her grandfather, Obama is 100, though their childs Nathan is 12 
        and Edwards is 15 years old.
'''
ages = re.findall(r'\d{1,3}',text)
names = re.findall(r'[A-Z]\w*',text)
info = {}
for i,j in zip(ages,names):
    info[i] = j

print(info)