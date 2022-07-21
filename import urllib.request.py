import urllib.request 
import json

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = urllib.request.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sums = 0
count_number = 0

for comment in json_obj["comments"]:
    sums += int(comment["count"])
    count_number += 1

print('Count:', count_number)
print('Sum:', sums)
