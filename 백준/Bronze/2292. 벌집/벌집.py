def CheckRooms(number):
    run = True
    cnt = 0

    number = number - 1

    while(run):
        if number >  6*cnt:
            number = number - 6*cnt
            cnt = cnt +1
        else:
            run = False

    return cnt+1

print(CheckRooms(int(input())))