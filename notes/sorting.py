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
    s_arr = selection_sort(arr)
    
    print(s_arr)