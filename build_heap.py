# python3
# Daniels Raivo Ivanovs 211RMB021 15.grupa

def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            k =2*j + 1
            if k >= n:
                break
            if k +1 < n and data[k + 1] < data[k]:
                k += 1
            if data[j] > data[k]:
                swaps.append((j, k))
                data[j], data[k] = data[k], data[j]
                j = k
            else:
                break  
  
    return swaps


def main():
    
    read_input = input()
    
    if read.startswith('I'):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    elif read.startswith('F'):
        file = input().strip()
        with open(f'data/{file}', 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        
    else:
        print('Invalid character')
     


if __name__ == "__main__":
    main()
