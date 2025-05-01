test_case = int(input())


for case in range(test_case):

    floors = int(input())
    rooms = int(input())
    floors = floors + 1
    
    room = [[0 for col in range(rooms)] for row in range(floors)]

    for i in range(rooms):
        room[0][i] = i+1
        
    
    
    for i in range(1,floors):
        for j in range(rooms):
            for k in range(j+1):
                room[i][j] = room[i][j] + room[i-1][k]

    # for i in range(1,floors):
    #         for j in range(rooms):
    #             print(room[i][j], end=' ')
    #         print()

    print(room[floors-1][rooms-1])