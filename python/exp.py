import re

pattern =r'\d+'

text='there are 123 apples '
match= re.search(pattern,text)
print(match.group())