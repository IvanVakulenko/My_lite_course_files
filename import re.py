import re
name = input("Enter file:")
alltext = open(name)
result = 0
for line in alltext :
    line = line.strip()
    x = re.findall('[0-9]+', line)
    for z in x :
        result = result + int(z)
print(result)