import random

n = int(input("hoeveel lijstjes wilt u zien"))


for i in range(1, n + 1):
    lengte = int(input(f"hoelang moet de lijst {i} zijn"))
    lijst = [random.randint(1, 100) for _ in range(lengte)]
    print(f"lijst {i}: {lijst}")