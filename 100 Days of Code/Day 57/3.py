# Paren-Magic
def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False

    if stack:
        return False
    return True


t = int(input())
while t != 0:
    s = input()
    l = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            l.append(s[i:j])
    # print(l)
    x = 0
    y = ""
    for i in l:
        if len(i) > x:
            if areBracketsBalanced(i):
                x = len(i)
                y = i
    print(y)
    t = t - 1
