n, m, k, x, y, z, t, a = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input())
)

nm = n - (x - m) - t
mk = m - (y - k) - t
nk = k - (z - n) - t
two = nm + mk + nk

_n = n - nm - nk - t
_k = k - nk - mk - t
_m = m - nm - mk - t
one = _n + _k + _m

zero = a - one - two - t

print(one, two, zero, sep='\n')