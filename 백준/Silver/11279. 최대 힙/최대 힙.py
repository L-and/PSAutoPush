class Heap():
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    def push(self, n):
        index = len(self.heap) # 추가된 n의 인덱스
        self.heap.append(n)

        
        # heapify
        index = len(self.heap) - 1
        while index > 1: # root노드까지 검사
            parent_index = index // 2
            
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] # SWAP
                index = parent_index
            else: # 부모노드와 자식노드간 heaptify가 완료되었다면 그 위의 노드들에 대한 검사는 불필요
                break 

    def pop(self):
        if len(self.heap) == 1: # heap 에 아무 수도 없음
            return 0
        
        # Root node를 뺀 후 last index의 node를 root와 교체
        popped_value = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]

        # heapify
        index = 1
        heap_len = len(self.heap)
        while index < heap_len: # last node까지 검사
            parent_index = index
            left_child_index = parent_index * 2
            right_child_index = (parent_index * 2) + 1
            largest_index = parent_index

            if left_child_index < heap_len and self.heap[left_child_index] > self.heap[largest_index]: # 좌측 자식노드가 존재하며 부모보다 큼
                largest_index = left_child_index
            
            if right_child_index < heap_len and self.heap[right_child_index] > self.heap[largest_index]: # 우측 자식노드가 존재하며 부모, 좌측노드보다 큼(이전에 if문을 거쳤으니 부모, 좌측노드중 뭐가 더큰지는 모름)
                largest_index = right_child_index

            if largest_index == parent_index: # 부모노드가 가장 큰노드 == 더이상 heaptify는 불필요
                break

            self.heap[largest_index], self.heap[parent_index] = self.heap[parent_index], self.heap[largest_index] # SWAP
            index = largest_index


        return popped_value

import sys

heap = Heap()

n = int(input())
print_count = 0

for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        sys.stdout.writelines(str(heap.pop())+'\n')
    else:
        heap.push(num)
