from collections import deque
bank = deque(["mim", "faria", "farhad", "binita"])
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("No person left")