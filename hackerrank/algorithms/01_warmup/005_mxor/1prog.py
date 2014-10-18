
def  maxXor( l,  r):
    return max([x^y for x in xrange(l,r+1) for y in xrange(x+1,r+1)])

_l = int(raw_input());

_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

