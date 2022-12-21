def rec(i):
    print("Hello")
    i-=1
    if i > 0:
        rec(i)

rec(5)