string = list(input())
ball = [1, 0, 0]

for i in string:
    if i == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif i == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[1], ball[2] = ball[2], ball[0]

print(ball.index(1) + 1)