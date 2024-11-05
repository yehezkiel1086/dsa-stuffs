def binary_search(arr, v):
    l = 0
    h = len(arr) - 1
    
    while l <= h:
        m = l + ((h - l) // 2)
        
        if v == arr[m]:
            return m
        elif v < arr[m]:
            h = m - 1
        else:
            l = m + 1

    return -1

def linear_search(arr, v):
    for i, x in enumerate(arr):
        if x == v:
            return i
    return -1

if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7, 8, 9]
    
    print("searching...")
    # idx = linear_search(arr, 8)
    idx = binary_search(arr, 8)
    print(idx)