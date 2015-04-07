headlinesfilename = 'headlines.txt'

counts = {}
counts['_'] = 0

with open(headlinesfilename) as f:
    for line in f:
        content = line.strip()
        if len(content) > 0:
            counts['_'] += 1
            words = content.split()
            for casedword in words:
                word = casedword.lower()
                if word not in counts:
                    counts[word] = 0
                counts[word] += 1
            
interestingcounts = {k: v for k, v in counts.iteritems() if v > 1}          
print sorted(interestingcounts.items(), key=lambda x: x[1], reverse=True)