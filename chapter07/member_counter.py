class MemberCounter:
    members = 0

    def __init__(self) -> object:
        MemberCounter.members += 1


m1 = MemberCounter()
print(f"MemberCounter.members = {MemberCounter.members}")
m2 = MemberCounter()
print(f"MemberCounter.members = {MemberCounter.members}")
# zhengjuns-MacBook-Pro:chapter07 zhengjun$ python3 member_counter.py
# MemberCounter.members = 1
# MemberCounter.members = 2