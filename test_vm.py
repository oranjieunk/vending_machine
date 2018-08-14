# def test_5th_should_be_5():
#     assert 5 == fibo(33)

from vm import VendingMachine


def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_accumulation_of_change():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_unknown_command():
    m = VendingMachine()
    assert "알 수 없는 명령입니다" == m.run("웅앵")
