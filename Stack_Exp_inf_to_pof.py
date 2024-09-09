def priority(c):
    if c == '^':
        return 2
    elif c == '/' or c == '*':
        return 1
    elif c == '+' or c == '-':
        return 0
    else:
        return -1


def infixtopostfix(s):
    postfix = []
    stack = []
    for i in range(len(s)):
        c = s[i]
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and (priority(s[i]) < priority(stack[-1]) or priority(s[i]) == priority(stack[-1])):
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())
    print("".join(postfix))


s = input()
infixtopostfix(s)