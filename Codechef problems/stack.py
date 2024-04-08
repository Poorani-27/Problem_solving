MAX_SIZE = 101
a = [0] * MAX_SIZE
top = -1

def push(ele):
    global top
    if top < MAX_SIZE - 1:
        top += 1
        a[top] = ele
        print(f"Pushed: {ele}")
    else:
        print(f"Stack is full. Cannot push: {ele}")

def pop():
    global top
    if top >= 0:
        ele = a[top]
        top -= 1
        print(f"Popped: {ele}")
        return ele
    else:
        print("Stack is empty. Cannot pop.")
        return -1
