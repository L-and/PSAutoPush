# 문제
# 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 입력
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
#
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과,
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

test_case = int(input())  # 테스트케이스

for i in range(test_case):
    # 입력
    document_count, target_document_num = map(int, input().split())  # 문서의 개수, 궁금한 문서
    importance = list(map(int, input().split()))  # 중요도

    document_list = list(range(document_count))  # 문서 큐 생성 [0,1,2,3,...,document_count]
    print_count = 0  # 출력한 횟수

    # 상근이의 알고리즘에따라 target 이 몇번쨰로 출력되는지 반복해서 알아낼려함
    while target_document_num in document_list:  # 목표 문서번호가 문서리스트에 없을떄 까지 반복
        if importance[document_list[0]] == max(importance):  # 중요도가 제일 높다면 출력
            importance[document_list[0]] = -1  # 최고 중요도를 -1로 재조정
            document_list.pop(0)  # 출력

            print_count += 1
        elif importance[document_list[0]] < max(importance):  # 중요도가 제일 높지않다면 문서를 큐의 맨뒤로 재배치
            document_list.append(document_list.pop(0))  # 뒤로 재배치


    print(print_count)


