n = int(input())
budget = n * 0.8

case_one = n - n * 0.22
case_two = n - (n - budget) * 0.22

print(int(case_one), int(case_two))