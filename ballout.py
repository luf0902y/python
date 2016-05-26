import random
filename = 'namelist.txt'
filehandle = open(filename)
st=[]
t = random.randrange(0,19)
for line in filehandle:
	line = line.split()
	st.append(line[2])
print (st[t])
