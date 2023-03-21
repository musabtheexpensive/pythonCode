from  collections import deque

bank = deque(["Anis","Musab","Nargis","Bijoy"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")