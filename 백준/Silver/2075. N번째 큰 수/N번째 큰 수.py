import sys

class Heap:
    def __init__(self):
        self.heap = []
        self.flag = 0 # 0=Falsem 1=left, 2=right (heaptify_up 할 때 어떤 자식노드와 변경해야 할 지를 나타내는 변수)
        self.heap.append(None)

    def heaptify_down(self, idx): # heap pop 했을 때 heaptify 하는 함수
        length = len(self.heap) - 1

        left_child_idx = idx * 2
        right_child_idx = idx * 2 + 1

        if left_child_idx > length: # 자식노드가 없음
            self.flag = 0
            return False
        elif right_child_idx > length: # 노드가 1개 뿐임

            if self.heap[idx] > self.heap[left_child_idx]:
                self.flag = 1
                return True
            else:
                self.flag = 0
                return False
        else:
            if self.heap[left_child_idx] < self.heap[right_child_idx]:
                small_child_idx = left_child_idx
                self.flag = 1
            else:
                self.flag = 2
                small_child_idx = right_child_idx

            if self.heap[idx] > self.heap[small_child_idx]: # 왼쪽 노드보다 부모노드가 큼
                return True
            else:
                return False
        

    def heaptify_up(self, idx): # heap push했을 때 heap조건에 맞게 정렬되었는지 검사하는 함수(부모노드와 비교)
        if idx <= 1: # 노드가 1개 뿐 일때
            return False
        
        parent_idx = idx // 2

        if self.heap[parent_idx] > self.heap[idx]: # 부모 노드가 현재 노드보다 작을 때
            return True

    def heap_push(self, data):
        self.heap.append(data) # 힙에 데이터 추가

        idx = len(self.heap) - 1

        while self.heaptify_up(idx): # list를 heaptify 해 줌
            parent_idx = idx // 2
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx] # 스왑 해 줌
            idx = parent_idx

    def heap_pop(self):
        if len(self.heap) <= 1:
            return 0

        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            # root노드를 pop 하기위해 저장 후 맨 마지막 노드를 루트노드로 이동(heaptify하기 위해서)
            pop_data = self.heap[1]
            self.heap[1] = self.heap.pop()

            # list를 heaptify
            idx = 1 # 부모노드부터 시작
            while self.heaptify_down(idx):

                if self.flag == 1:
                    left_child_idx = idx * 2
                    self.heap[idx], self.heap[left_child_idx] = self.heap[left_child_idx], self.heap[idx]
                    idx = left_child_idx
                elif self.flag == 2:
                    right_child_idx = idx * 2 + 1
                    self.heap[idx], self.heap[right_child_idx] = self.heap[right_child_idx], self.heap[idx]
                    idx = right_child_idx



            return pop_data
    

heap = Heap()

n = int(sys.stdin.readline())

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        if len(heap.heap) < n + 1:
            heap.heap_push(data[i])
        else:
            if data[i] > heap.heap[1]:
                heap.heap_pop()
                heap.heap_push(data[i])

print(heap.heap[1])
