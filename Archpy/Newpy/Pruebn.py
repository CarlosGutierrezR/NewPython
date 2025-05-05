i=1
lista=[]
for i in range (1,11,2):
	print(i,*lista[::-1])
	lista.append(i)