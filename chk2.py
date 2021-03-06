N = 100
def isprime(n) :
    # The simplest primality test.
    # Enumerate $i$ from $2$ to $\sqrt{n}$ and see if $n$ has a divisor.
    if n == 1 : return 0
    for i in range(2, n) :
        if i * i > n : return 1
        if n % i == 0 : return 0

def f1(m, n) :
    # According to the definition above
    return not (isprime(n) and isprime(m))

def f2(m, n) :
    if m + n <= 6 : return 0
    # Goldbach's conjecture holds in small cases.
    # So if $m+n$ is even, $f_2(n,m)$ is false.
    # If $m+n$ is odd, we only need to check if $m+n-2$ is a prime not more than 99.
    if (m + n) % 2 == 0 : return 0
    if m + n - 2 > N : return 0
    if isprime(m + n - 2) : return 0
    return 1

def f3(m, n) :
    P = m * n
    if not f2(m, n) : return 0
    for p in range(2, P) :
        if P % p == 0 :
            q = P / p
            if p < q and q < N :
                # Check the condition
                # $\forall 2\le p<q\le 99, pq=mn,p\ne m\implies f_2(p,q)=\False$
                if p != m :
                    if f2(p, q) : return 0
    return 1

def f4(m, n) :
    S = m + n
    if not f3(m, n) : return 0
    for p in range(2, S) :
        q = S - p
        if p < q and q < N :
            # Check the condition
            # $\forall 2\le p<q\le 99, p+q=m+n, p\ne m\implies f_3(p,q)=\False$
            if p != m :
                if f3(p, q) : return 0
    return 1

for m in range(2, N) :
    for n in range(m + 1, N) :
        # $2\le m<n\le 99$, check which $f_4(m,n)$ is true.
        if f4(m, n) :
            print m, n
