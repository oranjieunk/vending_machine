def test_plus():
    assert 3 == 1 + 2

def fibo(n):
    if n < 3:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)
    return
