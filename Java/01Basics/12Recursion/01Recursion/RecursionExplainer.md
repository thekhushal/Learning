# Java Recursion

## What is Recursion?

**Recursion** is a programming technique where a method **calls itself** to solve a problem.

Instead of solving the entire problem at once, the method solves **one small part** and then calls itself to solve the remaining part.

Think of it like a person standing between two mirrors. The same image appears repeatedly until it eventually stops. In recursion, the repetition stops because of the **base case**.

---

# The Two Rules of Recursion

Every recursive function must have **two parts**:

## 1. Base Case

The condition where recursion stops.

Without a base case, the function keeps calling itself forever, eventually causing a **StackOverflowError**.

```java
if (n == 0)
    return;
```

---

## 2. Recursive Case

The function calls itself with a smaller (or simpler) version of the problem.

```java
function(n - 1);
```

Each recursive call should move closer to the base case.

---

# General Structure

```java
returnType function(parameters) {

    // Base Case
    if (condition)
        return value;

    // Recursive Case
    return function(smallerProblem);
}
```

---

# Example 1: Print Numbers from N to 1

```java
public class Main {

    static void printNumbers(int n) {

        // Base Case
        if (n == 0)
            return;

        System.out.println(n);

        // Recursive Call
        printNumbers(n - 1);
    }

    public static void main(String[] args) {
        printNumbers(5);
    }
}
```

Output

```
5
4
3
2
1
```

---

## Step-by-Step Execution

Call:

```java
printNumbers(5);
```

Execution:

```
printNumbers(5)
    prints 5
    calls printNumbers(4)

        prints 4
        calls printNumbers(3)

            prints 3
            calls printNumbers(2)

                prints 2
                calls printNumbers(1)

                    prints 1
                    calls printNumbers(0)

                        Base Case
                        return
```

Notice that every call waits until the next call finishes.

---

# What Happens in Memory?

Each method call gets its own **Stack Frame**.

```
Top of Stack
-----------------
printNumbers(0)
-----------------
printNumbers(1)
-----------------
printNumbers(2)
-----------------
printNumbers(3)
-----------------
printNumbers(4)
-----------------
printNumbers(5)
-----------------
```

When the base case is reached:

```
printNumbers(0) returns
↓

printNumbers(1) returns
↓

printNumbers(2) returns
↓

printNumbers(3) returns
↓

printNumbers(4) returns
↓

printNumbers(5) returns
```

The stack is emptied one frame at a time.

---

# Example 2: Factorial

Mathematically,

```
5! = 5 × 4 × 3 × 2 × 1
```

Recursively,

```
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1
```

Code:

```java
public class Main {

    static int factorial(int n) {

        // Base Case
        if (n == 1)
            return 1;

        // Recursive Case
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {

        int ans = factorial(5);

        System.out.println(ans);
    }
}
```

Output

```
120
```

---

## Step-by-Step Calls

```
factorial(5)

= 5 × factorial(4)

= 5 × (4 × factorial(3))

= 5 × (4 × (3 × factorial(2)))

= 5 × (4 × (3 × (2 × factorial(1))))

= 5 × (4 × (3 × (2 × 1)))

= 120
```

---

# Visualizing the Call Stack

```
factorial(5)
    waits for factorial(4)

        factorial(4)
            waits for factorial(3)

                factorial(3)
                    waits for factorial(2)

                        factorial(2)
                            waits for factorial(1)

                                factorial(1)
                                returns 1

                        returns 2

                returns 6

        returns 24

returns 120
```

Notice how the answers are calculated **while returning**, not while going down.

---

# Example 3: Sum of First N Numbers

Formula:

```
1 + 2 + 3 + ... + n
```

Recursive idea:

```
sum(5)

= 5 + sum(4)

= 5 + 4 + sum(3)

= 5 + 4 + 3 + sum(2)

...
```

Code

```java
public class Main {

    static int sum(int n) {

        if (n == 0)
            return 0;

        return n + sum(n - 1);
    }

    public static void main(String[] args) {

        System.out.println(sum(5));
    }
}
```

Output

```
15
```

---

# Example 4: Print 1 to N

Instead of printing before recursion, print after recursion.

```java
public class Main {

    static void print(int n) {

        if (n == 0)
            return;

        print(n - 1);

        System.out.println(n);
    }

    public static void main(String[] args) {

        print(5);
    }
}
```

Output

```
1
2
3
4
5
```

---

# Why Does This Work?

For `print(3)`:

```
print(3)

calls print(2)

    calls print(1)

        calls print(0)

            return

        prints 1

    prints 2

prints 3
```

Printing happens **after** recursion finishes.

---

# Before vs After the Recursive Call

Printing **before** recursion:

```java
System.out.println(n);
print(n - 1);
```

Output

```
5
4
3
2
1
```

Printing **after** recursion:

```java
print(n - 1);
System.out.println(n);
```

Output

```
1
2
3
4
5
```

---

# How to Think About Recursion

Whenever solving a recursion problem:

1. Identify the smallest problem that can be solved directly (Base Case).
2. Assume the recursive call already works correctly.
3. Use that result to solve the current problem.

This is called the **Leap of Faith**.

Example:

```
factorial(5)

Don't think about all calls.

Simply assume:

factorial(4) correctly returns 24.

Then:

5 × 24 = 120
```

---

# Common Mistakes

### 1. Forgetting the Base Case

```java
static void fun(int n) {
    fun(n - 1);
}
```

Results in:

```
StackOverflowError
```

---

### 2. Never Moving Toward the Base Case

```java
fun(n);
```

instead of

```java
fun(n - 1);
```

The problem never gets smaller.

---

### 3. Wrong Base Case

Incorrect:

```java
if (n == 10)
    return;
```

Correct (for counting down):

```java
if (n == 0)
    return;
```

---

# When Should You Use Recursion?

Recursion is especially useful when the problem naturally breaks into smaller versions of itself.

Common examples:

* Factorial
* Fibonacci
* Tree traversal
* Binary Search (recursive version)
* Merge Sort
* Quick Sort
* Depth First Search (DFS)
* Backtracking (N-Queens, Sudoku, Maze)
* Generating permutations and combinations

---

# Recursion vs Loop

Loop:

```java
for (int i = 5; i >= 1; i--)
    System.out.println(i);
```

Recursive:

```java
printNumbers(5);
```

Loops are generally:

* Faster
* Use constant memory
* Better for simple repetition

Recursion is generally:

* Easier to write for divide-and-conquer or hierarchical problems
* More intuitive for trees, graphs, and backtracking
* Uses extra memory because each recursive call creates a new stack frame

---

# Key Takeaways

* A recursive method calls itself.
* Every recursive solution needs a **base case** and a **recursive case**.
* Each recursive call should move closer to the base case.
* Every call creates a new stack frame.
* Calls are made while moving **down** the recursion.
* Results are usually produced while returning **up** the recursion.
* Printing before the recursive call processes in forward order; printing after the recursive call processes in reverse order.
* Always verify that recursion will eventually terminate to avoid `StackOverflowError`.
