## you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(T):
    # write your code in Python 3.6
    pass
    time = T

    hour = str(time / 3600)
    time %= 3600
    minute = str(time / 60)
    time %= 60
    second = str(time)

    return "%sh%sm%ss" % (hour, minute, second)

solution(83643)
print(solution(83643))

