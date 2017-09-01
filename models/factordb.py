from  base  import *
import re
import requests
#glb = [n,q,p,e]
def factordb(glb):
    try:
        url = 'http://www.factordb.com/index.php?query=%i'
        s = requests.get(url%glb[0][0])
        res = re.findall('<font color="#000000">(.*?)</font>',s.content)
        # print res
        if res[0] != 0 and res[1] !=0:
            # print "yes"
            return [glb[0],int(res[0]),int(res[1]),glb[3]]
    except Exception as a:
        print replace_red("[-] have soming wrong when use online factordb tools")
        return glb

# s = factordb((322831561921859,-1,-1,23))
# base.decrypt(s,0xdc2eeeb2782c,'str')
