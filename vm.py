class VendingMachine:
    def __init__(self):
        self._change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]   # ex)["동전","100","잔액"]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"
        elif cmd == "동전":
            known_coins = "10,50,100,500".split(",")
            coin = params[0]
            if coin not in known_coins:
                return "알 수 없는 동전입니다."

            self._change += int(coin)
            return coin + "원을 넣었습니다"

        elif cmd == "음료":
            prices = {'커피': 150, '우유': 200, '밀크커피': 300}
            beverage = params[0]
            known_beverages = list(prices.keys())
            if beverage not in known_beverages:
                return "알 수 없는 음료입니다."
            if self._change < prices[beverage]:
                return "잔액이 부족합니다."

            self._change = self._change - prices[beverage]
            return beverage + "가 나왔습니다."

        elif cmd == "반환":
            coins = [500,100,50,10]
            changes = ""
            i = 0
            if self._change == 0:
                changes = "잔액이 없습니다.."
            while self._change > 0:
                if self._change // coins[i] > 0:
                    changes = changes + str(coins[i]) + ","
                    self._change = self._change - coins[i]
                else:
                    i = i+1
            changes = changes[:-1]
            return changes



        # elif cmd == "음료":
        #     drink = params[0]
        #     if drink != "커피":
        #         return "알 수 없는 음료입니다."
        #     else:
        #         price = 150
        #         if self._change >= price:
        #             self._change = self._change - price
        #             return "커피가 나왔습니다."
        #         else :
        #             return "잔액이 부족합니다."
        else:
            return "알 수 없는 명령입니다."


# def init():
#     global change
#     change = 0
#
# def run(raw):
#     global change
#
#     tokens = raw.split(" ")
#     cmd, params = tokens[0], tokens[1:]
#
#     if cmd == "잔액":
#         return "잔액은 " + str(change) + "원입니다"
#     elif cmd == "동전":
#         coin = params[0]
#         change += int(coin)
#         return coin + "원을 넣었습니다"
#     else:
#         return "알 수 없는 명령입니다."
