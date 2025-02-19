import heapq


def main():
    a = []
    
    heapq.heappush(a, 3)
    heapq.heappush(a, 8)
    heapq.heappush(a, 9)
    heapq.heappush(a, 2)
    heapq.heappush(a, 1)
    
    print(heapq.nlargest(3, a))


if __name__ == '__main__':
    main()
