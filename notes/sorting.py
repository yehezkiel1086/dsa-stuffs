def partition(arr, l, h):
    
    i = l - 1
    pvt = arr[h]
    
    for j in range(l, h):
        if arr[j] <= pvt:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h] = arr[h], arr[i+1]
    
    return i + 1
    
def quick_sort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)
        
        # left
        quick_sort(arr, l, pi - 1)
        
        # right
        quick_sort(arr, pi + 1, h)

def selection_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[m], arr[i] = arr[i], arr[m]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [7, 12, 9, 11, 3]
    # s_arr = insertion_sort(arr)
    # s_arr = bubble_sort(arr)
    # s_arr = selection_sort(arr)
    
    quick_sort(arr, 0, len(arr) - 1)
    
    print(arr)