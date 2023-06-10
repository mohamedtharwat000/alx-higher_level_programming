#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    b = []
    c = []
    for i in range(2):
        a.append(tuple_a[i]) if i < len(tuple_a) else a.append(0)
        b.append(tuple_b[i]) if i < len(tuple_b) else b.append(0)
        c.append(a[i] + b[i])
    return tuple(c)
