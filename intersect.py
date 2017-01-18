seq1 = [1,2,3,4,5,6,7,8,9]
seq2 = [2,4,6,8,0]

'''
res = []

def intersect(seq1,seq2):
	
	for x in seq1:
		if x not in seq2:
			res.append(x)
	print(res)
intersect(seq1,seq2)
'''
L = [x for x in seq2 if x in seq1]
print(L)