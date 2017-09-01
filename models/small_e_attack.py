from base import *
#glb = [n,q,p,e]
def small_e_attack(glb,c):
	c = c[0]
	n = glb[0][0]
	e = glb[3][0]
	i = 0
	while 1:
		res = gmpy.root(c+i*n,e)
		if(res[1] == True):
		    # print res
		    break
		# print "i="+str(i)
		i = i+1
	glb.append(int(res[0]))

	return glb