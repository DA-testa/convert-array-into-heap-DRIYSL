# python3


def build_heap(data):
    swaps = []
    size = len(data)
    
    for i in range(size // 2, -1, -1):
        while True:
            min_element = i
            left_child = 2*i + 1
            right_child = 2*i + 2
            
            if left_child < size and data[left_child] < data[min_element]:
                min_element = left_child
            if right_child < size and data[right_child] < data[min_element]:
                min_element = right_child
                
            if i == min_element:
                break
                
            swaps.append((i, min_element))
            data[i], data[min_element] = data[min_element],data[i]
            
            i = min_element
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input().strip())
    data = list(map(int, input().strip().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    
    mode = input().strip()
    
    assert mode == 'I' or mode == 'F'
    
    swaps = []
    if mode == 'F':  # read data from file
        with open('swap.txt', r) as file:
            for line in file:
                swaps.append(tuple(map(int, line.split())))
    
    if mode == 'I':
        swaps = build_heap(data)
        
    valid = all(data[i] <= data[2*i +1] and data[i] <= 2*i +2 for i in range (n//2))

    # calls function to assess the data 
    # and give back all swaps

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i in swaps:
        print(i[0], i[1])


if __name__ == "__main__":
    main()
