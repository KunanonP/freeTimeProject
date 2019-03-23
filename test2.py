# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # write your code in Python 3.6
    pass
    day = 0
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


    if (S == "Mon"):
        day = 1
    elif (S == "Tue"):
        day = 2
    elif (S == "Wed"):
        day = 3
    elif (S == "Thu"):
        day = 4
    elif (S == "Fri"):
        day = 5
    elif (S == "Sat"):
        day = 6
    elif (S == "Sun"):
        day = 7

    for i in range(0, K):
        day = day + 1
        if day == 8:
            day = 1
    newDay = week[day-1]

    return newDay

def solution2(S, K):

    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = S
    dayWeek = len(week)

    for i in range(0, dayWeek):
        if day == week[i]:
            d = i
            for j in range(0, K):
                d = d + 1
                if d == 7:
                    d = 0
            newDay = (week[d])
            return newDay



test = solution("Sat", 23)
test2 = solution2("Sat",230)
print(test2, test)

