import sys


blue_count = 0
white_count = 0

def paper_cut(paper:list):
    global blue_count
    global white_count

    color_set = set()
    for i in range(len(paper)):
        color_set.update(set(paper[i]))

    if len(color_set) == 1: # 모든 부분이 같은 색
        if color_set == {0}: #흰색
            white_count += 1
        elif color_set == {1}: # 파란색
            blue_count += 1
    else:
        left_top = []
        right_top = []
        left_bottom = []
        right_bottom = []

        for i in range(len(paper)):
            if i < len(paper) // 2:
                left_top.append(paper[i][0:len(paper[i]) // 2])
                right_top.append(paper[i][len(paper[i]) // 2: len(paper[i])])
            else:
                left_bottom.append(paper[i][0:len(paper[i]) // 2])
                right_bottom.append(paper[i][len(paper[i]) // 2: len(paper[i])])

        paper_cut(left_top) # 좌측 상단
        paper_cut(left_bottom) # 좌측하단
        paper_cut(right_top) #우측 상단
        paper_cut(right_bottom) # 우측 하단


n = int(sys.stdin.readline())

paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

paper_cut(paper)

print(white_count)
print(blue_count)
