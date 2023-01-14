def gcd(n,m):
    # 求n,m的最大公因数
    if n < m:
        n,m=m,n
    while n%m!=0:
        n,m=m,n%m
    return m