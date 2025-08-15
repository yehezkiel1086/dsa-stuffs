if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    l_arr = sorted(list(set(arr)))
    print(l_arr[-2])