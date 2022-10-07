L,  P = map(int, input().split())
participant_list = list(map(int, input().split()))
standard = L * P

for person in participant_list:
    print(person - standard, end = " ")