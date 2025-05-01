def binary_search(card, deck):
    start = 0
    end = len(deck)-1

    while start<=end:
        mid = (start+end) // 2
        
        if deck[mid] == card:
            return 1
        elif deck[mid] > card:
            end = mid - 1
        elif deck[mid] < card:
            start = mid + 1
    
    return 0

n = int(input())

deck = list(map(int, input().split()))

m = int(input())

comparision_deck = list(map(int, input().split()))

deck.sort()

for card in comparision_deck:
    print(binary_search(card, deck), end=' ')