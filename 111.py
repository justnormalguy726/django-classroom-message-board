"""
name = "传值博客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price},每日增长系数是：{stock_price_daily_growth_factor},经过{growth_days}天后的股价将是：{stock_price * (stock_price_daily_growth_factor ** growth_days)}")
"""
"""
print("请告诉我你的银行卡号：")
name = input()
print("懂了，你的卡号是：%s"%name)
"""
"""
user_name = input("请输入你的用户名：")
user_type = input("请输入你的用户类型：")
print("欢迎！%s,你是%s用户" % (user_name, user_type))
"""

"""
num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")
"""
"""
age = input("请输入你的年龄：")
print("欢迎来到黑马游乐园，儿童免费，成人收费，请输入你的年龄：%s" % age)
if int(age) < 18:
    print("你是儿童，免费入园")
else:
    print("你是成人，补票十元入园")
"""
"""
sum = 0
i = 1
while i<= 100:
    sum += i
    i += 1
print("和为%s"%sum)
"""
"""
i = 1
while i <= 100:
    print(f"今天是向小美表白的第{i}天")
    j = 1
    while j <= 10:
        print(f"今天送给小美{j}朵玫瑰花")
        j += 1
    print("小美我喜欢你")
    i += 1
print(f"在第{i}天，小美答应我的表白了")
"""
"""
i = 1
while i<= 9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}",end="\t")
        j += 1
    i += 1
    print()
"""
"""
函数定义
def 函数名(传入参数):
    函数体
    return 返回值
调用函数
函数名(传入参数)
"""
"""
def say_hi():
    print("hi")
say_hi()
"""
"""
传参定义
函数定义时给的参数是传参，函数使用时给的参数是实参
函数返回值
程序中函数完成后，最后给调用者的结果
"""
"""
def add(x,y):
    result = x + y
    print(f"{x}+{y}={result}")
add(2,3)
"""
"""
def add(a,b):
    result = a + b
    return result
r = add(2,3)
print(r)
"""
"""
def say_hi():
    return "hi"
result = say_hi()
print(result)
"""
"""
money = 5000000
name = input("请输入你的名字：")

def check(show_header):
    if show_header:
        print("-------余额-------")
    print(f"{name},您好，您的存款余额为{money}元")

def saving(num):
    global money
    money += num
    print("-------存款-------")
    print(f"{name},您好，存入{num}元")
    check(False)

def get_money(num):
    global money
    money -= num
    print("-------取款-------")
    print(f"{name},您好，取出{num}元")
    check(False)

def main():
    print("-------主菜单-------")
    print(f"{name},您好，欢迎来到银行，请选择您的操作：")
    print("查询余额\t请输入1")
    print("存款\t\t请输入2")
    print("取款\t\t请输入3")
    print("退出\t\t请输入4")
    return input("请输入您的选择:")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        check(True)
    elif keyboard_input == "2":
        num = int(input("您想存入多少钱："))
        saving(num)
    elif keyboard_input == "3":
        num = int(input("您想取出多少钱："))
        get_money(num)
    else:
        print("退出程序")
        break
"""
"""
数据容器:一种可以存储多种元素的python数据类型
列表，元组，字符串，集合，字典


列表定义：
#字面量
[元素1,元素2,元素3,......]

#定义变量
变量名称 = [元素1,元素2,元素3,.....]

#定于空列表
变量名称 = []
变量名称 = list()
列表可以一次存储多个数据，且可以为不同数据类型，支持嵌套

#嵌套列表
变量名称 = [[1,2,3],[4,5,6]]
"""
"""
#下标索引（不能超出列表范围）
语法:列表[下表索引]0,1,2,...
#反向索引
-5,-4,-3,-2,-1  最后一个元素是-1。向前递减
列表嵌套同理
"""
"""
my_list = ['Tom','Lily','Rose']
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
"""
#取出嵌套元素列表
"""
my_list = [[1,2,3],[4,5,6]]
print(my_list[1][1])
"""
#列表的切片
"""
my_list = [1,2,3,4,5,6]
print (my_list[:-1])
"""

#查找元素所在索引
#语法:列表.index(元素)
"""
mylist = ['wang','yi','xiao']
index = mylist.index('yi')
print(f"yi在mylist中的索引是{index}")
"""
#如果查找的元素不存在，会显示错误

#修改特定位置(索引)的元素值
#语法:；列表[下标]=值
"""
mylist[0] = "王"
print(f"修改后的元素为{index}")
"""


"""
#插入元素
#语法：列表.insert(下标，元素)   在指定的位置插入指定的元素

mylist.insert(3,"牛逼")
print(f"修改后的元素为{mylist}")
"""


#追加元素
#语法：列表.append(元素)     将指定的元素追加到列表的尾部
"""
mylist.append("plus")
print(f"修改完的列表为{mylist}")
"""


#追加一批元素为
#语法:  列表.extend(元素)
"""
mylist = ['wang','yi','xiao']
mylist.extend([29,30,31])
print(f"修改后的列表为{mylist}")
"""
#列表删除元素方法
#1.   del 列表[下标]
"""
mylist = ['wang','yi','xiao']
del mylist[2]
print(f"修改后的列表为{mylist}")
"""

#2.   列表.pop(下标)


#列表删除第一个匹配项
#列表.remove(元素)

#清空列表
#列表.clear()

#统计某一元素在列表中的数量
#列表.count(元素)

#统计列表全部元素数量
#len(列表)

"""
列表的遍历,while循环
index = 0
    while index < len(列表):
    元素 = 列表[index]
    对元素进行处理
    index += 1
"""
"""
mylist = ['wang','yi','xiao']
index = 0
while index < len(mylist):
    element = mylist[index]
    print(f"列表的元素{index}")
    index += 1
"""
"""
列表的遍历，for循环
for 临时变量 in 数据容器:
    对临时变量进行处理
"""
"""
def list_for_func():
    mylist = [1,2,3,4,5]
    for element in mylist:
        print(f"for循环内的元素为{element}")
list_for_func()
"""
#元组   （元素1，元素2，元素3，......）
#定义元组
#t1 = (1,'Hello',True)
#定义单个元素的元组，最后必须加逗号,
"""
#元组的嵌套
t2 = ((1,2,3),(4,5,6))

#元组中下标元素的索引
num = t2[1][2]
print(f"取出的元素是{num}")
"""
"""
#元组中的操作
#index()
t6 = ('wang','yi','xiao')
index = t6.index('wang')
print(f"{index}")

#count()
t7 = ('wang','yi','xiao',6,6,6)
count = t7.count(6)
print(f"{count}")
"""
"""
#len(元组)
t8 = ('王','翼','啸','牛逼')
shuliang = len(t8)
print(f"{shuliang}")


#元组的遍历while
index = 0
while index < len(t8):
    print(f"元组的元素有{t8[index]}")
    index += 1

#元组的遍历for
for element in t8:
    print(f"{element}")
"""
#元组内的元素不能被修改，但元组内嵌套的list可以被修改
"""
t9 = ('王','翼','啸',[1,2])
t9[3][0] = '牛'
t9[3][1] = '逼'
print(f"{t9}")
"""
#字符串相关操作(不可修改的数据容器)
#取值
"""
my_str = "wang yi xiao nb"
value = my_str[0]
value2 = my_str[-1]
print(f"取的值为{value}{value2}")

#index操作
index= my_str.index("xiao")
print(f"取的值为{index}")

#字符串的替换
#语法：字符串.replace(字符串1，字符串2)   1为被替换的，2为替换的
new_my_str = my_str.replace("nb","666")
print(f"新的字符串为{new_my_str}")
"""

"""
#字符串的分割   
#语法；字符串.split(分隔符字符串)   按照指定的字符串分隔符，将字符串划分为多个字符串并存入列表当中
my_str = "wang yi xiao nb"
my_new_list = my_str.split(" ")
print(f"新的列表为{my_new_list}")
print(f"类型是{type(my_new_list)}")
"""

#字符串的规整操作
#语法:字符串.strip()    去除字符串前后空格
"""
mystr = " 王 "
new_mystr = mystr.strip( )
print(f"{new_mystr}")

#    字符串.strip(字符串)    去除字符串前后字符
mystr = "12王21"
new_mystr = mystr.strip("12")
print(f"{new_mystr}")
"""
#序列语法   序列[起始下标:结束下标:步长]  步长表示取元素的间隔  1表示1个1个取  2表示跳一个跳一个取 以此类推  N表示N-1个取  步长为负数，反向取
"""
my_list = [0,1,2,3,4,5]
result1 = my_list[1:-2:1]
print(f"{result1}")
"""
#集合：{}
#字典：通过key找到对应的value   定义{key:value,key:value}


#设计类
"""
class student:
    name = None
    gender = None
   #设计一个类

stu_1 = student()
    #创建一个对象

stu_1.name = "wang"
stu_1.gender = "male"
stu_2 = student()
stu_2.name = "yi"
stu_2.gender = "male"
    #给对象赋值

print(stu_1.name)
print(stu_1.gender)
    #获取对象中存储的信息

"""

#类的定义   
"""
# 语法：
class 类的名称
    类的属性（定义在类中的变量）
    类的行为（定义在类中的函数）
创建类对象的语法:
对象 = 类名称()
"""
"""
函数：写在类外    方法：写在类内


类的行为（方法）  写在类内的函数



def 方法名(self,形参1,....形参N)    self:定义在类内部是必须加上的，表示类本身
    方法体
"""

#构造方法__init__
#魔术方法     __   __（统称为魔术方法）有__init__,__str__
"""
class Student:
    name = None
    age = None
    def say_hi(self):
        print(f"hi,大家好,我的名字是{self.name}")
stu = Student()
stu.name = "ishao"
stu.say_hi()
stu2 = Student()
stu2.name = "王翼啸"
stu2.say_hi()
"""

"""
程序中设计表格 == 设计类
class Student:
    name = None

程序中打印生产表格 == 创建对象
stu_1 = Student()
stu_2 = Student()

程序中填写表格 == 对象属性赋值
stu_1.name = "找对象"
stu_2.name = "顺利毕业"
stu_3.name = "找工作"

"""