# Evaluate simple expressions like "2+3*4-5/5"
# Supports +, -, *, /

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b  # integer division
    return 0

def evaluate(expression):
    nums = []
    ops = []
    i = 0
    while i < len(expression):
        ch = expression[i]

        if ch == ' ':
            i += 1
            continue

        if ch.isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            nums.append(val)
            continue

        if ch in "+-*/":
            while ops and precedence(ops[-1]) >= precedence(ch):
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(apply_op(a, b, op))
            ops.append(ch)

        i += 1

    while ops:
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        nums.append(apply_op(a, b, op))

    return nums[0]

# Main Execution
print("Simple Expression Evaluator")
print("Enter expressions like: 2+3*4-1 (no brackets)")
while True:
    expr = input(">> ")
    if expr.lower() == "exit":
        break
    try:
        result = evaluate(expr)
        print("Result:", result)
    except:
        print("Invalid expression.")
