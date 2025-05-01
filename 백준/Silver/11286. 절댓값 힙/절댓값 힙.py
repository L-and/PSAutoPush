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
            
            # 부모노드와 자식노드간의 절대값의 비교하는 플래그
            parent_big_flag = abs(self.heap[index]) < abs(self.heap[parent_index])
            # 부모노드와 자식노드간의 절대값이 동일한지를 비교하는 플래그
            abs_equal_flag = abs(self.heap[index]) == abs(self.heap[parent_index])

            if parent_big_flag:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] # SWAP
                index = parent_index
            elif abs_equal_flag:
                # 절댓값이 동일할 시 더 작은 노드를 부모노드로 설정해 줌
                if self.heap[index] < self.heap[parent_index]:
                    self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] # SWAP
                    index = parent_index
            
                # 부모노드와 자식노드가 동일할 경우 index의 변화가없어서 무한루프에 빠지게되니 break
                else:
                    break

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
            smallest_index = parent_index

            if left_child_index < heap_len and abs(self.heap[left_child_index]) < abs(self.heap[smallest_index]): # 좌측 자식노드가 존재하며 최소값 노드보다 작음
                smallest_index = left_child_index
            # 최소값 노드가 왼쪽노드와 동일하며 더 크다
            if (left_child_index < heap_len and 
                abs(self.heap[left_child_index]) == abs(self.heap[smallest_index]) and
                self.heap[left_child_index] < self.heap[smallest_index]
                ):
                smallest_index = left_child_index
            
            if right_child_index < heap_len and abs(self.heap[right_child_index]) < abs(self.heap[smallest_index]): # 우측 자식노드가 존재하며 최소값 노드보다 작음
                smallest_index = right_child_index

            # 최소값 노드가 오른쪽노드와 동일하며 더 크다
            if (right_child_index < heap_len and 
                abs(self.heap[right_child_index]) == abs(self.heap[smallest_index]) and
                self.heap[right_child_index] < self.heap[smallest_index]
                ):
                smallest_index = right_child_index

            if smallest_index == parent_index: # 부모노드가 가장 큰노드 == 더이상 heaptify는 불필요
                break

            self.heap[smallest_index], self.heap[parent_index] = self.heap[parent_index], self.heap[smallest_index] # SWAP
            index = smallest_index


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
