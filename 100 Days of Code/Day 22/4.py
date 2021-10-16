# HackerEarth (October Circuit's 21)
t = int(input())
while t != 0:
    d = input()
    y = d[4:]
    z = int(y)
    date = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
    ]
    month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    l = []
    for i in date:
        for j in month:
            x = j[::-1] + i[::-1]
            if int(x) <= z:
                l.append(x)
    if len(l) == 0:
        print(-1)
    else:
        l.sort()
        # print(l)
        a = l[-1]
        print(a[::-1] + a)
    t = t - 1
