'''#defaultc arguments
def greet(name,vlg,lang="python"):
    print("Hi :"+name)
    print("I am from: "+vlg)
    print("language: "+lang)
greet("Harish","hyd")
greet("rajesh","vij","c")'''


'''def lst(x,y):
    print(x+y)
l1=[10,20,30]
l2=[40,50,60]
lst(l1,l2)'''

'''def lst(s):
    print(s)
l1=[10,20,30,40,50]
lst(l1)'''

'''def lst(s):
    d=0
    res=""
    for i in s:
        if type(i)==int:
            d=d+i
        else:
            res=res+i
    print(d)
    print(res)
l1=[10,"H","A",40,50,"R","T"]
lst(l1)'''

'''#passing function as parameter to another function
def add(x):
    return x+10
def out(r):
    print(r)
out(add(5))'''


'''def add(x):
    return x+15
def out(r):
    print(r)
out(add(5))'''


'''def one():
    def two():
        print("I am from second")
    two()
    print("outer function")
one()'''

'''def rec(n):
    if n==1000:
        return
    print(n)
    n=n+1
    rec(n)
rec(1)'''

'''def rec(n):
    if n==0:
        return
    print(n)
    rec(n-1)
rec(10)'''

def rec(n):
    if n==0:
        return
    print(n)
    rec(n-1)
rec(10)









    
