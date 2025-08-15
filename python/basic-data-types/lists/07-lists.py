if __name__ == '__main__':
    N = int(input())
    
    arr = []
    
    while N:
        cmds = list(input().split(' '))
        cmd = cmds[0]
        
        if cmd == 'insert':
            arr.insert(int(cmds[1]), int(cmds[2]))
        elif cmd == 'print':
            print(arr)
        elif cmd == 'remove':
            arr.remove(int(cmds[1]))
        elif cmd == 'sort':
            arr.sort()
        elif cmd == 'append':
            arr.append(int(cmds[1]))
        elif cmd == 'pop':
            arr.pop()
        elif cmd == 'reverse':
            arr.reverse()
        
        N -= 1