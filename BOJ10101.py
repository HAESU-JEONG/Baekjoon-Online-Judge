angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

total = angle1 + angle2 + angle3

if total != 180:
    print("Error")
else:
    if angle1 == 60 and angle2 == 60 and angle3 == 60:
        print("Equilateral")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Isosceles")
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        print("Scalene")