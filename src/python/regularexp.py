import re

pattern = re.compile(r'\d+')
result = re.match(pattern, 'adbc12343eeeed555dd')
if result:
    print('match')
else:
    print('non-match')
result1 = re.search(pattern, 'adbc12343eeeed555dd')
print(result1.group())
print(re.split(pattern, 'adbc12343eeeed555dd'))
print(re.findall(pattern, 'adbc12343eeeed555dd'))