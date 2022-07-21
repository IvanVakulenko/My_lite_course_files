name = input("Enter file:")
handle = open(name)
hourlist = []
hourcount = dict()
for line in handle :
    word = line.split() 
    if len(word) > 2 and word[0] == 'From': 
        hour = word[5].split(':') 
        hourcount[hour[0]] = hourcount.get(hour[0],0) + 1
    else : continue 
        
for k,v in hourcount.items():
    hourlist.append((k,v))
    hourlist.sort()
for k,v in hourlist :
    print(k,v)
    
    
    