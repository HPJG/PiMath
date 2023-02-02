def gcd(n,m):
    # 求n,m的最大公因数
    if n < m:
        n,m=m,n
    while n%m!=0:
        n,m=m,n%m
    return m

def lcm(n,m):
    # 求n,m的最小公倍数
    return n*m//gcd(n,m)