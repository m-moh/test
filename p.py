# Q1 What is the problem with this code?

def foo(bar=[]):        
    bar.append("baz")
    return bar


# Q2 What is the output of this code?

x = 10
def foo():
    x += 1
    print x



# Q3 What is the output of this code?

lst = [1, 2, 3]
def foo1():
    lst.append(5)
    print(lst)

foo1()


# Q4 What is the output of this code?

lst = [1, 2, 3]
def foo2():
    lst += [5]
    print(lst)

foo2()


# Q5 What is the output of this code?

odd = lambda x : bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        del numbers[i]
        
        
