n = int(input())
d = {"S": 0, "M": 1, "L": 2}
for _ in range(n):
    left, right = input().split(" ")

    if d[left[-1]] < d[right[-1]]:
        print("<")
    elif d[left[-1]] > d[right[-1]]:
        print(">")
    else:

        if left[-1] == "S":
            if len(left) > len(right):
                print("<")
            elif len(left) < len(right):
                print(">")
            else:
                print("=")
        else:
            if len(left) > len(right):
                print(">")
            elif len(left) < len(right):
                print("<")
            else:
                print("=")
