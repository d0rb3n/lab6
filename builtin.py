#ex1
import math
nums = list(map(int, (input().split())))
def multi(nums):
        res = math.prod(nums)
        print(res)
multi(nums)

#ex2 
s = str(input())
def count(s):
        sumu = 0
        suml = 0
        for x in s:
            if x.isupper():
                sumu+=1
            else:
                suml += 1
        print('upper:', sumu, 'lower:', suml)
count(s)

#ex3
s = input() 
slist = [] 
rev = reversed(s)
srev = [] 
for x in s: 
    slist.append(x) 
for z in rev: 
    srev.append(z) 
if srev == slist: 
    print('palindrome') 
else: 
    print('not palindrome')

#ex4
import math 
import threading 
n = int(input())
mil = float(input())
def delayed_sqrt(n, mil):  
    sec = mil / 1000  
    def calculate_sqrt(): 
        result = math.sqrt(n) 
        print(f"Square root of {n} after {mil} milliseconds is {result}") 
    timer = threading.Timer(sec, calculate_sqrt) 
    timer.start() 
delayed_sqrt(n, mil)

#ex5
tup = tuple(map(int, (input().split())))
def alltrue(t):
    x = all(t)
    print(x)
alltrue(tup)