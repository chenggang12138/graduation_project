import protocol3 as p3
import protocol1 as p1
import paillierself
def protocol4(x,w,public_key, private_key):
    n, public_key, private_key = paillierself.generate_paillier_keypair()
    v=[]
    #x =  [1,2,3]
    #w = [[10,20,30],[14,25,26],[17,16,29]]
    k = len(w)
    i = 0
    while i<k:
        temp =  p3.protocol3(x,w[i],public_key, private_key)
        i = i+1
        #print(private_key.decrypt(temp))
        v.append(temp)

    return  p1.protocol1(v,14,public_key, private_key)

