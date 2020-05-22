def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tr = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2,])

print("""\
Shows when values are hashable, which only happens
when an object can never change.
""")

print(fixed(tr))

print(fixed(tm))

