from libnum import *
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, isPrime, size
import random,gmpy
from Crypto.PublicKey import RSA
import argparse

def replace_red(string):
    return string.replace(string,'\033[1;31;40m'+string+'\033[0m')
def replace_green(string):
    return string.replace(string,'\033[1;32;40m'+string+'\033[0m')
#glb = [n,q,p,e]
def decrypt(glb,c,form):
	# print glb
	for i in range(len(glb[0])):
		print ("[+] n%i=%i"%(i,glb[0][0]))
	print ("[+] q=%i"%glb[1])
	print ("[+] p=%i"%glb[2])

	if len(glb)==5:
		if form=='int':
			print ("[+] m=%i"%convert(glb[4],form))
		else:
			print ("[+] m=%s"%convert(glb[4],form))		
		exit()
	d = get_d(glb)
	m = pow(c[0],d,glb[0][0])
	m = convert(m,form)	
	if form=='int':
		print ("[+] m=%i"%m)
	else:
		print ("[+] m=%s"%m)

def get_d(glb):
	try:
		q = glb[1]
		p = glb[2]
		e = glb[3][0]
		# print e
		d = invmod(e,(q-1)*(p-1))

		return d
	except Exception as string:
		print "[-] I got something wrong when get_d and now:"
        print "         p= {p}".format(p=p)
        print "         q= {q}".format(q=q)
        return 0

def convert(m,mode):
	if mode == 'int':
		return m
	elif mode == 'hex':
		return hex(m)
	elif mode == 'str':
		return n2s(m)

# print 1