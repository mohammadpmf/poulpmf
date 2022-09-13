# print(eval('5**9.3-3/9*7*8'))

# # 5! = 5*4*3*2*1 = 120
# # 6! = 6*5*4*3*2*1 = 720
# # n! = n*(n-1)!
# # 1! = 1
# # recursive functions => tavabe e bazgashti توابعی که خودشون رو صدا میکنند.
# def fact1(n=1):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i
#         # ans = ans * i
#     return ans
# def fact2(n=1):
#     if n==1:
#         return 1
#     return n*fact2 (n-1)
# # print(fact1(3))
# print(fact2(3))
# fib(n)
# 1,1,2,3,5,8,13,21,34,55,89,144, ...
# [1,1]
# f(0) = 1
# f(1) = 1
# f(2) = f(0) + f(1) = 1+1=2
# f(3) = f(1) + f(2) = 1+2=3
# .
# .
# .
# f(n) = f(n-1) + f(n-2)

def fib1(n):
    mylist = [1,1]
    i = 2
    while i<n:
        mylist.append(mylist[i-2]+mylist[i-1])
        i += 1
    return mylist[i-1]
print(fib1(11))

def fib2(n):
    if n==1 or n==2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
print(fib2(11))
