
# def greeting(name,msg):
#     print("Hello",name)
#     print(msg)
# greeting("vikash","Good Morning")


def even(a):
    for i in a:
         if i%2==0:
            print(i)

even([1,2,3,4,5])


def greet(name,mes="Good Morning"):
    print("Hello",name)
    print(mes)
greet("vikash")


def cal(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    elif op=="%":
        return a%b
    else:
        return "invalid operater"
a=cal(12,13,"+")
print(a)
