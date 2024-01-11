from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if food >= order:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left:", *orders)
        break
else:
    print("Orders complete")


# while orders:
#         order = orders.popleft()
#         if food >= order:
#             food -= order
#         else:
#             print(f"Orders left:", order, *orders)
#         break
# else:
#     print("Orders complete")