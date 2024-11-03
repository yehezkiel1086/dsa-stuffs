if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    l_arr = list(arr)
    l_arr.sort()
    s_arr = list(set(l_arr))
    print(s_arr[-2])