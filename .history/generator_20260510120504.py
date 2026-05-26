def fibbo(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p+q

x = fibbo(10)

x.__next__()

