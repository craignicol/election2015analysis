headlinesfilename = 'headlines.txt'

counts = {}
counts['_'] = 0

with open(headlinesfilename) as f:
    for line in f:
        content = line.strip()
        if len(content) > 0:
            counts['_'] += 1
            words = content.split()
            for word in words:
                if word not in counts:
                    counts[word] = 0
                counts[word] += 1
            
interestingcounts = {counts             
print counts