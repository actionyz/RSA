def hastads_extend(gld,c):
	# c1,c2,c3,n1,n2,n3,
	c1 = c[0]
	c2 = c[1]
	c3 = c[2]
	n1 = gld[0][0]
	n2 = gld[0][1]
	n3 = gld[0][2]
	e = gld[3][0]
    M=n1*n2*n3
    M1=n2*n3
    M2=n1*n3
    M3=n1*n2
    t1=invmod(M1,n1)
    t2=invmod(M2,n2)
    t3=invmod(M3,n3)
    t=(c1*t1*M1+c2*t2*M2+c3*t3*M3)%M ##t=m^e
    return (t,M)