from base import *

def gcd(i,j):
    if i < j:
        i , j = j, i    
    r = i%j
    while r!=0:
        i = j
        j = r
        r = i%j
    return j

def ext_gcd(gld):
	n1 = gld[0][0]
	n2 = gld[0][1]
	e1 = gld[3][0]
	e2 = gld[3][1]
	q = gcd(n1,n2)
	p = n1/q
	gld[1] = q
	gld[2] = p
	return gld