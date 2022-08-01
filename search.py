List = open("names.txt").readlines()

tempList = []

for name in List:
    if ((('o' in name) or ('O' in name)) & 
        (('r' in name) or ('R' in name)) & 
        (('k' in name) or ('K' in name)) &
        (('y' in name) or ('Y' in name)) &
            (' ' not in name) &
            ('(' not in name) &
            ('a' not in name) &
            ('A' not in name) &
            ('e' not in name) &
            ('E' not in name) &
            ('i' not in name) &
            ('I' not in name) &
            ('u' not in name) &
            ('U' not in name)):

        tempList.append(name)

with open(r'outPut.txt', 'w') as fp:
    for name in tempList:
        fp.write("%s" % name)