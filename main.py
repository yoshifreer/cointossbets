import random

money = 10000
total_coin_flips = 0
bet = 1

while money > 0:
    # bet = bet * 2
    if random.randint(0,1) == 1:
        money = money + bet
        # bet = 1
    else:
        money = money - bet
    total_coin_flips = total_coin_flips + 1
    if total_coin_flips % 1000000 == 0:
        print(f"total_coin_flips = {total_coin_flips}")
        print(f"money = {money}")
    # input()

print(f"You lost all your money in {total_coin_flips} coin flips.")