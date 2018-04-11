fname = raw_input("Enter File Name: ")
try:
    fhand = open(fname)
except:
    print 'File does not exist!'
    exit()
    
for line in fhand:
        print line.rstrip().upper()
        
