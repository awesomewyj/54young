from time import sleep

print("C:\AppData\Roaming")


print("py" "thon")

###字符串
x = "abd"
print("C:\AppData\Roaming\\"+x)
print(f"C:\AppData\Roaming\\{x}")
print("C:\AppData\Roaming\\{}\\{}".format(x,123))

###列表
s = [1,4,9,16,25]
print(s[1])
print(s[1:3])
print(s[-2:])

##列表的堆栈  后进先出

s.append("a")
s.append("b")
print(s.pop())


##队列用法   先进先出
from collections import deque
q= [1,4,9,16,2]
quque = deque(q)
quque.append("a")
quque.append("b")
print(quque.popleft())
print(quque.popleft())


###列表创建

x = [x*10 for x in range(10)]
print(x)


###  集合

basket1 = {"a","b","c","d"}
basket1.add("qwe")

basket2 = {"apple","banana","a","b"}

print(basket1.union(basket2))

###字典
d = {"a":1,"apple":"iphone"}
for k , v in d.items():
    print(f"{k}:{v}")



##函数
def num():
    print(2+2)

def fun(a,b=1,*c,**d):
    print(f"a={a}\nb={b}\nc={c}\nd={d}")


print(fun(1))
print(fun(1,2))
print(fun(1,2,3))
print(fun(1,2,3,4))
print(fun(1,2,3,4,5,y=1))


def fun1(*x):
    print(x)

print(fun1(1))
print(fun1(1,2))
m = (1,2,3)
print(fun1(m))
print(fun1(*m))

##类
class Student:
    name = ""
    def study(self,*c):
        print(c)
        return c

student_1 = Student()
student_1.name = "王栎杰"

##类的方法

class Teacher():
    @classmethod
    def share(cls,*c):
        print(c)

print(Teacher.share(1,2,3,888))

from hogwarts.sdetr.Student import Student

Student.study()