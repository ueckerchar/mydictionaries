infile = open('someone.txt','r')
words = {}
i = 0

txt = infile.read()
txt = txt.rstrip('\n'+','+',')

list = txt.split(' ')

print(list)

for record in list:
    if record in list and record not in words:
        x = list.count(record)
        words[record] = {'count': x}

print(words)