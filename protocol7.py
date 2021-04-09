import  paillierself
import random
import  GM
import  dgk
n,public_key, private_key = paillierself.generate_paillier_keypair()
def protocol7(first_number,second_number,public_key, private_key):
    p, q, R = 232312311797, 971179711797, 17
    alice = GM.Alice(p, q, R)
    bob = GM.Bob(R, p * q)
    l=40
    a=first_number
    b=second_number
    aa = public_key.encrypt(a)
    bb = public_key.encrypt(b)
    xx = ((2 ** l) + bb - aa)
    x = private_key.decrypt(xx)
    r = random.randint(1, 2 ** (l+20))
    rr = public_key.encrypt(r)
    zz = (xx + rr)
    z = private_key.decrypt(zz)
    c = r % (2 ** l)
    d = z % (2 ** l)
    dgk_number = dgk.dgk(d,c,public_key, private_key)
    if dgk_number:
        t1 = "1"
    else:
        t1 = "0"
    t11 = bob.Ec(t1)  # t11 = [ t']
    r_int = int(r / (2 ** l))
    r_int = r_int % 2
    if r_int  :
        r1 = "1"
    else :
        r1 = "0"
    r11 = bob.Ec(r1)  # r11 = [rl]
    z_int = int(z / (2 ** l))
    z_int = z_int % 2
    if z_int :
        z1 = "1"
    else :
        z1 = "0"
    z11 = bob.Ec(z1)  # z11 = [zl]
    temp = GM.testTong( z11,r11,p * q)
    tt = GM.testTong(temp, t11,p * q)
    t = alice.Dc(tt)
    #print("x:" + str(x), "r:" + str(r), "z:" + str(z), "c:" + str(c),"d:" + str(d))
    #print("t1:" +str(t1),"r1:"+str(r1),"z1:"+str(z1),t)
    return  t

#print(protocol7(835,1480,public_key, private_key,))
