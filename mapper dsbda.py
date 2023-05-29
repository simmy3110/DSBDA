# import sys
# for line in sys.stdin:
#     for word in line.strip().split():
#         print(f'{word}\t{1}') 
#         # print ('%s\t%s' % (word, 1))

import sys
for line in sys.stdin:
    line=line.strip()
    words=line.split()

    for word in words:
        print ('%s\t%s' % (word,1))