fhand = raw_input('Enter File Name: ')
xfile = open(fhand)
count = 0.0000
Sum = 0.0000
for line in xfile:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        a = line.find(':')
        number = float(line[a + 1:])
        Sum += number
        Sum = float(Sum)
print Sum/count
        
    
