f = open("out01.txt","r")  # open file, read-only
s = open("Sorteroutput.txt", "w") # open file, write
lines = f.readlines()
lines.sort()

for line in lines:
 s.write(line)

f.close()
s.close()