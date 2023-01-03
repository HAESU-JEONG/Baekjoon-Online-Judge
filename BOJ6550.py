while True:
    try: 
        string1, string2 = input().split()
        cnt = 0
        flag = 0

        for i in range(len(string2)):
            if string2[i] == string1[cnt]:
                cnt += 1
                if cnt == len(string1):
                    flag = 1
                    break
        
        if flag == 1:
            print("Yes")
        else:
            print("No")
    except:
        break