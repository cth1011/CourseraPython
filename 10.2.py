
'''
10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the hour
 out from the 'From ' line by finding the time and then splitting the string a 
 second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below
'''

xfile = open("mbox-short.txt", 'r')
x=list()
lst = list()
dct = dict()
for line in xfile:
    if not line.startswith('From'): continue
    else:    
        x = line.rstrip()
        x = line.split()
        try:
            y = x[5].split(':')
            lst.append(y[0])

        except:
            continue
for number in lst:
    dct[number] = dct.get(number, 0)+1
#print dct
        #x = line.split(':')
        

for key, val in sorted(dct.items()):
    print key, val