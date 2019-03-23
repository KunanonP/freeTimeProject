# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T, R):
    # write your code in Python 3.6
    pass
    groupT = len(T)
    print(T[3])
    for i in range(0, groupT):
        if "1" in T[i]:
            print T[i]
        elif "2" in T[i]:
            print T[i]
        elif "3" in T[i]:
            print T[i]


T = ['test1a', 'test2', 'test1b', 'test1c', 'test3']
R = ['Wrong answer', 'OK', 'Runtime error', 'OK', 'Time limit exceeded']
solution(T, R)
# print(len(T))

