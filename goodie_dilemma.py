inp=open("sample_input.txt","r")
c=0
n=0
d={}
l=[]
l1=[]
l2=[]
for lines in inp:
	s=lines
	c=c+1
	if(c==1):
		s=s[::-1]
		z=s.find(' ')
		n=s[:z]
	elif(c==3):
		continue
	else:
		if(len(s)!=1):
			z=s.find(":")
			if(s[-1]=="\n"):
				d[s[:z].strip()]=int(s[z+1:-1].strip())
				l.append(int(s[z+1:-1].strip()))
			else:
				d[s[:z].strip()]=int(s[z+1:].strip())
				l.append(int(s[z+1:].strip()))
l.sort()
for i in range(0,len(l)-n):
	l1.append(l[i+n-1]-l[i])
m=min(l1)
x=m
m=l1.index(m)
m=len(l1)-m-n
inp.close()
out=open("sample_output.txt","w")
out.write("Here the goodies that are selected for distribution are : \n\n")
for i in range(0,n):
	l2.append(l[m-n+i])
k=list(d.keys())
v=list(d.values())
for i in l2:
	p=v.index(i)
	g=str(k[p])+": "+str(v[p])+"\n"
	out.write(g)
out.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+ str(x))