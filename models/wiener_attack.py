from libnum import gcd,invmod
import random
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    if pow(x, 2) == n:
        return x
    else:
        return False

def con_fra(a, b):
    r = []
    while True:
        if a == 1:
            break
        tmp = a/b
        if tmp != 0:
            r.append(tmp)
        a, b = b, (a-tmp*b)
    return r

def divide_pq(ed, n):
    # ed = e*d
    k = ed - 1
    while True:
        g = random.randint(3, n-2)
        t = k
        while True:
            if t % 2 != 0:
                break
            t /= 2
            x = pow(g, t, n)
            if x > 1 and gcd(x-1, n) > 1:
                p = gcd(x-1, n)
                return (p, n/p)

def wiener_attack(glb):
    n = glb[0][0]
    e = glb[3][0]
    # print e
    cf = con_fra(e, n)
    for x in xrange(len(cf)):
        k, d = 0, 1
        while x >= 0:
            k, d = d, d*cf[x] + k
            x -= 1
        # print "k: %s\nd: %s\n" %(k, d)
        phi_n = (e*d - 1)/k
        B = n - phi_n + 1
        C = n
        dt = pow(B, 2) - 4*C    # b^2 - 4*a*c
        if dt >= 0 and isqrt(dt) and (B+isqrt(dt)) % 2 == 0:
            #return phi_n
            tmp_p,tmp_q=divide_pq(e*d,n)
            glb[1]  = tmp_q
            glb[2]  = tmp_p
    return glb

e = 57019382772166837488750427040015464490863175936396575556290232679668259683514801918298546850349718538222635977304361506235546587039055174992606638351023434322917005735910505716857963030159773221874370814472973319422853023944637626372539074831161749650232791256091117301145054914651557523038888181457290682237
n = 68253958478963934124300215757460723273691925280596309221863375905836387105252457670797482776100691909463871547306272253629697109054703333176926409544379734932863965587299902358818026560280727724874176607409038276642286734734838152097800253007709025880304435661500771500046972983240470823245360867996258239121
print wiener_attack([[n],-1,-1,[e]])